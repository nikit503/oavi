import skimage.data as data
from skimage.exposure import histogram

from image_processing.treshold import balanced_hist_thresholding, treshold_image
from image_processing.utils import image_show, draw_hist

if __name__ == '__main__':
    # image = data.camera()
    image = data.astronaut()
    # image = io.imread('D:/photo/velic.jpg')

    hist, hist_centers = histogram(image)
    draw_hist(hist)

    thresh_value = balanced_hist_thresholding(hist)
    print("thresh_value: " + str(thresh_value))

    image_binarized = treshold_image(image.copy(), thresh_value)

    image_show(image)
    image_show(image_binarized)

# io.imsave('D:/photo/out.jpg', image)
