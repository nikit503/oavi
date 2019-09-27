import numpy as np


def _get_weight(hist, since, before):
    weight = 0
    for item in hist[since:before]:
        weight += item
    return weight


def balanced_hist_thresholding(hist):
    first_index = 0
    last_index = 255
    midle_index = (first_index + last_index) // 2
    weight_left = _get_weight(hist, first_index, midle_index + 1)
    weight_right = _get_weight(hist, midle_index + 1, last_index + 1)
    while first_index != last_index:
        if weight_right > weight_left:
            weight_right -= hist[last_index]
            last_index -= 1
            # Adjust the center position and recompute the weights
            if ((first_index + last_index) // 2) < midle_index:
                weight_left -= hist[midle_index]
                weight_right += hist[midle_index]
                midle_index -= 1
        else:
            weight_left -= hist[first_index]
            first_index += 1
            # Adjust the center position and recompute the weights
            if ((first_index + last_index) // 2) >= midle_index:
                weight_left += hist[midle_index + 1]
                weight_right -= hist[midle_index + 1]
                midle_index += 1
    return midle_index


def treshold_image(image, thresh_value):
    print(image.ndim)
    for row_id in range(len(image)):
        for pixel_id in range(len(image[row_id])):
            if image.ndim == 2:
                if image[row_id][pixel_id] > thresh_value:
                    image[row_id][pixel_id] = 255
                else:
                    image[row_id][pixel_id] = 0
            else:
                for px_color_components in range(len(image[row_id][pixel_id])):
                    if image[row_id][pixel_id][px_color_components] > thresh_value:
                        image[row_id][pixel_id] = [255, 255, 255]
                    else:
                        image[row_id][pixel_id] = [0, 0, 0]
    return image
