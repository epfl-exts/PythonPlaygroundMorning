# Image Manipulation
# Python program to convert iamge to grey scale

# import image module from Python Imaging Library (PIL)
from PIL import Image

# Open file and load image
image  = Image.open('OriginalImages/sunflowers.jpg')
pixels = image.load()

# Get width and height of image
width, height = image.size

# Loop over range of numbers: width and height of image
for x in range(width):
    for y in range(height):

        # Get the values of rgb for each pixel
        red, green, blue = image.getpixel((x, y))

        # Calculate the average for each pixel
        avg = (red + blue + green)/3

        # Set Pixel with grey value
        pixels[x, y] = (avg, avg, avg)

# Save new image in NewImages folder
image.save('NewImages/GreyImage.jpg')
