import math
from PIL import Image
import numpy as np
import sys

# opens the image file as a pil image object
def get_image(filename):
    """
    Opens the image file and returns it as a PIL Image object.
    Args:
        filename (str): The name of the input image file.
    Returns:
        PIL.Image.Image: The image object.
    """
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(filename)
        return image
    else:
        print("This is not a supported file type. Please use .png, .jpg, or .jpeg")

#save the image using PIL's save method NOTE: this is unneccesary and I wont be using it in the future
def save_image(image, new_name, filetype):
    """
    Saves the input image object to a file with the specified name and file type.
    Args:
        image (PIL.Image.Image): The image object to be saved.
        new_name (str): The name of the output image file.
        filetype (str): The file type for the output image (e.g., 'PNG', 'JPEG').
    """
    image.save(new_name, filetype)

# makes sure there is a valid output file to write to
def output_file_name():
    """
    Returns the output file name based on the command-line arguments or default value.
    Returns:
        str: The output file name.
    """
    try:
        return sys.argv[2]
    except IndexError:
        return "Pixl8ed_" + sys.argv[1]

# makes sure there was an argument passed for the filename
def input_file():
    """
    Returns the input file name based on the command-line arguments.
    Returns:
        str: The input file name.
    Raises:
        IndexError: If no input file is provided as a command-line argument.
    """
    try:
        return sys.argv[1]
    except Exception as e:
        print(f"\nno input file detected\n{e}\n")

# takes an image and resolution, and returns a copy of that image in the desired resolution
def pixl8(im, res = (32, 32)):
    """
    Resizes the input image to the specified resolution using nearest-neighbor interpolation.
    Args:
        im (PIL.Image.Image): The input image object.
        res (tuple): A tuple representing the desired resolution (width, height).
    Returns:
        PIL.Image.Image: The resized image object.
    """
    small = im.resize(res, Image.NEAREST)
    return small

# returns the euclidean distance between two rgb values
def euclidean_distance(c1,c2):
    """
    Calculates the Euclidean distance between two RGB color values.
    Args:
        c1 (tuple): The first RGB color value (r, g, b).
        c2 (tuple): The second RGB color value (r, g, b).
    Returns:
        float: The Euclidean distance between the two RGB colors.
    """
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

# takes a single rgb value, and a palette of colors as an array, and returns whatever color in the palette is closest to the input pixel
def nearest_color(pix, pal):
    """
    Finds the closest color in the palette to the input RGB pixel.
    Args:
        pix (tuple): The RGB pixel value to be matched (r, g, b).
        pal (list): A list of RGB color values representing the palette.
    Returns:
        tuple: The RGB color value from the palette that is closest to the input pixel.
    """
    #sets initial minimum distance to infinite, so there is a value to compare to that wil always be highest, and initial closest to 0,0,0
    min_distance = float('inf')
    closest = (0,0,0)
    for c in pal:
        # loops through each color in the palette and if its distance is closer than the previous color, updates the closest color to itself
        d = euclidean_distance(pix, c) 
        if d < min_distance:
            min_distance = d
            closest = c
    return closest

# takes an image and palette and returns a recolored image that is within the palette
def palettizer(im, p):
    """
    Recolors the input image using the provided palette.
    Args:
        im (PIL.Image.Image): The input image object.
        p (PIL.Image.Image): The palette image object.
    Returns:
        PIL.Image.Image: The recolored image object.
    """
    width, height = im.size
    # turns the input palette into the PIL 'palette' type object. idk if this is 100% necessary, but it works well this way
    p = p.convert("P")
    p1 = p.getpalette()
    #creates an array of rgb values representing the palette
    p2 = [p1[i:i + 3] for i in range(0, len(p1), 3)]
    #turns the input image into a flattened array of rgb values
    im_d = np.asarray(im.getdata())
    for x in range(len(im_d)):
        #replace each pixel in the input image with the closest color in the palette
        nearest = nearest_color(im_d[x], p2)
        im_d[x] = nearest
    #ensure that the image creates is in the correct format
    im_d_reshaped = im_d.reshape((height, width, 3))
    im_d_reshaped = np.clip(im_d_reshaped, 0, 255).astype('uint8')
    new_im = Image.fromarray(im_d_reshaped)
    return new_im

def main():
    sample_palette = get_image("./dreamscape8-1x.png")
    in_f_name = input_file()
    og_image = get_image(in_f_name)
    im1 = pixl8(og_image)
    im2 = palettizer(im1, sample_palette)
    im2.save(f'{output_file_name()}.png')
    print(f"saved images")