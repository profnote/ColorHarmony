import argparse
import numpy as np
import os
from PIL import Image
from utils import *

PALETTE_SIZE = 150


def print_result(colors, wheel, harmonies):
    print("Extracted colors:")
    print(colors)
    print()
    print("Colors on RGB wheel:")
    print(wheel)
    print()
    print("Harmonies:")
    for harmony in harmonies:
        print(harmony)


def image_result(colors, size, filename):
    # input: array of RGB colors
    num_colors = len(colors)
    palette = np.zeros((size, size * num_colors, 3))
    for c in range(len(colors)):
        palette[:, c * size:c * size + size, 0] = colors[c][0]  # red
        palette[:, c * size:c * size + size, 1] = colors[c][1]  # green
        palette[:, c * size:c * size + size, 2] = colors[c][2]  # blue

    filename = filename + "_colors.png"
    im = Image.fromarray((palette* 255).astype('uint8'), 'RGB')
    im.save(filename, "PNG")
    print("Saved palette as", filename)


def main():
    # create argument parser object and parse arguments
    parser = argparse.ArgumentParser(description="Color Harmony")
    parser.add_argument("image", nargs=1, metavar="PATH", help="Path to image file")
    parser.add_argument("-k", "--clusters", type=int, nargs=1, metavar="clusters",
                        default=[10], help="Number of clusters to perform k-means")
    parser.add_argument("-t", "--tolerance", type=float, nargs=1, metavar="tolerance", default=[1.0],
                        help="Number of standard deviations below the mean chroma to cut-off, defaulted to 1.0")
    parser.add_argument("-o", "--output", type=str, choices=["all", "image", "text"],
                        default="all", help="Format of the output")
    args = parser.parse_args()
    path = args.image[0]
    filename = os.path.splitext(os.path.basename(path))[0]

    # get colors from file and identify harmonies
    img = img_to_numpy(path)
    dc = DominantColors(img, args.clusters[0])
    colors = dc.get_colors()
    main_cols = get_main_colors(colors, args.tolerance[0])
    wheel = colors_on_wheel(main_cols)
    harmonies = get_harmonies(wheel)

    if args.output in ["all", "text"]:
        print_result(main_cols, wheel, harmonies)

    if args.output in ["all", "image"]:
        image_result(main_cols, PALETTE_SIZE, filename)


if __name__ == "__main__":
    main()
