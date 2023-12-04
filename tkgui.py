import tkinter as tk
from tkinter import filedialog
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
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
        tk.Button(welcome_frame, text="Next", command=self.show_next_screen).pack(pady=30, anchor="s")
        self.screens.append(welcome_frame)


        # Image selection screen
        image_frame = tk.Frame(master)

        # Left frame for image selection
        left_frame = tk.Frame(image_frame)
        tk.Label(left_frame, text="Select an image file:").pack(pady=10)
        tk.Button(left_frame, text="Browse", command=self.browse_image).pack(pady=10)
        self.selected_image_path = tk.StringVar()
        self.selected_image_path.set('./example images/knight.jpg')
        self.image_label = tk.Label(left_frame, textvariable=self.selected_image_path, wraplength=200)
        self.image_label.pack()
        #buttons frame
        image_screen_buttons_frame = tk.Frame(left_frame)
        tk.Button(image_screen_buttons_frame, text="Back", command=self.show_previous_screen).pack(padx=5, side='left')
        tk.Button(image_screen_buttons_frame, text="Next", command=self.show_next_screen).pack(padx=5, side='right')
        image_screen_buttons_frame.pack(pady=50)
        
        left_frame.pack(side="left", padx=20)

        # Right frame for image preview
        right_frame = tk.Frame(image_frame)
        self.preview_image_frame = tk.Label(right_frame, text='Image Preview', image=None)
        self.preview_image_frame.pack()
        right_frame.pack(side="right", padx=20)
        self.screens.append(image_frame)


        # Options screen
        options_frame = tk.Frame(master)
        tk.Label(options_frame, text="Options:").pack(pady=10)
        
        #palette options frame
        palette_frame = tk.Frame(options_frame)
        self.palette_var = tk.StringVar()
        self.palette_var.set('./palettes/dreamscape8-1x.png')
        self.example_palettes = ["./palettes/dreamscape8-1x.png", "./palettes/oil-6-1x.png", "./palettes/slso8-1x.png"]
        tk.Label(palette_frame, text="Choose a palette:").pack(side='left')
        tk.OptionMenu(palette_frame, self.palette_var, *self.example_palettes).pack(side="right")
        self.palette_var.trace('w', self.pal_update_dropdown)
        palette_frame.pack(pady=5)
        
        #palete preview frame
        palette_preview_frame = tk.Frame(options_frame)
        self.palette_preview = tk.Label(palette_preview_frame, text='Palette Preview', image=None)
        self.palette_preview.pack(side='left', padx=40)
        tk.Button(palette_preview_frame, text="Add a custom palette", command=self.browse_palette).pack(side="right")
        palette_preview_frame.pack(pady=5)

        #image size frame
        image_size_frame = tk.Frame(options_frame)
        self.size_var = tk.IntVar()
        self.size_var.set(32)
        self.size_options = [8, 16, 32, 64, 128, 256, 512]
        tk.Label(image_size_frame, text='Image Size:').pack(pady=10, side='left')
        tk.OptionMenu(image_size_frame, self.size_var, *self.size_options).pack(pady = 10, side='right')
        image_size_frame.pack(pady=5)
        
        #info frame
        info_frame = tk.Frame(options_frame)
        tk.Label(info_frame, justify="center", wraplength=300, text='Palettes should be a 1xN image with whatever colors you want. Inputing other images should not break the app, but will not work as intended.').pack()
        info_frame.pack()
        
        #buttons frame
        options_screen_buttons_frame = tk.Frame(options_frame)
        tk.Button(options_screen_buttons_frame, text="Process Image", command=self.process_image).pack(padx=5, side="right")
        tk.Button(options_screen_buttons_frame, text="Back", command=self.show_previous_screen).pack(padx=5, side='left')
        options_screen_buttons_frame.pack(pady=40, anchor='s')
        
        self.screens.append(options_frame)


        #final screen
        final_frame = tk.Frame(master)
        self.bigger_image = None
        self.proccessed_image = None
        
        # initial image frame
        init_image_frame = tk.Frame(final_frame)
        tk.Label(init_image_frame, text="Input Image:").pack(pady=10)
        self.init_image_label = tk.Label(init_image_frame, image=None)
        self.init_image_label.pack()
        init_image_frame.pack(side="left")
        
        #processed image frame
        processed_image_frame = tk.Frame(final_frame)
        tk.Label(processed_image_frame, text="Final Image:").pack(pady=10)
        self.bigger_image_label = tk.Label(processed_image_frame, image=None)
        self.bigger_image_label.pack()
        processed_image_frame.pack(side='right')
        
        #buttons frame
        final_buttons_frame = tk.Frame(final_frame)
        tk.Button(final_buttons_frame, text="Start Over", command=self.restart_program).pack(side='bottom', pady= 50)
        tk.Button(final_buttons_frame, text='Save Image (Actual Size)', command=self.save_final_image).pack(pady=5)
        tk.Button(final_buttons_frame, text='Save Image (Enlarged)', command=self.save_enlarged_image).pack(pady=5)
        final_buttons_frame.pack(padx=5, side='bottom')
        
        self.screens.append(final_frame)

        # Show the initial screen
        self.show_current_screen()

    def process_image(self):
        image_path = self.selected_image_path.get()
        palette = self.palette_var.get()
        w = self.size_var.get()
        if image_path:
            im = get_image(image_path)
            pal = get_image(palette)
            small = pixl8(im, w)
            palettized = palettizer(small, pal)
            fit = make_image_fit(palettized)
            self.proccessed_image = palettized
            self.bigger_image = fit
            self.resized = ImageTk.PhotoImage(fit)
            self.bigger_image_label.config(image=self.resized)
            self.bigger_image_label.image = self.resized
            og = ImageTk.PhotoImage(make_image_fit(im))
            self.init_image_label.config(image=og)
            self.init_image_label.image = og
            self.current_screen += 1
            self.show_current_screen()

    def save_final_image(self):
        initial_file_name = self.selected_image_path.get()
        default_output_file = make_rand_file_name(initial_file_name)
        fp = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=default_output_file)
        if not fp:
            return
        self.proccessed_image.save(fp)
        print(f'image saved to {fp}')

    def save_enlarged_image(self):
        initial_file_name = self.selected_image_path.get()
        default_output_file = 'BIG' + make_rand_file_name(initial_file_name)
        fp = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=default_output_file)
        if not fp:
            return
        self.bigger_image.save(fp)
        print(f'image saved to {fp}')

    def helper(self, filepath):
        print(filepath)
        self.selected_image_path.set(filepath)
        print(self.selected_image_path)
        self.make_preview_image()

    def make_preview_image(self):
        fp = self.selected_image_path.get()
        if fp:
            im = get_image(fp)
            resized = make_image_fit(im)
            prev_right = ImageTk.PhotoImage(resized)
            self.preview_image_frame.config(image=prev_right)
            self.preview_image_frame.image = prev_right

    def make_preview_palette(self):
        fp = self.palette_var.get()
        if fp:
            im = get_image(fp)
            resim = make_image_fit(im, 150)
            prev = ImageTk.PhotoImage(resim)
            self.palette_preview.config(image=prev)
            self.palette_preview.image = prev

    def restart_program(self):
        self.current_screen = 0
        self.show_current_screen()

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
            self.make_preview_image()

    def browse_palette(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.palette_var.set(file_path)
            self.make_preview_palette()
            
    def pal_update_dropdown(self, *args):
        self.make_preview_palette()


if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    root.geometry("600x400")
    wizard = SimpleWizard(root)
    root.mainloop()