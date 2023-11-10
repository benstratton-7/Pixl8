import tkinter as tk
from tkinter import filedialog
from main import *

class SimpleWizard:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Wizard")

        self.current_screen = 0  # Index of the current screen
        self.screens = []  # List to hold screen frames

        # Welcome screen
        welcome_frame = tk.Frame(master)
        tk.Label(welcome_frame, text="Pixl8", font=('Helvetica', 24)).pack(pady=10)
        tk.Label(welcome_frame, wraplength=300, font=('Helvetica', 12), justify="center", text="This is an image manipulation tool made with python. Input any jpg or png image file, select your settings, and pixl8 will create a perfectly scaled and colored pixel art asset for you").pack(pady=30, padx=10)
        tk.Button(welcome_frame, text="Next", command=self.show_next_screen).pack(pady=30)
        self.screens.append(welcome_frame)

        # Image selection screen
        image_frame = tk.Frame(master)
        tk.Label(image_frame, text="Select an image file:").pack(pady=10)
        tk.Button(image_frame, text="Browse", command=self.browse_image).pack(pady=30)
        self.selected_image_path = tk.StringVar()
        self.image_label = tk.Label(image_frame, textvariable=self.selected_image_path)
        self.image_label.pack()
        # Dropdown for example images
        example_images = ["example1.jpg", "example2.png", "example3.gif"]
        example_dropdown = tk.OptionMenu(image_frame, self.selected_image_path, *example_images)
        example_dropdown.pack(pady=10)

        tk.Button(image_frame, text="Next", command=self.show_next_screen).pack(pady=10)
        tk.Button(image_frame, text="Back", command=self.show_previous_screen).pack(pady=10)
        self.screens.append(image_frame)
        
        # Image processing options screen
        options_frame = tk.Frame(master)
        tk.Label(options_frame, text="Options:").pack(pady=10)
        
        self.palette_var = tk.StringVar()
        example_palettes = ["Dreamscape8", "SLSO8", "Oil 6"]
        tk.Label(options_frame, text="Choose a palette:").pack()
        tk.OptionMenu(options_frame, self.palette_var, *example_palettes).pack()
        '''
        Need to figure out how to set the palette file as palette_var based on the name listed in the dropdown
        Displayed palette names are not and should not be the same as the file path
        '''

        tk.Button(options_frame, text="Process Image", command=self.process_image).pack()
        tk.Button(options_frame, text="Back", command=self.show_previous_screen).pack()
        self.screens.append(options_frame)
        
        #final screen
        final_frame = tk.Frame(master)
        tk.Label(final_frame, text="Final Image:").pack(pady=10)
        self.screens.append(final_frame)

        # Show the initial screen
        self.show_current_screen()

    def process_image(self):
        self.show_next_screen
        image_path = self.selected_image_path.get()
        scale = (32,32)
        palette = self.palette_var.get()
        if image_path:
            im = get_image(image_path)
            pal = get_image(palette)
            small = pixl8(im, scale)
            palettized = palettizer(small, pal)
            

    def show_current_screen(self):
        # Hide all screens
        for screen in self.screens:
            screen.pack_forget()

        # Show the current screen
        self.screens[self.current_screen].pack()

    def show_next_screen(self):
        # Move to the next screen
        if self.current_screen < len(self.screens) - 1:
            self.current_screen += 1
            self.show_current_screen()

    def show_previous_screen(self):
        # Move to the previous screen
        if self.current_screen > 0:
            self.current_screen -= 1
            self.show_current_screen()

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.selected_image_path.set(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    wizard = SimpleWizard(root)
    root.mainloop()

