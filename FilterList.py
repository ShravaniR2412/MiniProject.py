import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import sys

filtered_destinations = eval(sys.argv[1])

# Global variable to store user preferences
# user_preferences = {
#     "category": "",
#     "preference": "",
#     "season": "",
#     "duration": "",
#     "budget": ""
# }

db_config = {
        'host': "localhost",
        'user': "root",
        'password': "shravani0212",
        'database': "login"
    }

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        return None
    
def filter_options(user_preferences):
    connection = connect_to_database()
    filtered_destinations = []  # Initialize a list to store filtered destinations
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM TravelPreferences WHERE "
            conditions = []
            for key, value in user_preferences.items():
                if value:
                    # Map keys to corresponding column names
                    column_name = ""
                    if key == "preference":
                        column_name = "Category"
                    elif key == "season":
                        column_name = "Season"
                    elif key == "duration":
                        column_name = "Duration"
                    elif key == "budget":
                        column_name = "BudgetType"
                    conditions.append(f"{column_name} = '{value}'")
            if conditions:
                query += " AND ".join(conditions)
                cursor.execute(query)
                filtered_destinations = cursor.fetchall()  # Get the filtered destinations
            else:
                print("No preferences selected.")
            cursor.close()
            connection.close()
            
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
    else:
        print("Could not establish connection to the database.")
    
    return filtered_destinations

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
welcome_label = tk.Label(bg_label, text="Here are your recommendations", font=('Courier New', 20, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Add destinations
initial_y_position = 0.2  # Initial y position for the first label
y_offset = 0.1  # Offset to adjust the y position for each subsequent label (increased for more space)

for idx, destination in enumerate(filtered_destinations):
    destination_name = destination[0]
    lorem_label = tk.Label(bg_label, text=destination_name, font=('Courier New', 13), fg='white', bg='#016A70', wraplength=400)
    # Calculate y position for each label
    label_y_position = initial_y_position + idx * y_offset
    lorem_label.place(relx=0.5, rely=label_y_position, anchor='n')

root.mainloop()
