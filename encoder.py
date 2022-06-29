import sys
from PIL import Image
import numpy as np

def Main():
    args = sys.argv
    print(args[1])
    img = Image.open(args[1])

    width, height = img.size

    img2 = Image.new('RGB', (width, height))

    img_pixels = Init_image(img, width, height)

    for y in range(height):
        for x in range(width):
            img2.putpixel((x, y), (255, 0, 255))
    img2.show()

def Init_image(img, width, height):
    img_pixels = []
    for y in range(height):
        for x in range(width):
            img_pixels.append(img.getpixel((x,y)))
    img_pixels = np.array(img_pixels)
    return(img_pixels)

def Mono():
    a = 1

if __name__ == "__main__":
    Main()

