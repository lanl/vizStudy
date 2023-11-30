# Project Libra

A project to compare two image and output metrics of their differences

## Packages to install

```
conda install -c conda-forge scikit-image
conda install -c conda-forge opencv
conda install matplotlib
```

## Notes

The structure is based on:

- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://github.com/TrevorJA/example_python_project/tree/main


## ToDo
In python
- input: json file; can compute many metrics or just one ( ml training)
- ability to add different metrics
- readable code from the start
- can go inside pip
- use online libraries as much as possible:
 - opencv, …
 - https://pypi.org/project/image-similarity-measures/
 - https://blog.tensorflow.org/2021/09/introducing-tensorflow-similarity.html
 -https://openaccess.thecvf.com/content/CVPR2022W/NTIRE/papers/Gu_NTIRE_2022_Challenge_on_Perceptual_Image_Quality_Assessment_CVPRW_2022_paper.pdf
 - https://pypi.org/project/sewar/

Capabilities:
- Start by comparing basic stuff like image size, quality, …
- Read in input and comparison
- Compute metrics such as ssim, …
- Compute ai based metrics
- Compute image diff in rub, cryk, cue lab,….
- produce image difference in terms of heat map
- Add things like https://research.nvidia.com/publication/flip
- https://datascience.stackexchange.com/questions/48642/how-to-measure-the-similarity-between-two-images
