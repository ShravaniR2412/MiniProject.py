import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess




content_label=None
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
    image = Image.open(r".\assets\img1.png")  # Use raw string and backslashes
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


def open_search_window():
    # Execute the login.py script
    subprocess.run(["python", "search.py"])

    
def create_section_frame(image_path, section_name):
    section_frame = tk.Frame(section_container, bg="white")
    section_frame.pack(side=tk.LEFT, padx=15)  # Align sections horizontally

    # Load and display image for the section
    section_image = Image.open(image_path)
    section_image = section_image.resize((300, 200))  # Resize image as needed
    section_photo = ImageTk.PhotoImage(section_image)
    section_label = tk.Label(section_frame, image=section_photo, bg="white")
    section_label.image = section_photo
    section_label.pack(pady=10)

    # Add button for navigation
    if section_name == "Can't Decide here we are to help":
        nav_button = ttk.Button(section_frame, text=f"Go to {section_name}", command=open_search_window)
    else:
        nav_button = ttk.Button(section_frame, text=f"Go to {section_name}", command=lambda: navigate_to_section(section_name))

    nav_button.pack(pady=10)

def navigate_to_section(section_name):
    if section_name == "ABOUT":
        show_about()
    elif section_name == "BLOGS":
        show_blogs()
    elif section_name == "SERVICES":
        show_services()
    elif section_name == "CONTACT":
        show_contact()

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
about_label.bind("<Button-1>", lambda e: navigate_to_section("ABOUT"))

blogs_label = ttk.Label(navbar_frame, text="BLOGS", cursor="hand2", style="TLabel")
blogs_label.pack(side=tk.LEFT, padx=5)
blogs_label.bind("<Button-1>", lambda e: navigate_to_section("BLOGS"))

services_label = ttk.Label(navbar_frame, text="SERVICES", cursor="hand2", style="TLabel")
services_label.pack(side=tk.LEFT, padx=5)
services_label.bind("<Button-1>", lambda e: navigate_to_section("SERVICES"))

contact_label = ttk.Label(navbar_frame, text="CONTACT", cursor="hand2", style="TLabel")
contact_label.pack(side=tk.LEFT, padx=5)
contact_label.bind("<Button-1>", lambda e: navigate_to_section("CONTACT"))

# Container for sections
section_container = tk.Frame(root, bg="white")
section_container.pack(pady=20)

# Create frames for each section with images and navigation buttons
create_section_frame(r".\assets\hotel.png", "Hotel")
create_section_frame(r".\assets\think.png", "Can't Decide here we are to help")
create_section_frame(r".\assets\services.png", "SERVICES")
create_section_frame(r".\assets\contact.png", "CONTACT")




# Run the Tkinter event loop
root.mainloop()
