import tkinter as tk

def resize_window(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    window_width = max(frame.winfo_reqwidth(), 300)  # 300 is a minimum width
    window_height = max(frame.winfo_reqheight(), 300)  # 200 is a minimum height
    window.geometry("{}x{}".format(window_width, window_height))

window = tk.Tk()
window.title("Resizable Window")

canvas = tk.Canvas(window)
canvas.pack(side="top", fill="both", expand=True)

scrollbar = tk.Scrollbar(window, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Your widgets go here
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")
label = tk.Label(frame, text="Hello, World!")
label.pack(pady=10, side="left")

# Bind the resize function to the window resize event
window.bind("<Configure>", resize_window)

window.mainloop()
