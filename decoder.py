import sys
from PIL import Image

def Main():
    args = sys.argv
    print(args[1])
    img = Image.open(args[1]).convert("L")

    img = img.point(lambda x: x%2)
    print("modulo img success")
    img.save('appear_key.png')
    img = img.point(lambda x: x*255).convert("RGB")
    print("x255 img success")
    img.save('appear_key.png')


if __name__ == "__main__":
    Main()

