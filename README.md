# color-harmony.py
A python script that extract main color groups from an image using k-means clustering and returns the color harmony based on the RGB wheel  

## Dependencies
* Python 3.7+
* sklearn
* Pillow
* matplotlib

## Installation
### Pip
The stable releases of gallery-dl are distributed on PyPI and can be easily installed or upgraded using pip:  
```python
$ python3 -m pip install color-harmony
```

### From Source
Clone the repository or download the folder from github, then navigate to the respective directory and run:
```python
python3 setup.py install
```

## Usage
To use *color-harmony*, simply include the path to your image file:  
```python
$ color-harmony [OPTION]... [FilePATH]
```
See also ```python color-harmony --help```.  

### Examples
Default run on an image file will return both RGB colors and create a color palette image with the same name but with *"_colors.png"*:  
```python
$ color-harmony sample.png
```
You can also set the number of clusters, tolerance, and output configurations:
```python
$ color-harmony -k 5 -t 1.5 -o text icon.png
```

## Color Scheme Analysis of Popular Illustrations (Python Notebook on Github)
You will need to download the dataset from: https://www.kaggle.com/profnote/pixiv-popular-illustrations or use your own images.

### ColorSchemeAnalysis.ipynb
Main jupyter notebook for the analysis, can use the data files below:  

### harmonies.csv
File containing the harmonies of each illustration in the dataset.  
Column names: "Monochromatic", "Complementary", "Split Complementary", "Triad", "Square", "Rectangular", "Analogous", "Other"

### wheelColors_arr.csv
Wheel color representations of each illustration in the dataset, starting from Red -> Green -> Blue -> Red.
