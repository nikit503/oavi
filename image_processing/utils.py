import matplotlib.pyplot as plt
import numpy as np


def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    plt.show()
    return fig, ax


def draw_hist(hist):
    x = np.arange(0, len(hist))
    fig, ax = plt.subplots()
    ax.bar(x, hist, color='darkblue')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    plt.show()