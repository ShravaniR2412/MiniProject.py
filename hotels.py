import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import subprocess

# Function to fetch hotel data from MySQL database
def fetch_hotel_data(order_by):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shravani0212",
        database="login"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT hotel_name, description, rating, cost, image_path FROM hotel WHERE city_name = 'Mumbai' ORDER BY {order_by}")
    hotel_data = cursor.fetchall()
    conn.close()
    return hotel_data


def open_hotelcity_window():
    subprocess.run(["python", "hotelSearch.py"])

def explore_place(place_name):
    print(f"Exploring {place_name}")

# Main Tkinter window
root = tk.Tk()
root.title("Hotels")
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

welcome_label = tk.Label(root, text="SEARCH FOR HOTELS", font=('Courier New', 30, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.pack(fill=tk.X,pady=10)

# Buttons for sorting
button_frame = tk.Frame(root, bg='#016A70')
button_frame.pack(side=tk.TOP, fill=tk.X)

sort_label = ttk.Label(button_frame, text="Sort by", style="TLabel")
sort_label.pack(side=tk.LEFT, padx=10, pady=5)

def sort_by_price_low_to_high():
    hotel_data = fetch_hotel_data("cost")
    show_cards(hotel_data)

def sort_by_price_high_to_low():
    hotel_data = fetch_hotel_data("cost DESC")
    show_cards(hotel_data)

def sort_by_ratings():
    hotel_data = fetch_hotel_data("rating DESC")
    show_cards(hotel_data)

button_style = ttk.Style()
button_style.configure("Custom.TButton", width=20, background='#000000', foreground='#016A70')

button1 = ttk.Button(button_frame, text="Price - low to high", style="Custom.TButton", command=sort_by_price_low_to_high)
button1.pack(side=tk.LEFT, padx=10, pady=5)

button2 = ttk.Button(button_frame, text="Price - high to low", style="Custom.TButton", command=sort_by_price_high_to_low)
button2.pack(side=tk.LEFT, padx=10, pady=5)

button3 = ttk.Button(button_frame, text="Ratings", style="Custom.TButton", command=sort_by_ratings)
button3.pack(side=tk.LEFT, padx=10, pady=5)

button3 = ttk.Button(button_frame, text="City", style="Custom.TButton", command=open_hotelcity_window)
button3.pack(side=tk.LEFT, padx=40, pady=5)

section_container = tk.Frame(root, bg="lightblue")
section_container.pack(pady=20, fill="both")

cards_per_page = 3
current_page = 0

# Function to display hotel cards
def show_cards(hotel_data):
    start_index = current_page * cards_per_page
    end_index = min((current_page + 1) * cards_per_page, len(hotel_data))
    
    for widget in section_container.winfo_children():
        widget.destroy()
    
    for hotel_info in hotel_data[start_index:end_index]:
        card_frame = tk.Frame(section_container, bg="lightblue", bd=2, relief=tk.RAISED)
        card_frame.pack(fill="x", padx=10, pady=5)

        hotel_name, description, rating, price, image_path = hotel_info

        card_image = Image.open(image_path)
        card_image = card_image.resize((150, 100))  # Resize image as needed
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(card_frame, image=card_photo, bg="white")
        card_label.image = card_photo
        card_label.pack(side=tk.LEFT, padx=10, pady=10)

        name_description_frame = tk.Frame(card_frame, bg="white")
        name_description_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        hotel_label = tk.Label(name_description_frame, text=hotel_name, font=('Courier New', 13, 'bold'), bg="white")
        hotel_label.pack(pady=(0, 5), anchor=tk.W)

        description_label = tk.Label(name_description_frame, text=description, font=('Courier New', 9), bg="white", wraplength=500)
        description_label.pack(side=tk.LEFT, anchor=tk.W)

        rating_price_frame = tk.Frame(card_frame, bg="white")
        rating_price_frame.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X)

        rating_label = tk.Label(rating_price_frame, text=f"Rating: {rating}", font=('Courier New', 10), bg="white")
        rating_label.pack(anchor=tk.W)

        price_label = tk.Label(rating_price_frame, text=f"Price: Rs.{price} per night", font=('Courier New', 10), bg="white")
        price_label.pack(anchor=tk.W)

        explore_button = ttk.Button(card_frame, text="Explore", command=lambda hotel_name=hotel_name: explore_place(hotel_name))
        explore_button.pack(side=tk.RIGHT, padx=10, pady=5)


hotel_data = fetch_hotel_data("hotel_name")
show_cards(hotel_data)

# Function to handle next page button click
def next_page():
    global current_page
    current_page += 1
    show_cards(hotel_data)

# Function to handle back button click
def previous_page():
    global current_page
    current_page -= 1
    if current_page < 0:
        current_page = 0
    show_cards(hotel_data)

# Next button
next_button = ttk.Button(root, text="Next", command=next_page, style="Custom.TButton")
next_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Back button
back_button = ttk.Button(root, text="Back", command=previous_page, style="Custom.TButton")
back_button.pack(side=tk.RIGHT, padx=10, pady=10)



# Run the Tkinter event loop
root.mainloop()
