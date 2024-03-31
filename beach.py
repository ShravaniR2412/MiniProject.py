import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from info import display_destination

def explore_place(beach_name):
    print(f"Exploring {beach_name}")


beach_recommendations = [
    ("assets/maldives.png", "Maldives Beach", "Relax on the iconic beaches of Maldives."),
    ("assets/waikki.png", "Waikiki Beach", "Enjoy the sun and surf at the world-famous Waikiki Beach in Honolulu, Hawaii."),
    ("assets/bondi.png", "Bondi Beach", "Experience the vibrant atmosphere of Bondi Beach in Sydney, Australia."),
    ("assets/cancun.png", "Cancun Beach", "Explore the beautiful beaches of Cancun, Mexico."),
    ("assets/myrtle.png", "Myrtle Beach", "Discover the stunning coastline of Myrtle Beach, South Carolina."),
    ("assets/phuket.png", "Phuket Beaches", "Relax on the pristine beaches of Phuket, Thailand.")
]

# Main Tkinter window
root = tk.Tk()
root.title("Beach Recommendations")

# Background color
root.configure(bg="lightblue")

# Navbar Frame with curved edges
navbar_frame = tk.Frame(root, bg='#016A70', bd=5, relief=tk.GROOVE, borderwidth=2, pady=2)
navbar_frame.pack(side=tk.TOP, fill=tk.X)

# Navbar Labels with white text and light blue on hovering
style = ttk.Style()
style.configure("TLabel", font=('Courier New', 10, 'bold'), foreground='white', background='#016A70')
style.map("TLabel", background=[('active', '#5DADE2')])

about_label = ttk.Label(navbar_frame, text="ABOUT", cursor="hand2", style="TLabel")
about_label.pack(side=tk.LEFT, padx=5)

blogs_label = ttk.Label(navbar_frame, text="BLOGS", cursor="hand2", style="TLabel")
blogs_label.pack(side=tk.LEFT, padx=5)

services_label = ttk.Label(navbar_frame, text="SERVICES", cursor="hand2", style="TLabel")
services_label.pack(side=tk.LEFT, padx=5)

contact_label = ttk.Label(navbar_frame, text="CONTACT", cursor="hand2", style="TLabel")
contact_label.pack(side=tk.LEFT, padx=5)

welcome_label = tk.Label(root, text="WELCOME TO TRAVEL-BUDDY", font=('Courier New', 30, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.pack(fill=tk.X,pady=10)

# Container for beach cards
section_container = tk.Frame(root, bg="lightblue")  
section_container.pack(pady=20, fill="both")


for idx, beach_info in enumerate(beach_recommendations):
    if idx % 3 == 0:  
        row_frame = tk.Frame(section_container, bg="lightblue")
        row_frame.pack(fill="x")

    image_path, beach_name, description = beach_info
    card_frame = tk.Frame(row_frame, bg="white", bd=2, relief=tk.RAISED)
    card_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True)  

    
    beach_label = tk.Label(card_frame, text=beach_name, font=('Courier New', 10, 'bold'), bg="white")
    beach_label.pack(pady=(0, 2))

    
    card_image = Image.open(image_path)
    card_image = card_image.resize((300, 100))  # Resize image as needed
    card_photo = ImageTk.PhotoImage(card_image)
    card_label = tk.Label(card_frame, image=card_photo, bg="white")
    card_label.image = card_photo
    card_label.pack(padx=5, pady=5)

   
    description_label = tk.Label(card_frame, text=description, font=('Courier New', 8), bg="white", wraplength=120)
    description_label.pack(pady=(0, 2))

    
    explore_button = ttk.Button(card_frame, text="Explore", command=lambda  beach=beach_name: display_destination(beach), style="TButton")
    explore_button.pack(pady=5)

# Add a label at the top with the welcome message


# Run the Tkinter event loop
root.mainloop()
