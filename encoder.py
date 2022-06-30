import sys
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def Main():
    args = sys.argv
    print(args[1])
    print(args[2])
    img1 = Image.open(args[1])
    img2 = AutoImageCreate(args[1],args[2])
    img3 = img2

    print("import img success")
    img1.show()
    img1 = img1.convert('L')
    print("mono img success")
    img1.show()
    img1 = EvenImg(img1)
    print("even img success")
    img1.show()
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
    m, n = img.size
    for x in range(m):
        for y in range(n):
            print(img.getpixel((x,y)))
            if r % 2 == 1:
                r -= 1
                g -= 1
                b -= 1
                img.putpixel((x,y),(r,g,b))
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
            img3[x,y,0] = img1[x,y,0] + img2[x,y,0]
            img3[x,y,1] = img1[x,y,1] + img2[x,y,1]
            img3[x,y,2] = img1[x,y,2] + img2[x,y,2]
    return img3

def AutoImageCreate(image_path,text):
    # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "/usr/share/fonts/fonts-go/Go-Mono-Bold.ttf"
    fontsize = 36

    # 画像サイズ，背景色，フォントの色を設定
    img = Image.open(image_path)
    canvasSize = img.size
    backgroundRGB = (0, 0, 0)
    textRGB = (255, 255, 255)

    # 文字を描く画像の作成
    img = Image.new('RGB', canvasSize, backgroundRGB)
    draw = ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)
    textTopLeft = (canvasSize[0]//2-textWidth//2, canvasSize[1]//2-textHeight//2) 
    draw.text(textTopLeft, text, fill=textRGB, font=font)

    return img

if __name__ == "__main__":
    Main()

