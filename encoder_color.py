import sys
import math
from PIL import Image
import numpy as np

def Main():
    args = sys.argv
    print(args[1])
    print(args[2])
    img1 = np.array(Image.open(args[1]))
    img2 = np.array(Image.open(args[2]))
    img3 = img2

    img_print = Image.fromarray(img1)
    print("import img success")
    img_print.show()
    img1 = EvenImg(img1)
    img_print = Image.fromarray(img1)
    print("even img success")
    img_print.show()
    img2 = OneImg(img2)
    img_print = Image.fromarray(img2)
    print("one img success")
    img_print.show()
    img3 = MergeImg(img1,img2)
    img_print = Image.fromarray(img3)
    print("merge img success")
    img_print.show()
    img_print.save('hiden.png')

def EvenImg(img):
    m, n, nch = img.shape
    for x in range(m):
        for y in range(n):
            if img[x,y,2] % 2 == 1:
                img[x,y,2] = img[x,y,2] - 1
    return img

def OneImg(img):
    m, n, nch = img.shape
    for x in range(m):
        for y in range(n):
            img[x,y,0] = img[x,y,0] / 255
            img[x,y,1] = img[x,y,1] / 255
            img[x,y,2] = img[x,y,2] / 255
    return img

def MergeImg(img1,img2):
    img3 = img1
    m, n, nch = img1.shape
    for x in range(m):
        for y in range(n):
            img3[x,y,2] = img1[x,y,2] + img2[x,y,2]
    return img3

if __name__ == "__main__":
    Main()

