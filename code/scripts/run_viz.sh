#!/bin/bash
### Visualization script ###

source /projects/exasky/VizAly-Foresight-Dev/evn_scripts/VizAly-CBench.bash.darwin
export PVPYTHON_PATH=/projects/exasky/ParaView-5.10.0-osmesa-MPI-Linux-Python3.9-x86_64/bin
export ORIGDATA_PATH=/projects/exasky/data/NYX/highz/512 #NVB_C009_l10n512_S12345T692_z42.hdf5
export DECOMPDATA_PATH=/projects/exasky/vis_compression/database/decompressed
export STATEFILE_PATH=/projects/exasky/vis_compression/database/state_files
export IMAGE_PATH=/projects/exasky/vis_compression/database/images

img_orig=NVB_C009_l10n512_S12345T692_z54

## New state files
#for var in baryon_density; do #dark_matter_density temperature velocity_x; do
#for cm in blue2cyan cool2warm jet plasma viridis; do
#$PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}_nobg.py $ORIGDATA_PATH/${img_orig}.h5 ${img_orig}.h5 $IMAGE_PATH/${img_orig}_${var}_${cm}_nobg.png 
#done
#done

for var in baryon_density; do # dark_matter_density temperature velocity_x; do

  mkdir -p $IMAGE_PATH/$var

  for dat in $DECOMPDATA_PATH/sz/${var}/*.h5; do    
    for cm in blue2cyan cool2warm jet plasma viridis ; do #
      readarray -d / -t datarr <<< $dat
      export datfile=${datarr[-1]}
      #echo $dat $var $IMAGE_PATH $datfile  $datfile__$cm
      #echo "$PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}.py $dat ${datfile%.*} $IMAGE_PATH/$var/${datfile%.*}__${cm}.png" 
      #$PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}_new.py $dat ${datfile%.*} $IMAGE_PATH/${var}/${datfile%.*}__${cm}_nobg.png
      $PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}_nobg.py $dat ${datfile%.*} $IMAGE_PATH/${var}/${datfile%.*}__${cm}_nobg.png
    done
  done
  for dat in $DECOMPDATA_PATH/zfp/${var}/*.h5; do    
    for cm in blue2cyan cool2warm jet plasma viridis ; do #
      readarray -d / -t datarr <<< $dat
      export datfile=${datarr[-1]}
      #echo $dat $var $IMAGE_PATH $datfile  $datfile__$cm
      #echo "$PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}.py $dat ${datfile%.*} $IMAGE_PATH/$var/${datfile%.*}__${cm}.png" 
      #$PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}_new.py $dat ${datfile%.*} $IMAGE_PATH/${var}/${datfile%.*}__${cm}_nobg.png
      $PVPYTHON_PATH/pvpython $STATEFILE_PATH/${var}_${cm}_nobg.py $dat ${datfile%.*} $IMAGE_PATH/${var}/${datfile%.*}__${cm}_nobg.png
    done
  done
done


