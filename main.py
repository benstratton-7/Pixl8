from PIL import Image
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
        print(f"\nThe following Error has occured in input_file():\n{e}\n")

# takes an image and resolution, and returns a copy that is now the desired size
def pixl8(im, res = (64, 64)):
    # im_size = im.size
    small = im.resize(res, Image.NEAREST)
    # new_im = small.resize(im_size, Image.NEAREST)
    return small

# takes an image and palette and returns an image which has been re-colored so that it is within the palette
def palettizer(im, palette):
    palette_v = palette.convert("P")
    im_quantized = im.quantize(palette=palette_v)
    im_palettized = im_quantized.convert("RGB")
    return im_quantized



def main():
    sample_palette = get_image("./dreamscape8-1x.png")
    try:
        in_f_name = input_file()
        og_image = get_image(in_f_name)
        out_f_name = output_file_name()
        im1 = pixl8(og_image)
        im2 = palettizer(im1, sample_palette)
        save_image(im2, out_f_name, og_image.format)
        print(f"New image saved as {out_f_name}")
    except Exception as e:
        print(f"\nThe following error occured in main():\n{e}\n")

def tests1():
    test_palette = get_image("./dreamscape8-1x.png")
    test_image = get_image("./matt-damon-the-departed-2006-2K2285Y.jpg")
    im1 = pixl8(test_image)
    im2 = palettizer(im1, test_palette)
    im2.show()

main()

#trying to figure how to get the output image to look like the quantized image from palletizer but we need to convert it to RGB for some reason?