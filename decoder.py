import sys
from PIL import Image

def Main():
    args = sys.argv
    print(args[1])
    img1 = Image.open(args[1])

    img1 = ModImg(img1)
    print("modulo img success")
    img1.show()
    img1.save('appear_key.png')
    img1 = X255Img(img1)
    print("x255 img success")
    img1.show()
    img1.save('appear_key.png')

def ModImg(img):
    m, n = img.size
    for x in range(m):
        for y in range(n):
            r, g, b = img.getpixel((x,y))
            r = r % 2
            g = g % 2
            b = b % 2
            img.putpixel((x,y),(r,g,b))
    return img

def X255Img(img):
    m, n = img.size
    for x in range(m):
        for y in range(n):
            r, g, b = img.getpixel((x,y))
            r = r * 255
            g = g * 255
            b = b * 255
            img.putpixel((x,y),(r,g,b))
    return img

if __name__ == "__main__":
    Main()

