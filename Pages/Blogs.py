import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def set_bg_image():
    global photo  # Declare photo as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open(r".\assets\nature.png")  # Use raw string and backslashes
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

# Main Tkinter window
root = tk.Tk()
root.title("Blogs")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

 # Add a label at the top with the welcome message
welcome_label = tk.Label(bg_label, text="WELCOME TO Blog section", font=('Courier New', 20, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

root.mainloop()
