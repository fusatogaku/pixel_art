"""
Convert the input image to a pixel art.

alpha = pixel block size. The smaller the value, the rougher the pixel art.
K = color volume.

Reference material:
https://algorithm.joho.info/programming/python/opencv-pixel-art-py/
"""

import os, sys
import numpy as np
import cv2

# subtract color
def sub_color(src, K):
    # lower demension
    Z = src.reshape((-1, 3))

    # convert float32
    Z = np.float32(Z)

    # definision base
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # subtract-color(K-means)
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # convert　UINT8
    center = np.uint8(center)
    res = center[label.flatten()]

    # return Array's dimension and inputImages
    return res.reshape((src.shape))

# Mosaic Proccess
def mosaic(img, alpha):
    
    # image height, width, channels.
    h, w, ch = img.shape

    # mosaic proccessing reducation -> expansion.
    img = cv2.resize(img, (int(w * alpha), int(h * alpha)))
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)

    return img


# Transform Dot Image
def pixel_art(img, alpha=2, K=4):

    # mosaic Proccess
    img = mosaic(img, alpha)

    # substract-color Proccess
    return sub_color(img, K)

# Rename for Argument name and save.
def rename():
    filename, exts = os.path.splitext(sys.argv[1])
    filename = filename.split("/")[-1]
    filename = filename + "_converted" + exts

    return filename

# Get inputImage
img = sys.argv[1]
img = cv2.imread(img, -1)

# Transform DotImage
dst = pixel_art(img, 0.3, 10)

# output result
filename = rename()
path = os.getcwd()
# cv2.imwrite("{0}/converted_img/{1}".format(path, filename), dst)
conv_img = "{0}/converted_img/{1}".format(path, filename)
cv2.imwrite(conv_img, dst)

# show converted image.
cv2.imshow(conv_img, dst)
cv2.waitKey(0)
cv2.destroyAllWindows()