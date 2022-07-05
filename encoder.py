import sys
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def Main():
    args = sys.argv
    print(args[1])
    print(args[2])
    img1 = Image.open(args[1]).convert('RGB')
    img2 = AutoImageCreate(args[1],args[2])
    img3 = img2

    print("import img success")
    img1.show()
    img1 = MonoImg(img1)
    print("mono img success")
    img1.show()
    img1 = EvenImg(img1)
    print("even img success")
    img1.show()
    img2 = OneImg(img2)
    print("one img success")
    img2.show()
    img3 = MergeImg(img1,img2)
    print("merge img success")
    img3.show()
    img3.save('hiden.png')

def MonoImg(img):
    m, n = img.size
    print(m,n)
    for x in range(m):
        for y in range(n):
            r, g, b = img.getpixel((x,y))
            gray = math.floor(r*0.299+g*0.587+b*0.114)
            img.putpixel((x,y),(gray,gray,gray))
    return img

def EvenImg(img):
    m, n = img.size
    for x in range(m):
        for y in range(n):
            r, g, b = img.getpixel((x,y))
            if r % 2 == 1:
                r -= 1
                g -= 1
                b -= 1
                img.putpixel((x,y),(r,g,b))
    return img

def OneImg(img):
    m, n = img.size
    for x in range(m):
        for y in range(n):
            r, g, b = img.getpixel((x,y))
            r = int(r / 255)
            g = int(g / 255)
            b = int(b / 255)
            img.putpixel((x,y),(r,g,b))
    return img

def MergeImg(img1,img2):
    img3 = img1
    m, n = img1.size
    for x in range(m):
        for y in range(n):
            r1, g1, b1 = img1.getpixel((x,y))
            r2, g2, b2 = img2.getpixel((x,y))
            r3 = r1 + r2
            g3 = g1 + g2
            b3 = b1 + b2
            img3.putpixel((x,y),(r3,g3,b3))
    return img3

def AutoImageCreate(image_path,text):
    # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "C:/Windows/Fonts/msgothic.ttc"
    fontsize = 100

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
