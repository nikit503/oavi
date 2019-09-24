from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import skimage.data as data
from skimage.exposure import histogram
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


def draw_hist(hist):
    x = np.arange(0, len(hist))
    fig, ax = plt.subplots()
    ax.bar(x, hist, color='darkblue')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')


def get_weight(hist, since, before):
    weight = 0
    for item in hist[since:before]:
        weight += item
    return weight


def balanced_hist_thresholding(hist):
    # Starting point of histogram
    first_index = 0
    # End point of histogram
    last_index = 255
    # Center of histogram
    midle_index = (first_index + last_index) // 2
    # Left side weight
    weight_left = get_weight(hist, first_index, midle_index + 1)
    # Right side weight
    weight_right = get_weight(hist, midle_index + 1, last_index + 1)
    # Until starting point not equal to endpoint
    while (first_index != last_index):
        # If right side is heavier
        if (weight_right > weight_left):
            # Remove the end weight
            weight_right -= hist[last_index]
            last_index -= 1
            # Adjust the center position and recompute the weights
            if ((first_index + last_index) // 2) < midle_index:
                weight_left -= hist[midle_index]
                weight_right += hist[midle_index]
                midle_index -= 1
        else:
            # If left side is heavier, remove the starting weight
            weight_left -= hist[first_index]
            first_index += 1
            # Adjust the center position and recompute the weights
            if ((first_index + last_index) // 2) >= midle_index:
                weight_left += hist[midle_index + 1]
                weight_right -= hist[midle_index + 1]
                midle_index += 1
    return midle_index


if __name__ == '__main__':
    image = data.camera()
    # image = io.imread('D:/photo/velic.jpg')

    hist, hist_centers = histogram(image)
    draw_hist(hist)

    thresh_value = balanced_hist_thresholding(hist)
    print("thresh_value: " + str(thresh_value))

    text_segmented = image > thresh_value
    image_show(text_segmented)

    plt.show()

# io.imsave('D:/photo/out.jpg', image)
