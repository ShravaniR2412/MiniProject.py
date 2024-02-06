import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def show_about():
    content_label.config(text="This is the About page content.")

def show_blogs():
    content_label.config(text="Check out our latest blogs here.")

def show_services():
    content_label.config(text="Explore our services and offerings.")

def show_contact():
    content_label.config(text="Contact us for any inquiries or assistance.")

def set_bg_image():
    global photo  # Declare photo as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open(r"C:\Users\Admin\Desktop\bg.jpg")  # Replace with your image path
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

    # Add a label at the top with the welcome message
    welcome_label = tk.Label(bg_label, text="WELCOME TO TRAVEL-BUDDY", font=('Courier New', 35, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    welcome_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# Main Tkinter window
root = tk.Tk()
root.title("Simple Page with Navbar")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

# Navbar Frame with curved edges
navbar_frame = tk.Frame(bg_label, bg='#016A70', bd=5, relief=tk.GROOVE, borderwidth=2, pady=2)
navbar_frame.pack(side=tk.TOP, fill=tk.X)

# Navbar Labels with white text and light blue on hovering
style = ttk.Style()
style.configure("TLabel", font=('Courier New', 12, 'bold'), foreground='white', background='#016A70')
style.map("TLabel", background=[('active', '#5DADE2')])

about_label = ttk.Label(navbar_frame, text="ABOUT", cursor="hand2", style="TLabel")
about_label.pack(side=tk.LEFT, padx=5)
about_label.bind("<Button-1>", lambda e: show_about())

blogs_label = ttk.Label(navbar_frame, text="BLOGS", cursor="hand2", style="TLabel")
blogs_label.pack(side=tk.LEFT, padx=5)
blogs_label.bind("<Button-1>", lambda e: show_blogs())

services_label = ttk.Label(navbar_frame, text="SERVICES", cursor="hand2", style="TLabel")
services_label.pack(side=tk.LEFT, padx=5)
services_label.bind("<Button-1>", lambda e: show_services())

contact_label = ttk.Label(navbar_frame, text="CONTACT", cursor="hand2", style="TLabel")
contact_label.pack(side=tk.LEFT, padx=5)
contact_label.bind("<Button-1>", lambda e: show_contact())

# Run the Tkinter event loop
root.mainloop()
