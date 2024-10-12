# Import necessary libraries
import numpy as np
import imageio
from skimage import io
from matplotlib import pyplot as plt

# 1) Using imread method in imageio
image_imageio = imageio.imread('sample1.bmp')
print("Channel sequence using imageio.imread:", image_imageio.shape)

# 2) Using imread method in skimage.io
image_skimage = io.imread('sample1.bmp')  # Replace with your image path
print("Channel sequence using skimage.io.imread:", image_skimage.shape)

# 3) Converting skimage image to numpy array (to check channel sequence)
image_skimage_np = np.array(image_skimage)
print("Channel sequence after converting to numpy array:", image_skimage_np.shape)

# 4) Creating an image using numpy
# Create a blank image of size 100x100 pixels, with 3 color channels (RGB)
image = np.zeros((100, 100, 3), dtype=np.uint8)

# Divide the image into 4 quadrants and fill with different colors

# Top-left quadrant (red)
image[0:50, 0:50] = [255, 0, 0]  # Red

# Top-right quadrant (green)
image[0:50, 50:100] = [0, 255, 0]  # Green

# Bottom-left quadrant (blue)
image[50:100, 0:50] = [0, 0, 255]  # Blue

# Bottom-right quadrant (yellow)
image[50:100, 50:100] = [255, 255, 0]  # Yellow

# Save the created image using imageio
imageio.imwrite('created_image.png', image)

# Display the created image using matplotlib
plt.imshow(image)
plt.title("Created Image")
plt.show()
