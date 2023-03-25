#!/usr/bin/python3

import os
import click
import pytesseract
from PIL import Image
import magic


def save2txt(img: str, output: str):

    name = img.split("/")[-1].split(".")[0]

    with open(f"{output}/{name}.txt", "w") as i_text:
        text = pytesseract.image_to_string(Image.open(img))
        i_text.write(text)
    i_text.close()

    print(f"{name}.txt")


@click.command()
@click.option("-p", default=None, help="Path of images.")
@click.option(
    "-o",
    default=".",
    help="Output path where text file will be stored. \
Default set to current directory",
)
def image2txt(p: str, o: str):

    if not p:
        print(f"path, not defined, use: {__file__} --help")
        return False

    if not os.path.isdir(o):
        os.mkdir(o)

    if os.path.isdir(p):
        files = os.listdir(p)
        images = list()

        for f in files:
            img_path = f"{p}/{f}"
            if "image" in magic.from_file(img_path):
                images.append(img_path)

        del files
        images.sort()

        for img in images:
            save2txt(img, o)
        
        if len(images) > 1:
            print(f"Done, Analysed {len(images)} image files")
        else:
            print(f"Done")


    elif os.path.isfile(p):
        
        if "image" in magic.from_file(p):
            save2txt(p, o)
            print(f"Done")
        else:
            print(f"{p}, Not a valid image file")
            return False

    return True


if __name__ == "__main__":
    image2txt()
