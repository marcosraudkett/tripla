import imageio
import numpy as np

def check_image(img):
    dimensions = img.shape
    
    height = img.shape[0]
    width = img.shape[1]

    width_tobe = 1200
    height_tobe = 670

    #is_right = height == height_tobe and width == width_tobe
    #print(str(height) + ' = ' + str(height_tobe))
    if height == height_tobe and width == width_tobe:
        return 'right'
    else:
        return 'wrong'