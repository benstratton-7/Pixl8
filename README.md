# Pixl8
A tool to turn an input image into a new pixelated version that fits your color palette. Great for video game asset creation

## Update Notes
Version 1.1 is complete. I got a working gui up and running so you can just run tkgui.py, and go through the wizard to see how it works. It should work fine for any jpg or png images.

## How to use gui
Run tkgui.py, choose an image to pixl8, choose from the provided palettes(have to add the ability to upload your own palette later), and click process image! the final screen shows two versiond of your image. One is actual size, and the other is blown up so you can see it better.

## How to use terminal app
Run term.py --help to see list of options, then use whatever options you want. example usage:

```python term.py --input [path/to/file] --size 128```

## Product Backlog
  - input of custom palettes
  - package so everyone can run it even if you dont have python installed
  - web version
  - midjourney/stable diffusion integration
