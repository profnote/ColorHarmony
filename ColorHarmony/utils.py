import numpy as np
from sklearn.cluster import KMeans
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D


# convert image to numpy
def img_to_numpy(path):
    img = Image.open(path)
    img = np.array(img.convert("RGB"))
    return img


# K-means clustering
class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None
    HEXCOLS = None

    def __init__(self, image, clusters=3):
        # image as numpy array (RGB)
        self.CLUSTERS = clusters
        self.IMAGE = image

    def get_colors(self):
        img = self.IMAGE

        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        # save image after operations
        self.IMAGE = img

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_

        # save labels
        self.LABELS = kmeans.labels_

        # returning after converting to integer from float
        return self.COLORS.astype(int)


def get_main_colors(colors_arr, tolerance):
    if len(colors_arr) == 0:
        return
    hsv_colors = rgb_to_hsv(colors_arr / 255)
    chroma = hsv_colors[:, 1] * hsv_colors[:, 2]
    cutoff = chroma.mean() - chroma.std() * tolerance
    to_remove = []

    for i in range(len(chroma)):
        if chroma[i] < cutoff:
            to_remove.append(i)

    main_colors = np.delete(colors_arr, to_remove, axis=0)
    return main_colors


def colors_on_wheel(colors_arr):
    # Outputs an array of presence of colors on the RGB color wheel up to tertiary colors (12-split)
    # Red=0,...,Green=4,...,Blue=8

    if len(colors_arr) == 0:
        return
    hues = rgb_to_hsv(colors_arr / 255)[:, 0]
    wheel = [0] * 12
    for i in range(len(hues)):
        for c in range(12):
            lb = c * 1 / 12 - 1 / 24
            ub = c * 1 / 12 + 1 / 24
            if lb < hues[i] < ub:
                wheel[c] = 1
        if hues[i] > 11 / 12:
            # if red > 345 degrees
            wheel[0] = 1
    return wheel


# Color Harmonies
# get color harmony from mainColors
def get_harmonies(wheel_cols):
    # Get the corresponding colors on the RGB wheel from array of RGB colors
    harmonies = []
    if monochromatic(wheel_cols):
        harmonies.append("Monochromatic")
    if complementary(wheel_cols):
        harmonies.append("Complementary")
    if split_complementary(wheel_cols):
        harmonies.append("Split Complementary")
    if triad(wheel_cols):
        harmonies.append("Triad")
    if square(wheel_cols):
        harmonies.append("Square")
    if rectangular(wheel_cols):
        harmonies.append("Rectangular")
    if analogous(wheel_cols):
        harmonies.append("Analogous")

    # If other color combinations
    if sum(wheel_cols) > 1 and len(harmonies) == 0:
        harmonies.append("Other")

    return harmonies


# Harmonies
def monochromatic(wheel_cols):
    return sum(wheel_cols) == 1


def complementary(wheel_cols):
    for curr in range(12):
        opp = (curr + 6) % 12
        if wheel_cols[curr] == 1 and wheel_cols[opp] == 1:
            return True
    return False


def split_complementary(wheel_cols):
    for curr in range(12):
        opp_left = (curr+5) % 12
        opp_right = (curr+7) % 12
        if wheel_cols[curr]==1 and wheel_cols[opp_left]==1 and wheel_cols[opp_right]==1:
            return True
    return False


def triad(wheel_cols):
    for curr in range(12):
        left = (curr+4) % 12
        right = (curr+8) % 12
        if wheel_cols[curr]==1 and wheel_cols[left]==1 and wheel_cols[right]==1:
            return True
    return False


def square(wheel_cols):
    for curr in range(12):
        left = (curr+3) % 12
        right = (curr+9) % 12
        opp = (curr+6) % 12
        if wheel_cols[curr]==1 and wheel_cols[left]==1 and wheel_cols[right]==1 and wheel_cols[opp]==1:
            return True
    return False


def rectangular(wheel_cols):
    for curr in range(6):
        for width in range(1,3):
            left = (curr+width) % 12
            right = (curr+6+width) % 12
            opp = (curr+6) % 12
            if wheel_cols[curr]==1 and wheel_cols[left]==1 and wheel_cols[right]==1 and wheel_cols[opp]==1:
                return True
    return False


def analogous(wheel_cols):
    for curr in range(12):
        right = (curr+1) % 12
        if wheel_cols[curr]==1 and wheel_cols[right]==1:
            return True
    return False

