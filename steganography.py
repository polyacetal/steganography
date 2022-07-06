import readline
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def Main():
    readline.parse_and_bind("")
    mode = input("どのモードにしますか 1:エンコード 2:デコード\n>")
    mode = 
    if mode == 1:
        Encode()
    elif mode == 2:
        Decode()


def Encode():
    img1 = Image.open(args[1])
    img2 = AutoImageCreate(args[1],args[2])

    print("import img success")
    img1.show()
    img1 = img1.convert("L")
    print("mono img success")
    img1.show()
    img1 = img1.point(lambda x: x-1 if x%2 == 1 else x)
    print("even img success")
    img1.show()
    img1 = MergeImg(img1,img2).convert("RGB")
    print("merge img success")
    img1.show()
    img1.save('hiden.png')


def MergeImg(img1,img2):
    width,height = img1.size
    img2data = img2.getdata()
    for h in range(height):
        hcache = h * width
        for w in range(width):
            if img2data[hcache+w] == 1:
                pix = img1.getpixel((w,h))
                img1.putpixel((w,h),pix+1)

    return img1


def AutoImageCreate(image_path,text):
    # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "/usr/share/fonts/fonts-go/Go-Mono-Bold.ttf"
    fontsize = 100

    # 画像サイズ，背景色，フォントの色を設定
    img = Image.open(image_path)
    canvasSize = img.size
    background = 0
    textColor = 1

    # 文字を描く画像の作成
    img = Image.new('L', canvasSize, background)
    draw = ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)
    textTopLeft = (canvasSize[0]//2-textWidth//2, canvasSize[1]//2-textHeight//2) 
    draw.text(textTopLeft, text, fill=textColor, font=font)

    return img

def Decode():
    img = Image.open(args[1]).convert("L")

    img = img.point(lambda x: x%2)
    print("modulo img success")
    img.show()
    img.save('appear_key.png')
    img = img.point(lambda x: x*255).convert("RGB")
    print("x255 img success")
    img.show()
    img.save('appear_key.png')


if __name__ == "__main__":
    Main()

