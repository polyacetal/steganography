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
    img2 = AutoImageCreate(args[1], args[2])

    print("import img success")
    img1 = EvenImg(img1)
    print("even img success")
    img1 = MergeImg(img1,img2)
    print("merge img success")
    img1.save('hidden.png')

def EvenImg(img):
    r,g,b = img.split()
    b = b.point(lambda x: x-1 if x%2 == 1 else x)
    img = Image.merge("RGB",(r,g,b))
    return img

def MergeImg(img1,img2):
    width,height = img1.size
    img2data = img2.getdata()
    for h in range(height):
        hcache = h * width
        for w in range(width):
            if img2data[hcache+w] == 1:
                r,g,b = img1.getpixel((w,h))
                img1.putpixel((w,h),(r,g,b+1))
    return img1

def AutoImageCreate(image_path,text):
    # 使うフォント,サイズ,描くテキストの設定
    ttfontname = "/usr/share/fonts/fonts-go/Go-Mono-Bold.ttf"
    fontsize = 100

    # 画像サイズ,背景色,フォントの色を設定
    img = Image.open(image_path)
    canvasSize = img.size
    background = 0
    textColor = 1

    # 文字を描く画像の作成
    img = Image.new('L', canvasSize, background)
    draw = ImageDraw.Draw(img)

    # 用意した画像の文字列を描く
    font = ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)
    textTopLeft = (canvasSize[0]//2-textWidth//2, canvasSize[1]//2-textHeight//2)
    draw.text(textTopLeft, text, fill=textColor, font=font)
    return img

if __name__ == "__main__":
    Main()

