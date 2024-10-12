# Import necessary libraries
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

# Open the image using PIL and convert it to a numpy array
image_PIL = Image.open("sample1.bmp")
image_PIL_np = np.array(image_PIL)

# 1. Display image using matplotlib (assumes RGB format)
plt.imshow(image_PIL_np)
plt.title("Image displayed with Matplotlib (RGB format)")
plt.show()

# 2. Display image using cv2 (OpenCV assumes BGR format)
cv2.imshow('Image displayed with OpenCV (BGR format)', image_PIL_np)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

# Optional: Convert from RGB to BGR before showing with cv2 to correct color issue
image_PIL_bgr = cv2.cvtColor(image_PIL_np, cv2.COLOR_RGB2BGR)
cv2.imshow('Corrected Image with OpenCV (after RGB to BGR conversion)', image_PIL_bgr)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
