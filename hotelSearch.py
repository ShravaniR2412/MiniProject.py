import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

# Function to fetch hotel data from MySQL database for a specific city
def fetch_hotel_data(city_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shravani0212",
        database="login"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT property_name, hotel_facilities, hotel_rating, property_type FROM hotelsIndia WHERE city = '{city_name}'")
    hotel_data = cursor.fetchall()
    conn.close()
    return hotel_data

def fetch_hotel_details(hotel_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shravani02",
        database="login"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM hotelsIndia WHERE property_name = '{hotel_name}'")
    hotel_details = cursor.fetchone()
    conn.close()
    return hotel_details

def explore_place(place_name):
    hotel_details = fetch_hotel_details(place_name)
    display_hotel_details(hotel_details)

def display_hotel_details(hotel_details):
    detail_window = tk.Toplevel()
    detail_window.title("Hotel Details")

    # Create labels to display hotel details
    labels = [
        "Property Name:",
        "Hotel Facilities:",
        "Hotel Rating:",
        "Property Type:",
        "Room Type:",
        "Point of Interest:",
        "Address:"
    ]

    for i, label_text in enumerate(labels):
        label = ttk.Label(detail_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

        if label_text == "Property Name:":
            data_label = ttk.Label(detail_window, text=hotel_details[3])
        elif label_text == "Hotel Facilities:":
            data_label = ttk.Label(detail_window, text=hotel_details[2], wraplength=450)
        elif label_text == "Hotel Rating:":
            data_label = ttk.Label(detail_window, text=hotel_details[6])
        elif label_text == "Property Type:":
            data_label = ttk.Label(detail_window, text=hotel_details[4])
        elif label_text == "Room Type:":
            data_label = ttk.Label(detail_window, text=hotel_details[5])
        elif label_text == "Point of Interest:":
            data_label = ttk.Label(detail_window, text=hotel_details[7], wraplength=450)
        elif label_text == "Address:":
            data_label = ttk.Label(detail_window, text=hotel_details[8])

        data_label.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

# Main Tkinter window
root = tk.Tk()
root.title("Hotels")
root.configure(bg="lightblue")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

def show_cards(hotel_data):
    start_index = current_page * cards_per_page
    end_index = min((current_page + 1) * cards_per_page, len(hotel_data))
    
    for widget in section_container.winfo_children():
        widget.destroy()
    
    for i, hotel_info in enumerate(hotel_data[start_index:end_index], start=start_index):
        property_name, hotel_facilities, hotel_rating, property_type = hotel_info

        card_frame = tk.Frame(section_container, bg="lightblue", bd=2, relief=tk.RAISED, width=1400)
        card_frame.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

        # Load and display image
        image_path = "assets/img.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((150, 100))  # Resize image as needed
        card_photo = ImageTk.PhotoImage(card_image)
        card_label = tk.Label(card_frame, image=card_photo, bg="white")
        card_label.image = card_photo
        card_label.grid(row=0, column=0, padx=10, pady=10, rowspan=4)

        hotel_label = ttk.Label(card_frame, text=property_name)
        hotel_label.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        clipped_facilities = hotel_facilities[:200] + '...' if len(hotel_facilities) > 200 else hotel_facilities
        facilities_label = ttk.Label(card_frame, text=clipped_facilities, wraplength=950)
        facilities_label.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        rating_label = ttk.Label(card_frame, text=f"Rating: {hotel_rating}")
        rating_label.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        type_label = ttk.Label(card_frame, text=f"Type: {property_type}")
        type_label.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        explore_button = ttk.Button(card_frame, text="Details", command=lambda name=property_name: explore_place(name))
        explore_button.grid(row=0, column=2, rowspan=4, padx=10, pady=5, sticky=tk.W+tk.E)




# Function to update hotel data based on the city name entered
def update_hotels():
    global hotel_data
    city_name = city_entry.get()
    hotel_data = fetch_hotel_data(city_name)
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

# City input Frame
city_input_frame = tk.Frame(root, bg="lightblue")
city_input_frame.pack(fill=tk.X)

city_label = tk.Label(city_input_frame, text="Enter city name:", font=('Courier New', 12), bg="lightblue")
city_label.pack(side=tk.LEFT, padx=10, pady=5)

city_entry = tk.Entry(city_input_frame, font=('Courier New', 12))
city_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Update button
update_button = ttk.Button(city_input_frame, text="Search", command=update_hotels)
update_button.pack(side=tk.LEFT, padx=5, pady=5)

# Section container
section_container = tk.Frame(root, bg="lightblue")
section_container.pack(pady=20, fill="both")

# Global variables
hotel_data = []
current_page = 0
cards_per_page = 3

# Fetch initial hotel data and display cards
update_hotels()

# Run the Tkinter event loop
root.mainloop()
