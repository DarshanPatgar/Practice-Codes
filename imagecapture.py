# Python program to Convert Image into sketch


# import all the required modules
import time
import numpy as np
import imageio
import scipy.ndimage
import cv2
import pygame
import pygame.camera
pygame.camera.init()


cam_list = pygame.camera.list_cameras()

if cam_list:

	cam = pygame.camera.Camera(camlist[0], (640, 480))

	cam.start()
	time.sleep(2)
	image = cam.get_image()
	pygame.image.save(image, "filename.jpg")

else:
	print("No camera on current device")

# take image input and assign variable to it
img = "filename.jpg"


# function to convert image into sketch
def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
	return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def dodge(front, back):

	# if image is greater than 255 (which is not possible) it will convert it to 255
	final_sketch = front*255/(255-back)
	final_sketch[final_sketch > 255] = 255
	final_sketch[back == 255] = 255

	# to convert any suitable existing column to categorical type we will use aspect function
	# and uint8 is for 8-bit signed integer
	return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 230-gray


# to convert into a blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)


# calling the function
r = dodge(blur, gray)


cv2.imwrite('create.png', r)
