import skimage.io as io
import skimage.data as data
from skimage.exposure import histogram
import numpy as np
from image_processing.treshold import balanced_hist_thresholding, treshold_image
from image_processing.utils import image_show, draw_hist
from skimage.morphology import disk
from skimage.filters import median


def svertka(window, kernel):
    rez = 0
    matrix_size = len(kernel)
    window_size = len(window)
    # if len(window) != matrix_size:
    #     raise AttributeError("Incorrect window size")

    for elem in range(window_size):
        if len(window[elem]) < matrix_size:
            print(window[elem])
            return 0

    for line in range(matrix_size):
        for row in range(matrix_size):
            rez = rez + window[line][row] * kernel[line][row]
    return rez


if __name__ == '__main__':
    # load images
    image = data.camera()
    # image = data.checkerboard()
    # image = data.astronaut()

    # image = io.imread('D:/photo/pic2.jpg')

    # processing images
    """
         Lab 1 - treshold
    """
    # hist, hist_centers = histogram(image)
    # draw_hist(hist)
    #
    # thresh_value = balanced_hist_thresholding(hist)
    # print("thresh_value: " + str(thresh_value))
    # image_modified = treshold_image(image.copy(), 130)

    """
         Lab 2 - filtering
    """
    image_len = len(image)
    count = 0
    image_modified = image.copy()

    kernel = [
        [0.0625, 0.125, 0.0625],
        [0.125, 1, 0.125],
        [0.0625, 0.125, 0.0625]
    ]

    kernel_test = [
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, -476, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ]

    use_kernel = kernel

    window_size = len(use_kernel)

    kernel_sum = 0
    for line in use_kernel:
        for elem in line:
            kernel_sum += elem

    for line in range(image_len - window_size - 1):
        for row in range(image_len - window_size - 1):
            wind = {}

            for elem in range(window_size):
                wind[elem] = image[line + elem][row:row + window_size]
            image_modified[line + window_size//2][row + window_size//2] = svertka(wind, use_kernel)/kernel_sum
            # print(row, wind, len(wind[0]))

    # svertka(window_test, kernel_test)

    # display images
    image_show(image)
    image_show(image_modified)
    # io.imsave('D:/photo/out.jpg', image)
