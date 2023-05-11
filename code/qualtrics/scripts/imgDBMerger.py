import os
import pandas as pd
from imgUtils import findImgID, findImgURL

if __name__ == "__main__":
    """
    Create a merged database for image information
    """
    # Reference images
    imgNameID_ref = pd.read_csv("imgNameID_Ref.csv")
    imgIDURL_ref = pd.read_csv("imgIDURL_Ref.csv")
    
    imgNames = []
    imgIDs = []
    imgURLs = []
    imgPaths = []
    for field in ["baryon_density", "dark_matter_density", "temperature", "velocity_x"]: #
        for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
            for imgname in imgNameID_ref.imgName.values:
                if "_{}_{}".format(field, colormap) in imgname and "_nobg" not in imgname:
                    imgid  = findImgID(imgNameID_ref, imgname)
                    imgurl = findImgURL(imgIDURL_ref, imgid)
                    
                    imgNames.append(imgname)
                    imgIDs.append(imgid)
                    imgURLs.append(imgurl)
                    imgPaths.append("syncDarwin/images/imageDB/baseline")
                    
    for field in ["baryon_density", "dark_matter_density", "temperature", "velocity_x"]: #
        for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
            for imgname in imgNameID_ref.imgName.values:
                if "_{}_{}".format(field, colormap) in imgname and "_nobg" in imgname:
                    
                    imgid  = findImgID(imgNameID_ref, imgname)
                    imgurl = findImgURL(imgIDURL_ref, imgid)
                    print(imgname)
                    imgNames.append(imgname)
                    imgIDs.append(imgid)
                    imgURLs.append(imgurl)
                    imgPaths.append("syncDarwin/images/imageDB/baseline_nobg")
                    
    imgNameIDURL = pd.DataFrame({"imgName": imgNames, "imgID": imgIDs, "imgURL": imgURLs, "imgPath": imgPaths})
    print(imgNameIDURL.head)
    imgNameIDURL.to_csv("imgNameIDURL_Ref.csv", index=False)
    
    # Target images
    imgNameID_tgt = pd.read_csv("imgNameID_Tgt.csv")
    imgIDURL_tgt = pd.read_csv("imgIDURL_Tgt.csv")

    imgNames = []
    imgIDs = []
    imgURLs = []
    imgPaths = []
    for field in ["baryon_density", "dark_matter_density", "temperature", "velocity_x"]: #
        for comp in ["sz", "zfp"]:
            for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
                for imgname in imgNameID_tgt.imgName.values:
                    if "{}_{}_abs__".format(field, comp) in imgname and "__{}".format(colormap) in imgname and "_nobg" not in imgname:
                        imgid  = findImgID(imgNameID_tgt, imgname)
                        imgurl = findImgURL(imgIDURL_tgt, imgid)

                        imgNames.append(imgname)
                        imgIDs.append(imgid)
                        imgURLs.append(imgurl)
                        imgPaths.append("syncDarwin/images/imageDB/{}_{}_{}".format(field, comp, colormap))

    for field in ["baryon_density", "dark_matter_density", "temperature", "velocity_x"]: #
        for comp in ["sz", "zfp"]:
            for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
                for imgname in imgNameID_tgt.imgName.values:
                    if "{}_{}_abs__".format(field, comp) in imgname and "__{}".format(colormap) in imgname and "_nobg" in imgname:
                        imgid  = findImgID(imgNameID_tgt, imgname)
                        imgurl = findImgURL(imgIDURL_tgt, imgid)

                        imgNames.append(imgname)
                        imgIDs.append(imgid)
                        imgURLs.append(imgurl)
                        imgPaths.append("syncDarwin/images/imageDB/{}_{}_{}_nobg".format(field, comp, colormap))

    imgNameIDURL = pd.DataFrame({"imgName": imgNames, "imgID": imgIDs, "imgURL": imgURLs, "imgPath": imgPaths})
    print(imgNameIDURL.head)
    imgNameIDURL.to_csv("imgNameIDURL_Tgt.csv", index=False)

