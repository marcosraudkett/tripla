# this has the filter dark images and save light images to another folder
import imageio
import numpy as np
import os
import cv2
import darkness_checker
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


outPath = "D:\Path\images-DAYLIGHT"
path = "D:\Path\images"

# iterate through the names of contents of the folder
for image_path in os.listdir(path):

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    output_path = os.path.join(outPath, image_path)
    image_to_use = imageio.imread(input_path)

    # check if image is light
    check_image = darkness_checker.check_image(image_to_use, 118)
    print(check_image + ", image: " + str(input_path))
    # create full output path, 'example.jpg' 
    # becomes 'rotate_example.jpg', save the file to disk
    if check_image == "light":
    	fullpath = os.path.join(outPath, image_path)
    	imageio.imwrite(output_path, image_to_use)
    else:
    	print("Dark image detected: " + input_path)

#if __name__ == '__main__':
#    main()
