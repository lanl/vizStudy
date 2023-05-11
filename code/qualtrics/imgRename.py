import os
import pandas as pd
from imgID_Generator import randomImgID

if __name__ == "__main__":
    """
    rename images in a folder to imgID
    """
    imgName_ref = pd.read_csv("imgName_Ref.csv")
    imgName_tgt = pd.read_csv("imgName_Tgt.csv")
    
    imgList_ref = imgName_ref.imgName.values
    imgList_tgt = imgName_tgt.imgName.values

    
#    for field in ["dark_matter_density"]: # "baryon_density", , "temperature", "velocity_x"
#        for comp in ["sz", "zfp"]:
#            for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
#                # normally do this:
#                dirname = "./imageDB/{}_{}_{}".format(field, comp, colormap)
#                
##                # except for baryon_density_nobg
##                dirname = "./imageDB/{}_{}_{}_nobg".format(field, comp, colormap)
#
#                for imageName in os.listdir(dirname):
#                    if imageName == ".DS_Store":   # ignore those non-image files.
#                        continue
#                    elif imageName in imgList_tgt:     # make sure not to rename imageID
#                        # print(imageName)
#                        imageID = randomImgID(imageName)
#                        # print(os.path.join(dirname, imageName), os.path.join(dirname, "{}.png".format(imageID)))
#                        os.rename(os.path.join(dirname, imageName), os.path.join(dirname, "{}.png".format(imageID)))


#    # for baseline
#    dirname = "./imageDB/baseline"
#    for imageName in os.listdir(dirname):
#        if imageName == ".DS_Store":
#            continue
#        elif imageName in imgList_ref:
#            imageID = randomImgID(imageName)
#            os.rename(os.path.join(dirname, imageName), os.path.join(dirname, "{}.png".format(imageID)))

    # for baseline
    dirname = "./imageDB/baseline_nobg"
    for imageName in os.listdir(dirname):
        if imageName == ".DS_Store":
            continue
        elif imageName in imgList_ref:
            imageID = randomImgID(imageName)
            os.rename(os.path.join(dirname, imageName), os.path.join(dirname, "{}.png".format(imageID)))
