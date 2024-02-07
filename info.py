import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

def fetch_destination_details(destination_name):
    # Replace these with your actual MySQL database connection details
    db_config = {
        'host': "localhost",
        'user': "root",
        'password': "shravani0212",
        'database': "login"
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Sample query to fetch details based on destination name
    query = f"SELECT * FROM destinations WHERE name = '{destination_name}'"
    cursor.execute(query)
    destination_details = cursor.fetchone()

    connection.close()
    print(destination_details)

    return destination_details

def display_destination(destination_name):
    # destination_label = tk.Label(new_window, text=f"Welcome to {destination.capitalize()}!", font=('Courier New', 23, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    # destination_label.pack(pady=20)
    # Fetch destination details from the database
    destination_details = fetch_destination_details(destination_name)

    if destination_details:
        # Create the main Tkinter window
        root = Tk()
        root.title(f"{destination_name} Details")

        # Set the window size to cover the full width of the desktop
        screen_width = root.winfo_screenwidth()
        root.geometry(f"{screen_width}x600")

       

        # Destination Details Frame
        details_frame = Frame(root, pady=20, bg="white", bd=5, relief=SOLID)
        details_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        title_label = Label(details_frame, text=destination_details[0], font=("Arial", 20, "bold"), fg="green", bg="white", anchor="w")
        title_label.pack()

        for label, value in zip(["Destination: ", "Famous For:", "Located At:", "Famous Food:", "Places to Visit:"], destination_details[1:]):
            detail_label = Label(details_frame, text=f"{label} {value}", font=("Helvetica", 14), fg="green", bg="white", anchor="w")
            detail_label.pack()

        # Run the Tkinter event loop
        root.mainloop()
    else:
        print(f"Details for {destination_name} not found in the database.")

# Call the display_destination function with a specific destination
# display_destination("Paris")