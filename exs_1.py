from PIL import Image
import numpy as np

# Load the image using PIL
image_PIL = Image.open("sample1.bmp")

image_PIL_np = np.array(image_PIL)

print(f'Shape of the image is {image_PIL_np.shape}')
