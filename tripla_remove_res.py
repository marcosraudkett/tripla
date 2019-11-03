# this has the ability to remove images that don't have the right resolution
import imageio
import numpy as np
import os
import cv2
import check_resolution
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


outPath = "D:\TriplaScraper\images-FINAL"
path = "D:\TriplaScraper\images"

# iterate through the names of contents of the folder
for image_path in os.listdir(path):

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    output_path = os.path.join(outPath, image_path)
    image_to_use = imageio.imread(input_path)

    # check if image is light
    check_image = check_resolution.check_image(image_to_use)
    print(check_image + ", image: " + str(input_path))
    # create full output path, 'example.jpg' 
    # becomes 'rotate_example.jpg', save the file to disk
    if check_image == "right":
    	fullpath = os.path.join(outPath, image_path)
    	imageio.imwrite(output_path, image_to_use)

#if __name__ == '__main__':
#    main()