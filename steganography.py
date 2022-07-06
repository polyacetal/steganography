import readline
import os
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def Main():
    readline.parse_and_bind("tab: complete")
    mode = int(input("モードを選択してください 1:モノクロエンコード 2:カラーエンコード 3:デコード\n>"))
    if mode == 1:
        MonoEncode()
    elif mode == 2:
        ColorEncode()
    elif mode == 3:
        Decode()


def MonoEncode():
    imgFile = input("対象の画像ファイルのパスを入力してください(相対パス対応)\n>")
    text = input("隠したい文字を入力してください\n>")
    cwd = os.getcwd()
    imgFilePath = os.path.join(cwd,imgFile)
    img1 = Image.open(imgFilePath)
    img2 = AutoImageCreate(imgFilePath,text)

    print("import img success")
    img1 = img1.convert("L")
    print("mono img success")
    img1 = img1.point(lambda x: x-1 if x%2 == 1 else x)
    print("even img success")
    img = MonoMergeImg(img1,img2).convert("RGB")
    print("merge img success")
    
    saveName = input("保存するファイル名を決めてください (hidden.png)\n>")
    if not saveName:
        saveName = "hidden.png"
    saveFilePath = os.path.join(cwd,saveName)
    img.save(saveFilePath,format="png")


def MonoMergeImg(img1,img2):
    width,height = img1.size
    img2data = img2.getdata()
    for h in range(height):
        hcache = h * width
        for w in range(width):
            if img2data[hcache+w] == 1:
                pix = img1.getpixel((w,h))
                img1.putpixel((w,h),pix+1)

    return img1


def ColorEncode():
    imgFile = input("対象の画像ファイルのパスを入力してください(相対パス対応)\n>")
    text = input("隠したい文字を入力してください\n>")
    cwd = os.getcwd()
    imgFilePath = os.path.join(cwd,imgFile)
    img1 = Image.open(imgFilePath).convert("RGB")
    img2 = AutoImageCreate(imgFilePath,text)

    print("import img success")
    img1 = EvenImg(img1)
    print("even img success")
    img1 = ColorMergeImg(img1,img2)
    print("merge img success")
    img1.save('hidden.png')

def EvenImg(img):
    r,g,b = img.split()
    b = b.point(lambda x: x-1 if x%2 == 1 else x)
    img = Image.merge("RGB",(r,g,b))
    return img

def ColorMergeImg(img1,img2):
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
    imgFile = input("対象の画像ファイルを選択してください\n>")
    cwd = os.getcwd()
    imgFilePath = os.path.join(cwd,imgFile)
    img = Image.open(imgFilePath).split()[2]

    img = img.point(lambda x: x%2)
    print("modulo img success")
    img = img.point(lambda x: x*255).convert("L")
    print("x255 img success")
    img.show()
    saveFlag = input("ファイルを保存しますか？ y/n\n>")
    if saveFlag == "y" or saveFlag == "yes":
        saveName = input("保存するファイル名を決めてください (default:appear_key.png)\n>")
        if not saveName:
            saveName = "appear_key.png"
        saveFilePath = os.path.join(cwd,saveName)
        img.save(saveFilePath,format="png")


if __name__ == "__main__":
    Main()

