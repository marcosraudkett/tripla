import imageio
import numpy as np

def check_image(img, thrshld):
    is_light = np.mean(img) > thrshld
    return 'light' if is_light else 'dark'
