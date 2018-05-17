# Image Manipulation
# Python program to convert red pixels to blue

# Import image module from Python Imaging Library (PIL)
from PIL import Image

# Open file and load image
image  = Image.open('OriginalImages/EPFLlogo.jpg')
pixels = image.load()

# Get width and height of image
width, height = image.size

# Loop over range of numbers: width and height of image
for x in range(width):
    for y in range(height):

        # Get the values of rgb for each pixel
        red, green, blue = image.getpixel((x, y))

        # Check if red dominant
        if (red > blue and red > green):
            # Set pixel color values
            pixels[x, y] = (0, 0, 255)

# Save new image in NewImages folder
image.save('NewImages/BlueLogo.jpg')
