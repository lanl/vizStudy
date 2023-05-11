# Functions to handle imageDB

def findImgID(imgNameID, imgName):
    return imgNameID[imgNameID.imgName == imgName].imgID.values[0]
    
def findImgName(imgNameID, imgID):
    return imgNameID[imgNameID.imgID == imgID].imgName.values[0]
    
def findImgURL(imgIDURL, imgID):
    if ".png" in imgIDURL.imgID.values[0]:
        return imgIDURL[imgIDURL.imgID == imgID+".png"].imgURL.values[0]
    else:
        return imgIDURL[imgIDURL.imgID == imgID].imgURL.values[0]

def findImgPath(imgNameIDURL, imgID):
    if ".png" in imgNameIDURL.imgID.values[0]:
        return imgNameIDURL[imgNameIDURL.imgID == imgID+".png"].imgPath.values[0]
    else:
        return imgNameIDURL[imgNameIDURL.imgID == imgID].imgPath.values[0]
    
def findImgRef(imgNameIDURL_Ref, imgNameIDURL_Tgt, img_tgt):
    """
    Given the imgID of a target image, find the corresponding imgID of reference image.
    """
    imgPath = imgNameIDURL_Tgt[imgNameIDURL_Tgt.imgID == img_tgt].imgPath.values[0]
  
    if "_sz_" in imgPath:
        imgPath = imgPath.replace("_sz_", "_")
    elif "_zfp_" in imgPath:
        imgPath = imgPath.replace("_zfp_", "_")

    imgname_ref = "NVB_C009_l10n512_S12345T692_z54_{}.png".format(imgPath.split("/", 4)[-1])

    return imgNameIDURL_Ref[imgNameIDURL_Ref.imgName == imgname_ref].imgID.values[0]

