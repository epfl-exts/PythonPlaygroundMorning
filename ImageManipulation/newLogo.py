# Image Manipulation
# Python program to merge two images

# Import image module from Python Imaging Library (PIL)
from PIL import Image

# Open file1 and load image
image  = Image.open('OriginalImages/EPFLlogo.jpg')
pixels = image.load()

# Open file2 and load bakground
background  = Image.open('OriginalImages/sunflowers.jpg')
pixelsBackground = image.load()

# Get width and height of image
width, height = image.size

# Loop over all pixels
for x in range(width):
    for y in range(height):

        # Get the values of rgb for each pixel in the image
        red, green, blue = image.getpixel((x, y))

        # Calculate the average for each pixel
        avg = (red + blue + green)/3

        # Check if red dominant
        if (red > avg):

            # Get the information about the same pixel in the background image
            redb, greenb, blueb = background.getpixel((x, y))

            # Set the image pixel with information from the background
            pixels[x, y] = (redb, greenb, blueb)

# Save new image in NewImages folder
image.save('NewImages/newLogo.jpg')
