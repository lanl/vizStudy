#!/bin/bash

curr_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

#for var in baryon_density; do
#  for comp in sz zfp; do
#    for cm in blue2cyan cool2warm jet plasma viridis; do
#
#      foldername=${var}_${comp}_${cm}
#      for img in ${curr_dir}/imageDB/${foldername}/*; do
#        curl --request POST \
#          --url https://iad1.qualtrics.com/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics \
#          --header 'Content-Type: multipart/form-data; boundary=---011000010111000001101001' \
#          --header 'X-API-TOKEN: y938Vu56ku9UUnHRssFEnvnF6csQtkeTUA7WORfU' \
#          --form file=@$img \
#          --form folder=$foldername
#        echo "\n"
#      done
#
#    done
#  done
#done


foldername=baseline_nobg
for img in ${curr_dir}/imageDB/${foldername}/*; do
  curl --request POST \
    --url https://iad1.qualtrics.com/API/v3/libraries/UR_cTIvKxsmN7AzjL0/graphics \
    --header 'Content-Type: multipart/form-data; boundary=---011000010111000001101001' \
    --header 'X-API-TOKEN: y938Vu56ku9UUnHRssFEnvnF6csQtkeTUA7WORfU' \
    --form file=@$img \
    --form folder=$foldername
  echo "\n"
done

