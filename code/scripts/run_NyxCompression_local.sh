#!/bin/bash
export PVPYTHON_PATH=/projects/exasky/ParaView-5.10.0-osmesa-MPI-Linux-Python3.9-x86_64/bin
export ORIGDATA_PATH=/projects/exasky/data/NYX/highz/512 #NVB_C009_l10n512_S12345T692_z54.hdf5
export SZ3_PATH=/projects/exasky/vis_compression/code/VizAly-Foresight/ExternalDependencies/SZ3/install/bin

source $PROJWORK/code/VizAly-Foresight/evn_scripts/VizAly-CBench.bash.darwin

dat=temperature

$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-1.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-1 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-2.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-2 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-3.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-3 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-4.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-4 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-5.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-5 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-6.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-6 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-7.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-7 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-8.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-8 -a 
$SZ3_PATH/sz3 -f -i ${dat}.dat -z ${dat}_sz_rel__9E-9.sz -o ${dat}.sz.out -3 512 512 512 -c sz3.config -M REL 9E-9 -a 
