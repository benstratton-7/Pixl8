# This was my first attempt at this project, using PIL(pillow) but I didnt like how rigid pillow was when trying to edit individual pixels, and also pillowds docs werent the best so it made it tough to understand what was going on.
import math
from PIL import Image
import numpy as np
import sys

# opens the image file as a pil image object
def get_image(filename):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(filename)
        return image
    else:
        print("This is not a supported file type. Please use .png, .jpg, or .jpeg")


def save_image(image, new_name, filetype):
    image.save(new_name, filetype)
    pass

# makes sure there is a valid output file to write to
def output_file_name():
    try:
        return sys.argv[2]
    except IndexError:
        return "Pixl8ed_" + sys.argv[1]

# makes sure there was an argument passed for the filename
def input_file():
    try:
        return sys.argv[1]
    except Exception as e:
        print(f"\nno input file detected\n{e}\n")

# takes an image and resolution, and returns a copy that is now the desired size
def pixl8(im, res = (32, 32)):
    small = im.resize(res, Image.NEAREST)
    return small

def euclidean_distance(c1,c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)
    

def nearest_color(pix, pal):
    min_distance = float('inf')
    closest = (0,0,0)
    for c in pal:
        d = euclidean_distance(pix, c) 
        if d < min_distance:
            min_distance = d
            closest = c
    return closest

# takes an image and palette and returns a recolored image that is within the palette
def palettizer(im, p):
    width, height = im.size
    p = p.convert("P")
    p1 = p.getpalette()
    #creates an array of rgb values representing the palette
    p2 = [p1[i:i + 3] for i in range(0, len(p1), 3)]
    #turns the input image into a flattened array of rgb values
    im_d = np.asarray(im.getdata())
    print('beginning:\n',im_d)
    for pix in im_d:
        #replaces each pixel with the  nearest palette color
        pix = nearest_color(pix, p2)
        #UNFINISHED: I think I need to make sure I am altering the array in place, because everything is running smoothly but the output image is not palettized. Check the update in place functionality of this loop!
    print('afterloop:\n', im_d)
    new_im = Image.fromarray(np.reshape(im_d, (height, width, 3)).astype('uint8'))
    print('final:\n', new_im)
    return new_im

def main():
    sample_palette = get_image("./dreamscape8-1x.png")
    in_f_name = input_file()
    og_image = get_image(in_f_name)
    out_f_name = output_file_name()
    im1 = pixl8(og_image)
    im2 = palettizer(im1, sample_palette)
    im2.save(out_f_name)
    print(f"New image saved as {out_f_name}")


main()