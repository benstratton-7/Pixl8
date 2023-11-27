from main import *
import argparse
import os

def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Script with command-line arguments.')

    # Add arguments
    parser.add_argument('--input', default='./example images/matt-damon.jpg', help='Input file path. Type the full path to the file to use images other than the given examples. Only use JPG or PNG images for best results')
    parser.add_argument('--output', default='outputs', help="Output folder path. Type the full path to a desired output folder. If not specified, defaults to the 'outputs' folder in the pixl8 installation directory")
    parser.add_argument('--palette',default='./palettes/dreamscape8-1x.png', help='Choose a palette or input a path to a palette. Type the full path to an image of size Nx1. N represesnts the number of pixels to be used as a color reference in the palette')
    parser.add_argument('--size', type=int, default=64, help='Desired output size. Default is 64')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Ensure the output folder exists, create if not
    os.makedirs(args.output, exist_ok=True)

    input_path = args.input
    output_path = args.output
    input_palette = args.palette
    size_param = args.size
    
    # Run functions on the input
    palette = get_image(input_palette)
    og_image = get_image(input_path)
    resized = pixl8(og_image, size_param)
    recolored = palettizer(resized, palette)
    final_path = f'{output_path}/{make_rand_file_name(input_path)}.png'
    recolored.save(final_path)
    print(f"saved images to:", str(final_path))

if __name__ == "__main__":
    main()