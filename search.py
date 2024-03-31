import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from info import display_destination
import mysql.connector

content_label = None

# List of destinations
# destinations = [
#     "Paris","Matheran","new york", "tokyo", "rome", "barcelona","Kyoto",
#     "sydney", "london", "dubai", "rio de janeiro", "cape town",
#     "singapore", "kyoto", "amsterdam", "vancouver", "prague",
#     "bali", "edinburgh", "istanbul", "san francisco", "rajasthan"
# ]

def show_about():
    content_label.config(text="This is the About page content.")

def show_blogs():
    content_label.config(text="Check out our latest blogs here.")

def show_services():
    content_label.config(text="Explore our services and offerings.")

def show_contact():
    content_label.config(text="Contact us for any inquiries or assistance.")

def open_destination_page(destination):
    new_window = tk.Toplevel(root)
    new_window.title(destination.capitalize())
    
    
    #BY REMOVING THE COMMENTS OF BELOW TWO LINES THE NEW PAGE WILL OPEN HE SIZE OF DESKTOP WITH NEED TO BE MAXIMIZED
    # Set the size of the new window to match the desktop size
    # Set the size of the new window to match the desktop size
    new_window.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
  
    
    # Load background image for the destination
    bg_image_path = f"C:/Users/Admin/Desktop/Destination Images/{destination}.jpg"  # Replace with your image path
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    
    # Add opacity to the background image
    alpha = Image.new('L', bg_image.size, 99)  # 99 is the alpha value (30% opacity)
    bg_image.putalpha(alpha)
    
    photo = ImageTk.PhotoImage(bg_image)
    
    # Set background image for the new window
    bg_label = tk.Label(new_window, image=photo)
    bg_label.image = photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add content_label
    content_label = tk.Label(bg_label, text="", font=('Courier New', 18), wraplength=800, justify="left", fg='black', bg='#9AD0C2', bd=10, relief=tk.GROOVE)
    content_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    
    destination_label = tk.Label(new_window, text=f"Welcome to {destination.capitalize()}!", font=('Courier New', 23, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    destination_label.pack(pady=20)
    
    # Add more details about the destination here if needed


def fetch_destination_details(destination_name):
    # db_config = {
    #     'host': "localhost",
    #     'user': "root",
    #     'password': "Mahvish#04",
    #     'database': "travel_buddy"
    # }

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


def search_destination():
    query = search_entry.get("1.0", "end-1c").strip()  # Get the text from the Text widget and remove leading/trailing spaces
    if query:  # Check if the query is not empty
        destination_details = fetch_destination_details(query)
        if destination_details:
            display_destination(query)
        else:
            content_label.config(text=f"Destination '{query}' not found in the database.")
    else:
        content_label.config(text="Please enter a destination.")


def set_bg_image():
    global photo  # Declare photo as a global variable
    global destinations  # Declare destinations as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open(r"bg.jpg")  # Replace with your image path
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

    # Add a label at the top with the welcome message
    welcome_label = tk.Label(bg_label, text="TRAVEL-BUDDY: Your seamless travel companion", font=('Courier New', 23, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    welcome_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # Add a search box below the welcome message
    search_label = tk.Label(bg_label, text="Search your dream destination:", font=('Courier New', 20, 'bold'), fg='white', bg='#016A70', bd=11, relief=tk.GROOVE)
    search_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    # Add a text box for the search with curved edges and border
    search_style = ttk.Style()
    search_style.configure("TEntry", font=('Courier New', 15), borderwidth=9, relief="curve", foreground='black')
    global search_entry  # Make search_entry global
    search_entry = tk.Text(bg_label, font=('Courier New', 15), wrap=tk.WORD, height=1.4, bd=5, relief=tk.GROOVE)  # Increased height, added border and relief
    search_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER, width=500)  # Increased width

    # Add a search button
    search_button = ttk.Button(bg_label, text="SEARCH", command=lambda: search_destination() , style="TButton" )
    search_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Main Tkinter window
root = tk.Tk()
root.title("Search")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

# Navbar Frame with curved edges
navbar_frame = tk.Frame(bg_label, bg='#016A70', bd=5, relief=tk.GROOVE, borderwidth=2, pady=2)
navbar_frame.pack(side=tk.TOP, fill=tk.X)

# Navbar Labels with white text and light blue on hovering
style = ttk.Style()
style.configure("TLabel", font=('Courier New', 15, 'bold'), foreground='white', background='#016A70')
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



# Style for the search button
style.configure("TButton", font=('Courier New', 15, 'bold'), foreground='#016A70', background='#016A70', borderwidth=5, relief="ridge")
style.map("TButton", background=[('active', '#9AD0C2')])

# Run the Tkinter event loop
root.mainloop()