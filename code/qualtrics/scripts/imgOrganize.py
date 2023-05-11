import os
import glob
import shutil

if __name__ == "__main__":
    
    for field in ["dark_matter_density"]: # "baryon_density", , "temperature", "velocity_x"
        for comp in ["sz", "zfp"]:
            for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
            
                #### normally do this:
                try:
                     os.makedirs("./imageDB/{}_{}_{}".format(field, comp, colormap))
                except FileExistsError:
                    # directory already exists
                    pass
                                
                files_to_move = glob.glob("./{}/{}_{}_abs__*__NVB_C009_l10n512_S12345T692_z54__{}.png".format(field, field, comp, colormap))
                
                for source in files_to_move:
                    filename = source.split("/")[2]
                    destination = "./imageDB/{}_{}_{}/{}".format(field, comp, colormap, filename)
                    shutil.copy2(source, destination)
                    
#                #### baryon_density_nobg
#                try:
#                    os.makedirs("./imageDB/{}_{}_{}_nobg".format(field, comp, colormap))
#                except FileExistsError:
#                    # directory already exists
#                    pass
#
#                files_to_move = glob.glob("./{}_nobg/{}_{}_abs__*__NVB_C009_l10n512_S12345T692_z54__{}_nobg.png".format(field, field, comp, colormap))
#
#                for source in files_to_move:
#                    filename = source.split("/")[2]
#                    destination = "./imageDB/{}_{}_{}_nobg/{}".format(field, comp, colormap, filename)
#                    # move file
#                    shutil.copy2(source, destination)
#                    #os.rename(source, destination)

##    for baseline
#    for field in ["baryon_density"]:
#        for colormap in ["blue2cyan", "cool2warm", "jet", "plasma", "viridis"]:
#            try:
#                os.makedirs("./imageDB/baseline_nobg")
#            except FileExistsError:
#                # directory already exists
#                pass
#
#            files_to_move = glob.glob("./baseline/baryon_density_nobg/NVB_C009_l10n512_S12345T692_z54_{}_{}_nobg.png".format(field, colormap))
#
#            for source in files_to_move:
#                filename = source.split("/")[3]
#                destination = "./imageDB/baseline_nobg/{}".format(filename)
#                # move file
#                #print(source, destination)
#                os.rename(source, destination)
