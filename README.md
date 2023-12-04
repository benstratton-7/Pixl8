# Pixl8
A tool to turn an input image into a new pixelated version that fits your color palette. Great for video game asset creation
![Untitled design(1)](https://github.com/benstratton-7/Pixl8/assets/109835020/bb46896a-b8c5-400a-b8cb-08b226846690)

## Update Notes
Version 1.2.3:

  -Now supports more image types
    -can hangle png images and most image types that include alpha values.
    -fixed bug on creating file names, and simplified the process

P.S. You might need to expand the window on certain frames to fit all the options and buttons on the screen.

## How to use GUI with python
Simply run ```python tkgui.py``` and ensure you have all the dependencies installed. Then you can choose an image to pixl8, choose from the provided palette, and click process image! The final screen shows your input image compared to the result. you can choose to save the resulting image anywhere.

## How to use terminal app
Run term.py --help to see list of options, then use whatever options you want. example usage:

```python term.py --input [path/to/file] --size 128```

## Product Backlog
  - input of custom palettes
  - resize the window to fit content automatically
