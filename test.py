import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageManipulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Manipulation App")

        # Variables
        self.image_path = tk.StringVar()
        self.preview_image = None

        # GUI elements
        self.create_widgets()

    def create_widgets(self):
        # File Browser Button
        file_button = tk.Button(self.root, text="Select Image", command=self.browse_image)
        file_button.pack(pady=10)

        # Preview Image Label
        self.preview_label = tk.Label(self.root, text="Preview Image")
        self.preview_label.pack(pady=10)

        # Next Steps Button (replace this with your next steps functionality)
        next_button = tk.Button(self.root, text="Next Steps", command=self.next_steps)
        next_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            self.image_path.set(file_path)
            self.update_preview_image()

    def update_preview_image(self):
        image_path = self.image_path.get()

        if image_path:
            image = Image.open(image_path)
            image = image.resize((200, 200))  # Adjust size as needed
            photo = ImageTk.PhotoImage(image)

            # Update the preview label
            self.preview_label.config(image=photo)
            self.preview_label.image = photo  # Keep a reference to avoid garbage collection issues

    def next_steps(self):
        # Add your logic for the next steps after image selection here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulationApp(root)
    root.mainloop()
