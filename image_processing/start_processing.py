from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from skimage.filters import try_all_threshold

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax


def balanced_hist_thresholding(b):
    # Starting point of histogram
    i_s = np.min(np.where(b[0] > 0))
    # End point of histogram
    i_e = np.max(np.where(b[0] > 0))
    # Center of histogram
    i_m = (i_s + i_e) // 2
    # Left side weight
    w_l = np.sum(b[0][0:i_m + 1])
    # Right side weight
    w_r = np.sum(b[0][i_m + 1:i_e + 1])
    # Until starting point not equal to endpoint
    while (i_s != i_e):
        # If right side is heavier
        if (w_r > w_l):
            # Remove the end weight
            w_r -= b[0][i_e]
            i_e -= 1
            # Adjust the center position and recompute the weights
            if ((i_s + i_e) // 2) < i_m:
                w_l -= b[0][i_m]
                w_r += b[0][i_m]
                i_m -= 1
        else:
            # If left side is heavier, remove the starting weight
            w_l -= b[0][i_s]
            i_s += 1
            # Adjust the center position and recompute the weights
            if ((i_s + i_e) // 2) >= i_m:
                w_l += b[0][i_m + 1]
                w_r -= b[0][i_m + 1]
                i_m += 1
    return i_m


if __name__ == '__main__':
    # image = data.camera()
    image = io.imread('D:/photo/velic.jpg')

    # text = data.page()
    # image_show(text)

    fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=False)
    # image_hist = ax.hist(text.ravel(), bins=32, range=[0, 256])
    # ax.set_xlim(0, 256)

    # thresh_value = balanced_hist_thresholding(image_hist)
    # print(thresh_value)
    # plt.imshow(image)
    plt.show()

    # io.imsave('D:/photo/out.jpg', image)
