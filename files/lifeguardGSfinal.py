import PIL
import matplotlib.pyplot as plt
import os.path   
from PIL import ImageFilter           

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
gray_file = os.path.join(directory, 'lifeguardGS2.jpg')

# Open and show the grayscale background image in a new Figure window
gray_img = PIL.Image.open(gray_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(gray_img, interpolation='none')

# Open, and display lifeguard
shane_file = os.path.join(directory, 'shane2.png')
shane_img = PIL.Image.open(shane_file)
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(shane_img)

# takes the background image and applies a filter to blur it
blurred_image = gray_img.filter(ImageFilter.UnsharpMask(radius=20, percent=400, threshold=4))

# Paste lifeguard onto background and display
# Uses alpha from mask
blurred_image.paste(shane_img, (250, 260), mask=shane_img) 

# Display
fig3, axes3 = plt.subplots(1, 1)
axes3.imshow(blurred_image, interpolation='none')
fig3.show()