import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from info import display_destination
import mysql.connector

content_label = None
search_entry = None

def explore_place(place_name):
    print(f"Exploring {place_name}")


city_recommendations = [
    ("assets/newyork.png", "New York City", "Experience the vibrant energy of the Big Apple."),
    ("assets/london.png", "London", "Discover the rich history and cultural diversity of London."),
    ("assets/tokyo.png", "Tokyo", "Immerse yourself in the futuristic cityscape of Tokyo."),
    ("assets/paris.png", "Paris", "Explore the romantic charm and iconic landmarks of Paris."),
    ("assets/dubai.png", "Dubai", "Indulge in luxury and innovation in the dynamic city of Dubai."),
    ("assets/singapore.png", "Singapore", "Enjoy the blend of tradition and modernity in Singapore.")
]
def fetch_destination_details(destination_name):
 
    db_config = {
        'host': "localhost",
        'user': "root",
        'password': "shravani0212",
        'database': "login"
     }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    query = f"SELECT * FROM destinations WHERE name = '{destination_name}'"
    cursor.execute(query)
    destination_details = cursor.fetchone()

    connection.close()

    return destination_details


# Main Tkinter window
root = tk.Tk()
root.title("City Recommendations")

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

welcome_label = tk.Label(root, text="WELCOME TO CITY EXPLORER", font=('Courier New', 30, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.pack(fill=tk.X,pady=10)



# Container for city cards
section_container = tk.Frame(root, bg="lightblue")  
section_container.pack(pady=20, fill="both")

for idx, city_info in enumerate(city_recommendations):
    if idx % 3 == 0:  
        row_frame = tk.Frame(section_container, bg="lightblue")
        row_frame.pack(fill="x")

    image_path, city_name, description = city_info
    card_frame = tk.Frame(row_frame, bg="white", bd=2, relief=tk.RAISED)
    card_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True)  

    city_label = tk.Label(card_frame, text=city_name, font=('Courier New', 10, 'bold'), bg="white")
    city_label.pack(pady=(0, 2))

    card_image = Image.open(image_path)
    card_image = card_image.resize((300, 100))  # Resize image as needed
    card_photo = ImageTk.PhotoImage(card_image)
    card_label = tk.Label(card_frame, image=card_photo, bg="white")
    card_label.image = card_photo
    card_label.pack(padx=5, pady=5)

    description_label = tk.Label(card_frame, text=description, font=('Courier New', 8), bg="white", wraplength=120)
    description_label.pack(pady=(0, 2))

    explore_button = ttk.Button(card_frame, text="Explore", command=lambda  city=city_name: display_destination(city), style="TButton" )
    explore_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

# Run the Tkinter event loop
root.mainloop()

