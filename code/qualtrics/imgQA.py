import os
import glob
import random
import array
import numpy as np
import pandas as pd
import time
import math
from decimal import Decimal
import torch
import piq
from skimage.io import imread
from tqdm import tqdm

from imgUtils import findImgPath, findImgRef, findImgName, findImgURL

import warnings
warnings.filterwarnings("ignore")

def mse(x: torch.Tensor, y: torch.Tensor):
    return torch.mean(( (x - y) ** 2), dim = [1, 2, 3])

#  calculate image assessment metrics
def imgAssessment(img_tgt, img_ref):
    x = img_tgt
    y = img_ref

    # print(x, y)
    x = torch.tensor(imread(x)).permute(2, 0, 1)[None, ...] / 255.
    y = torch.tensor(imread(y)).permute(2, 0, 1)[None, ...] / 255.

    if torch.cuda.is_available():
        # Move to GPU to make computaions faster
        x = x.cuda()
        y = y.cuda()

    # image mse
    mse_index: torch.Tensor = mse(x, y)

    # To compute BRISQUE score as a measure, use lower case function from the library
    brisque_index: torch.Tensor = piq.brisque(x, data_range=1., reduction='none')
    # # In order to use BRISQUE as a loss function, use corresponding PyTorch module.
    # # Note: the back propagation is not available using torch==1.5.0.
    # # Update the environment with latest torch and torchvision.
    # brisque_loss: torch.Tensor = piq.BRISQUELoss(data_range=1., reduction='none')(x)
    # print(f"BRISQUE index: {brisque_index.item():0.4f}, loss: {brisque_loss.item():0.4f}")

    # To compute Content score as a loss function, use corresponding PyTorch module
    # By default VGG16 model is used, but any feature extractor model is supported.
    # Don't forget to adjust layers names accordingly. Features from different layers can be weighted differently.
    # Use weights parameter. See other options in class docstring.
    content_loss = piq.ContentLoss(
     feature_extractor="vgg16", layers=("relu3_3",), reduction='none')(x, y)
    # print(f"ContentLoss: {content_loss.item():0.4f}")
    
    # To compute DISTS as a loss function, use corresponding PyTorch module
    # By default input images are normalized with ImageNet statistics before forwarding through VGG16 model.
    # If there is no need to normalize the data, use mean=[0.0, 0.0, 0.0] and std=[1.0, 1.0, 1.0].
    dists_loss = piq.DISTS(reduction='none')(x, y)
    # print(f"DISTS: {dists_loss.item():0.4f}")

    # To compute DSS as a measure, use lower case function from the library
    dss_index: torch.Tensor = piq.dss(x, y, data_range=1., reduction='none')
    # # In order to use DSS as a loss function, use corresponding PyTorch module
    # dss_loss = piq.DSSLoss(data_range=1., reduction='none')(x, y)
    # print(f"DSS index: {dss_index.item():0.4f}, loss: {dss_loss.item():0.4f}")

    # To compute FSIM as a measure, use lower case function from the library
    fsim_index: torch.Tensor = piq.fsim(x, y, data_range=1., reduction='none')
    # # In order to use FSIM as a loss function, use corresponding PyTorch module
    # fsim_loss = piq.FSIMLoss(data_range=1., reduction='none')(x, y)
    # print(f"FSIM index: {fsim_index.item():0.4f}, loss: {fsim_loss.item():0.4f}")

    # To compute GMSD as a measure, use lower case function from the library
    # This is port of MATLAB version from the authors of original paper.
    # In any case it should me minimized. Usually values of GMSD lie in [0, 0.35] interval.
    gmsd_index: torch.Tensor = piq.gmsd(x, y, data_range=1., reduction='none')
    # # In order to use GMSD as a loss function, use corresponding PyTorch module:
    # gmsd_loss: torch.Tensor = piq.GMSDLoss(data_range=1., reduction='none')(x, y)
    # print(f"GMSD index: {gmsd_index.item():0.4f}, loss: {gmsd_loss.item():0.4f}")

    # To compute HaarPSI as a measure, use lower case function from the library
    # This is port of MATLAB version from the authors of original paper.
    haarpsi_index: torch.Tensor = piq.haarpsi(x, y, data_range=1., reduction='none')
    # # In order to use HaarPSI as a loss function, use corresponding PyTorch module
    # haarpsi_loss: torch.Tensor = piq.HaarPSILoss(data_range=1., reduction='none')(x, y)
    # print(f"HaarPSI index: {haarpsi_index.item():0.4f}, loss: {haarpsi_loss.item():0.4f}")

    # To compute LPIPS as a loss function, use corresponding PyTorch module
    lpips_loss: torch.Tensor = piq.LPIPS(reduction='none')(x, y)
    # print(f"LPIPS: {lpips_loss.item():0.4f}")

    # To compute MDSI as a measure, use lower case function from the library
    mdsi_index: torch.Tensor = piq.mdsi(x, y, data_range=1., reduction='none')
    # # In order to use MDSI as a loss function, use corresponding PyTorch module
    # mdsi_loss: torch.Tensor = piq.MDSILoss(data_range=1., reduction='none')(x, y)
    # print(f"MDSI index: {mdsi_index.item():0.4f}, loss: {mdsi_loss.item():0.4f}")

    # To compute MS-SSIM index as a measure, use lower case function from the library:
    ms_ssim_index: torch.Tensor = piq.multi_scale_ssim(x, y, data_range=1.)
    # # In order to use MS-SSIM as a loss function, use corresponding PyTorch module:
    # ms_ssim_loss = piq.MultiScaleSSIMLoss(data_range=1., reduction='none')(x, y)
    # print(f"MS-SSIM index: {ms_ssim_index.item():0.4f}, loss: {ms_ssim_loss.item():0.4f}")

    # To compute Multi-Scale GMSD as a measure, use lower case function from the library
    # It can be used both as a measure and as a loss function. In any case it should me minimized.
    # By default scale weights are initialized with values from the paper.
    # You can change them by passing a list of 4 variables to scale_weights argument during initialization
    # Note that input tensors should contain images with height and width equal 2 ** number_of_scales + 1 at least.
    ms_gmsd_index: torch.Tensor = piq.multi_scale_gmsd(
        x, y, data_range=1., chromatic=True, reduction='none')
    # # In order to use Multi-Scale GMSD as a loss function, use corresponding PyTorch module
    # ms_gmsd_loss: torch.Tensor = piq.MultiScaleGMSDLoss(
    #     chromatic=True, data_range=1., reduction='none')(x, y)
    # # print(f"MS-GMSDc index: {ms_gmsd_index.item():0.4f}, loss: {ms_gmsd_loss.item():0.4f}")

    # To compute PSNR as a measure, use lower case function from the library.
    psnr_index = piq.psnr(x, y, data_range=1., reduction='none')
    # print(f"PSNR index: {psnr_index.item():0.4f}")

    # To compute PieAPP as a loss function, use corresponding PyTorch module:
    # pieapp_loss: torch.Tensor = piq.PieAPP(reduction='none', stride=32)(x, y)
    # print(f"PieAPP loss: {pieapp_loss.item():0.4f}")

    # To compute SSIM index as a measure, use lower case function from the library:
    ssim_index = piq.ssim(x, y, data_range=1.)
    # In order to use SSIM as a loss function, use corresponding PyTorch module:
    # ssim_loss: torch.Tensor = piq.SSIMLoss(data_range=1.)(x, y)
    # print(f"SSIM index: {ssim_index.item():0.4f}, loss: {ssim_loss.item():0.4f}")

    # To compute Style score as a loss function, use corresponding PyTorch module:
    # By default VGG16 model is used, but any feature extractor model is supported.
    # Don't forget to adjust layers names accordingly. Features from different layers can be weighted differently.
    # Use weights parameter. See other options in class docstring.
    style_loss = piq.StyleLoss(feature_extractor="vgg16", layers=("relu3_3",))(x, y)
    # print(f"Style: {style_loss.item():0.4f}")

    # To compute TV as a measure, use lower case function from the library:
    tv_index: torch.Tensor = piq.total_variation(x)
    # # In order to use TV as a loss function, use corresponding PyTorch module:
    # tv_loss: torch.Tensor = piq.TVLoss(reduction='none')(x)
    # print(f"TV index: {tv_index.item():0.4f}, loss: {tv_loss.item():0.4f}")

    # To compute VIF as a measure, use lower case function from the library:
    vif_index: torch.Tensor = piq.vif_p(x, y, data_range=1.)
    # # In order to use VIF as a loss function, use corresponding PyTorch class:
    # vif_loss: torch.Tensor = piq.VIFLoss(sigma_n_sq=2.0, data_range=1.)(x, y)
    # print(f"VIFp index: {vif_index.item():0.4f}, loss: {vif_loss.item():0.4f}")

    # To compute VSI score as a measure, use lower case function from the library:
    vsi_index: torch.Tensor = piq.vsi(x, y, data_range=1.)
    # # In order to use VSI as a loss function, use corresponding PyTorch module:
    # vsi_loss: torch.Tensor = piq.VSILoss(data_range=1.)(x, y)
    # print(f"VSI index: {vsi_index.item():0.4f}, loss: {vsi_loss.item():0.4f}")

    # To compute SR-SIM score as a measure, use lower case function from the library:
    srsim_index: torch.Tensor = piq.srsim(x, y, data_range=1.)
    # # In order to use SR-SIM as a loss function, use corresponding PyTorch module:
    # srsim_loss: torch.Tensor = piq.SRSIMLoss(data_range=1.)(x, y)
    # print(f"SR-SIM index: {srsim_index.item():0.4f}, loss: {srsim_loss.item():0.4f}")

    return [mse_index.item(),     brisque_index.item(), content_loss.item(),  dists_loss.item(), dss_index.item(),
            fsim_index.item(),    gmsd_index.item(),    haarpsi_index.item(), lpips_loss.item(), mdsi_index.item(),
            ms_ssim_index.item(), ms_gmsd_index.item(), psnr_index.item(),    ssim_index.item(), style_loss.item(),
            tv_index.item(),      vif_index.item(),     vsi_index.item(),     srsim_index.item()]

