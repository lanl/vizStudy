#!/bin/bash
#
#SBATCH --job-name=run_NyxCompression
#SBATCH --output=run_NyxCompression.log
#SBATCH --partition=skylake-gold
#SBATCH --time=60:00
#SBATCH --nodes=1

export PVPYTHON_PATH=/projects/exasky/ParaView-5.10.0-osmesa-MPI-Linux-Python3.9-x86_64/bin
export ORIGDATA_PATH=/projects/exasky/data/NYX/highz/512 #NVB_C009_l10n512_S12345T692_z54.hdf5

source $PROJWORK/code/VizAly-Foresight/evn_scripts/VizAly-CBench.bash.darwin

mpirun -np 16 $PROJWORK/code/VizAly-Foresight/build/CBench $PROJWORK/code/VizAly-Foresight/inputs/nyx/nyx_img_compression_zfp_abs_baryon_density.json
#mpirun -np 16 $PROJWORK/code/VizAly-Foresight/build/CBench $PROJWORK/code/VizAly-Foresight/inputs/nyx/nyx_img_compression_zfp_abs_dark_matter_density.json
#mpirun -np 16 $PROJWORK/code/VizAly-Foresight/build/CBench $PROJWORK/code/VizAly-Foresight/inputs/nyx/nyx_img_compression_zfp_abs_temperature.json
#mpirun -np 16 $PROJWORK/code/VizAly-Foresight/build/CBench $PROJWORK/code/VizAly-Foresight/inputs/nyx/nyx_img_compression_zfp_abs_velocity_x.json

