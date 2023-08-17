import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def resize_image():
    source_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if source_path:
        try:
            scale_percent = int(scale_entry.get())
            src = cv2.imread(source_path, cv2.IMREAD_UNCHANGED)

            new_width = int(src.shape[1] * scale_percent / 100)
            new_height = int(src.shape[0] * scale_percent / 100)

            output = cv2.resize(src, (new_width, new_height))

            destination_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("Image files", "*.jpg")])
            if destination_path:
                cv2.imwrite(destination_path, output)
                result_label.config(text="Image resized and saved successfully!")
                result_label.pack()
        except ValueError:
            result_label.config(text="Invalid input! Please enter a valid scale value.")
            result_label.pack()

# Create the main application window
root = tk.Tk()
root.title("Image Resizer")

# Create widgets
file_button = tk.Button(root, text="Select Image", command=resize_image)
file_button.pack(pady=10)

scale_label = tk.Label(root, text="Enter the scale (in percentage):")
scale_label.pack()

scale_entry = tk.Entry(root)
scale_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
