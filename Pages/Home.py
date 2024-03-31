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
    image = Image.open(r".\assets\nature.png")  # Use raw string and backslashes
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

    # Add a label at the top with the welcome message
    welcome_label = tk.Label(bg_label, text="WELCOME TO TRAVEL-BUDDY", font=('Courier New', 30, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    welcome_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    # Add Lorem Ipsum text at the right side of the page
    lorem_label = tk.Label(bg_label, text="Welcome to TRAVEL-BUDDY, your ultimate destination for unforgettable travel experiences. Whether you're seeking the serenity of pristine beaches, the adventure of rugged mountains, or the charm of bustling cities, we have the perfect journey waiting for you.", 
                            font=('Courier New', 13), fg='white', bg='#016A70', wraplength=400)
    lorem_label.place(relx=0.75, rely=0.4, anchor='n')

    # Add padding, border, and background color
    lorem_label.config(padx=10, pady=10, relief=tk.RAISED, bd=2)

def create_card(image_path, place_name, description,nxtpg):
    card_frame = tk.Frame(section_container, bg="white", bd=2, relief=tk.RAISED)
    card_frame.pack(side=tk.LEFT, padx=5, pady=5, fill="x", expand=True)  # Pack the card frames horizontally

    # Load and display image for the card
    card_image = Image.open(image_path)
    card_image = card_image.resize((150, 100))  # Resize image as needed
    card_photo = ImageTk.PhotoImage(card_image)
    card_label = tk.Label(card_frame, image=card_photo, bg="white")
    card_label.image = card_photo
    card_label.pack(padx=5, pady=5)

    # Add place name and description
    place_label = tk.Label(card_frame, text=place_name, font=('Courier New', 10, 'bold'), bg="white")
    place_label.pack(pady=(0, 2))

    description_label = tk.Label(card_frame, text=description, font=('Courier New', 8), bg="white", wraplength=120)
    description_label.pack(pady=(0, 2))

     # Add button
    button = tk.Button(card_frame, text="More Info", command=nxtpg)
    button.pack(pady=(0, 2))

def open_search_window():
    # Execute the login.py script
    subprocess.run(["python", "Pages/search.py"])

def open_beach_window():
    # Execute the login.py script
    subprocess.run(["python", "Pages/beach.py"])

def open_city_window():
    # Execute the login.py script
    subprocess.run(["python", "Pages/city.py"])

def open_history_window():
    # Execute the login.py script
    subprocess.run(["python", "Pages/history.py"])

def open_mountains_window():
    # Execute the login.py script
    subprocess.run(["python", "Pages/mountains.py"])

def create_section_frame(image_path, section_name, width=200, height=150, bg_color="white"):
    section_frame = tk.Frame(section_container, bg=bg_color, width=width, height=height)
    section_frame.pack(side=tk.LEFT, padx=5, pady=5, fill="x", expand=True)  

    # Load and display image for the section
    section_image = Image.open(image_path)
    section_image = section_image.resize((width - 20, height - 40))  # Resize image as needed
    section_photo = ImageTk.PhotoImage(section_image)
    section_label = tk.Label(section_frame, image=section_photo, bg=bg_color)
    section_label.image = section_photo
    section_label.pack(pady=5)

    # Add button for navigation
    nav_button = ttk.Button(section_frame, text=f"Go to {section_name}",  command=open_search_window)
    nav_button.pack(pady=2)

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
root.title("Home")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

# Navbar Frame with curved edges
navbar_frame = tk.Frame(bg_label, bg='#016A70', bd=5, relief=tk.GROOVE, borderwidth=2, pady=2)
navbar_frame.pack(side=tk.TOP, fill=tk.X)

# Navbar Labels with white text and light blue on hovering
style = ttk.Style()
style.configure("TLabel", font=('Courier New', 10, 'bold'), foreground='white', background='#016A70')
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
section_container = tk.Frame(root, bg="#016A70")  # Set the background color here
section_container.pack(pady=20, fill="both")

# Create cards above the services frame
create_card(r".\assets\nature.png", "Beach Paradise", "Relax and unwind at our breathtaking beach resort.", open_beach_window)
create_card(r".\assets\mountain.png", "Mountain Retreat", "Escape to the mountains for an adventure-filled getaway.", open_mountains_window)
create_card(r".\assets\city.png", "City Exploration", "Experience the vibrant culture and nightlife of bustling cities.", open_city_window)
create_card(r".\assets\history.png", "Historical Sites", "Explore ancient ruins and historical landmarks.", open_history_window)

# Create frames for each section with images and navigation buttons
create_section_frame(r".\assets\hotel.png", "HOTELS")
create_section_frame(r".\assets\think.png", "CAN'T DECIDE WHERE TO GO?")

# Run the Tkinter event loop
root.mainloop()
