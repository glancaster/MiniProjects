# main.py
# python-mini-projects @Mitesh

import os
from PIL import Image
import sys

def watermark(imagepath,watermarkpath):
    image = Image.open(imagepath)
    watermark = Image.open(watermarkpath).convert("RGBA")

    position = image.size
    new_size = (int(position[0]*8/100),int(position[1]*8/100))
    watermark = watermark.resize(new_size)

    new_position = position[0]-new_size[0]-20,position[1]-new_size[1]-20
    transparent = Image.new(mode="RGBA", size=position, color = (0,0,0,0))
    transparent.paste(image,(0,0))

    transparent.paste(watermark,new_position,watermark)
    image_mode = image.mode

    if image_mode == "RGB":
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert("P")
    transparent.save("Watermarked"+imagepath, optimize = True, quality = 100)
    print(f"Created Watermarked{imagepath}....")


    print(position)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        watermark(*sys.argv[1:])
    else:
        print("Usage: python main.py {image file} {watermark file}")