if __name__ == "__main__":

    imgNameIDURL_Ref = pd.read_csv("imgNameIDURL_Ref.csv")
    imgNameIDURL_Tgt = pd.read_csv("imgNameIDURL_Tgt.csv")

    imgIDs = []
    imgNames = []
    imgURLs = []
    imgPaths = []

    mseIndex = []
    brisqueIndex = []
    contentLoss = []
    distsLoss = []
    dssIndex = []
    fsimIndex = []
    gmsdIndex = []
    haarpsiIndex = []
    lpipsLoss = []
    msdiIndex = []
    msssimIndex = []
    msdmsdIndex = []
    psnrIndex = []
    ssimIndex = []
    styleLoss = []
    tvIndex = []
    vifIndex = []
    vsiIndex = []
    srsimIndex = []

    for img_tgt in tqdm(imgNameIDURL_Tgt.imgID.values):
    
        img_ref = findImgRef(imgNameIDURL_Ref, imgNameIDURL_Tgt, img_tgt)
        img_name = findImgName(imgNameIDURL_Tgt, img_tgt)
        img_url = findImgURL(imgNameIDURL_Tgt, img_tgt)
        img_path = findImgPath(imgNameIDURL_Tgt, img_tgt)
        imgtgt_path = "/".join(img_path.split("/", 4)[2:4])
        
        imgref_path = findImgPath(imgNameIDURL_Ref, img_ref)
        imgref_path = "/".join(imgref_path.split("/", 4)[2:4])
        
        [mse_index,    brisque_index, content_loss,  dists_loss, dss_index,
        fsim_index,    gmsd_index,    haarpsi_index, lpips_loss, mdsi_index,
        ms_ssim_index, ms_gmsd_index, psnr_index,    ssim_index, style_loss,
        tv_index,      vif_index,     vsi_index,     srsim_index] = imgAssessment(os.path.join(imgtgt_path, img_tgt+".png"), os.path.join(imgref_path, img_ref+".png"))

        imgIDs.append(img_tgt)
        imgNames.append(img_name)
        imgURLs.append(img_url)
        imgPaths.append(img_path)
        mseIndex.append(mse_index)
        brisqueIndex.append(brisque_index)
        contentLoss.append(content_loss)
        distsLoss.append(dists_loss)
        dssIndex.append(dss_index)
        fsimIndex.append(fsim_index)
        gmsdIndex.append(gmsd_index)
        haarpsiIndex.append(haarpsi_index)
        lpipsLoss.append(lpips_loss)
        msdiIndex.append(mdsi_index)
        msssimIndex.append(ms_ssim_index)
        msdmsdIndex.append(ms_gmsd_index)
        psnrIndex.append(psnr_index)
        ssimIndex.append(ssim_index)
        styleLoss.append(style_loss)
        tvIndex.append(tv_index)
        vifIndex.append(vif_index)
        vsiIndex.append(vsi_index)
        srsimIndex.append(srsim_index)

    img_metrics_data = {
        "imgID":        imgIDs,
        "imgNames":     imgNames,
        "imgURLs":      imgURLs,
        "imgPaths":     imgPaths,
        "mseIndex":     mseIndex,
        "brisqueIndex": brisqueIndex,
        "contentLoss":  contentLoss,
        "distsLoss":    distsLoss,
        "dssIndex":     dssIndex,
        "fsimIndex":    fsimIndex,
        "gmsdIndex":    gmsdIndex,
        "haarpsiIndex": haarpsiIndex,
        "lpipsLoss":    lpipsLoss,
        "msdiIndex":    msdiIndex,
        "msssimIndex":  msssimIndex,
        "msdmsdIndex":  msdmsdIndex,
        "psnrIndex":    psnrIndex,
        "ssimIndex":    ssimIndex,
        "styleLoss":    styleLoss,
        "tvIndex":      tvIndex,
        "vifIndex":     vifIndex,
        "vsiIndex":     vsiIndex,
        "srsimIndex":   srsimIndex
    }

    img_metrics = pd.DataFrame(data = img_metrics_data)
    img_metrics.to_csv("imgQualityMetrics.csv", index=False)


