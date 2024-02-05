import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

def fetch_destination_details(destination_name):

    def __init__(self, root):
        self.root = root
    # Replace these with your actual MySQL database connection details
    db_config = {
        'host':"localhost",
        'user':"root",
        'password':"shravani0212",
        'database':"login"
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
    # Fetch destination details from the database
    destination_details = fetch_destination_details(destination_name)

    if destination_details:
        # Create the main Tkinter window
        root = Tk()
        root.title(f"{destination_name} Details")
        root.geometry("800x600")

        # # Destination Image
        # img_path = destination_details[-1]  # Replace with the actual path to your destination image
        # img = Image.open(img_path)
        # img = img.resize((550, 400))
        # img_tk = ImageTk.PhotoImage(img)

        # image_label = Label(root, image=img_tk)
        # image_label.photo = img_tk  # To prevent garbage collection
        # image_label.pack()

        # image_frame = Frame(root)
        # image_frame.pack(pady=20)

        # img_path = destination_details[-1]
        # original_image = PhotoImage(file=img_path)
        # resized_image = original_image.subsample(2)  # Subsample for resizing to 200x200 pixels

        # image_label = Label(image_frame, image=resized_image)
        # image_label.photo = resized_image  # To prevent garbage collection
        # image_label.pack(side=LEFT, padx=10)


        # Destination Details
        details_frame = Frame(root, pady=20)
        details_frame.pack()

        title_label = Label(details_frame, text=destination_details[0], font=("Helvetica", 16, "bold"))
        title_label.pack()

        for label, value in zip(["Destination: ", "Famous For:", "Located At:", "Famous Food:", "Places to Visit:"], destination_details[1:]):
            detail_label = Label(details_frame, text=f"{label} {value}", font=("Helvetica", 12))
            detail_label.pack()

        # Run the Tkinter event loop
        root.mainloop()
    else:
        print(f"Details for {destination_name} not found in the database.")
