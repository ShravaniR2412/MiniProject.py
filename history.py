import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from info import display_destination

def explore_place(place_name):
    print(f"Exploring {place_name}")


historical_recommendations = [
    ("assets/colosseum.png", "Colosseum", "Visit the ancient amphitheater in Rome, Italy."),
    ("assets/machupicchu.png", "Machu Picchu", "Explore the ancient Incan citadel nestled in the Andes."),
    ("assets/pyramid.png", "Pyramids of Giza", "Marvel at the iconic pyramids in Egypt."),
    ("assets/acropolisathens.png", "Acropolis of Athens", "Discover the architectural wonders of ancient Greece."),
    ("assets/angkorwat.png", "Angkor Wat", "Explore the largest religious monument in the world in Cambodia."),
    ("assets/tajmahal.png", "Taj Mahal", "Admire the grandeur of the marble mausoleum in India.")
]

# Main Tkinter window
root = tk.Tk()
root.title("Historical Site Recommendations")

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

welcome_label = tk.Label(root, text="WELCOME TO HISTORICAL SITE EXPLORER", font=('Courier New', 30, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.pack(fill=tk.X,pady=10)

# Container for historical site cards
section_container = tk.Frame(root, bg="lightblue")  
section_container.pack(pady=20, fill="both")


for idx, site_info in enumerate(historical_recommendations):
    if idx % 3 == 0:  
        row_frame = tk.Frame(section_container, bg="lightblue")
        row_frame.pack(fill="x")

    image_path, site_name, description = site_info
    card_frame = tk.Frame(row_frame, bg="white", bd=2, relief=tk.RAISED)
    card_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True)  

    site_label = tk.Label(card_frame, text=site_name, font=('Courier New', 10, 'bold'), bg="white")
    site_label.pack(pady=(0, 2))

    card_image = Image.open(image_path)
    card_image = card_image.resize((300, 100))  # Resize image as needed
    card_photo = ImageTk.PhotoImage(card_image)
    card_label = tk.Label(card_frame, image=card_photo, bg="white")
    card_label.image = card_photo
    card_label.pack(padx=5, pady=5)

    description_label = tk.Label(card_frame, text=description, font=('Courier New', 8), bg="white", wraplength=120)
    description_label.pack(pady=(0, 2))

    explore_button = ttk.Button(card_frame, text="Explore", command=lambda  site=site_name: display_destination(site), style="TButton" )
    explore_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
