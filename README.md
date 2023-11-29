# Pixl8
A tool to turn an input image into a new pixelated version that fits your color palette. Great for video game asset creation

## Update Notes
Version 1.2 is complete. Now you can download the package and run Pixl8.exe on any machine.

## How to use GUI without python
Download the entire package, and then run Pixl8.exe. Pyinstaller handles all imports and even provides a python compiler. As a result, the file size is quite large, so it will take a few extra seconds to start up. If you move the exe it won't work cause the palettes in the provided folder are needed to run the functions internally. I am planning to change this but not sure how yet.

## How to use GUI with python
Simply run ```python tkgui.py```. Then you can choose an image to pixl8, choose from the provided palette, and click process image! The final screen shows your input image compared to the result. you can choose to save the resulting image anywhere.

## How to use terminal app
Run term.py --help to see list of options, then use whatever options you want. example usage:

```python term.py --input [path/to/file] --size 128```

## Product Backlog
  - input of custom palettes
  - web version
  - midjourney/stable diffusion integration
