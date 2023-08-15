from PIL import Image, ImageFilter

import os, sys

img_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for images in os.listdir(img_folder):
    img = Image.open(f"./images/{images}")
    names = os.path.splitext(images)[0]
    print("NAMES", names) 
    img.save(f"./new/{names}.png", "png")