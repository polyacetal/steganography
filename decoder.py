import sys
from PIL import Image
import numpy as np

def Main():
    args = sys.argv
    print(args[1])
    img1 = np.array(Image.open(args[1]))

    img1 = ModImg(img1)
    img_print = Image.fromarray(img1)
    print("modulo img success")
    img_print.show()
    img_print.save('appear_key.png')
    img1 = X255Img(img1)
    img_print = Image.fromarray(img1)
    print("x255 img success")
    img_print.show()
    img_print.save('appear_key.png')

def ModImg(img):
    m, n, nch = img.shape
    for x in range(m):
        for y in range(n):
            img[x,y,0] = img[x,y,0] % 2
            img[x,y,1] = img[x,y,1] % 2
            img[x,y,2] = img[x,y,2] % 2
    return img

def X255Img(img):
    m, n, nch = img.shape
    for x in range(m):
        for y in range(n):
            img[x,y,0] = img[x,y,0] * 255
            img[x,y,1] = img[x,y,1] * 255
            img[x,y,2] = img[x,y,2] * 255
    return img

if __name__ == "__main__":
    Main()

