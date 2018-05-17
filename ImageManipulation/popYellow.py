# Image Manipulation
# Python program to highlight yellow by converting non-yellow pixels to grey scale

# import image module from Python Imaging Library (PIL)
from PIL import Image

# Open file and load image
image  = Image.open('OriginalImages/sunflowers.jpg')
pixels = image.load()

# Get width and height of image
width, height = image.size

# Vaiables to chenge and note effect
red_limit = 240
green_limit = 165

# Loop over all pixels
for x in range(width):
    for y in range(height):

        # Get the values of rgb for each pixel
        red, green, blue = image.getpixel((x, y))

        # If yellow set pixel as yellow
        if (red > red_limit and green > green_limit):
            pixels[x, y] = (red,green,blue)

        else:
            # Calculate the average for each pixel and convert to integer value
            avg = int((red + blue + green)/3)

            # Set Pixel with grey value
            pixels[x, y] = (avg, avg, avg)

# Save new image in NewImages folder as jpg
image.save('NewImages/popYellow.jpg')
