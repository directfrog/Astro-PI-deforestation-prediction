import sys, os, math
import numpy as np
import PIL
from PIL import Image
from scipy.stats import pearsonr

def get_pixels(image_filename):
	arr = []
	image = Image.open(image_filename)
	image = image.convert("RGB")

	width, height = image.size

	for x in range(width):
		for y in range(height):
			pixel = image.getpixel((x, y))
			arr.append(pixel)
	return arr


temperature = get_pixels('temperature.png')
vegetation_density = get_pixels('vegetation density.png')

for pixel in temperature:
	if pixel == (0, 0, 0):
		if vegetation_density[vegetation_density.index(pixel)] == 0:
			temperature.pop(temperature.index(pixel))
			vegetaion_density.pop(vegetation_density.index(pixel))

print(len(temperature), len(vegetation_density))

corr = pearsonr(temperature, vegetation_density)
print(corr)