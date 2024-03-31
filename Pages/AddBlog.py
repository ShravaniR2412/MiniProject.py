import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import mysql.connector

# Connect to MySQL database
db_config = {
    'host': "localhost",
    'user': "root",
    'password': "shravani0212",
    'database': "login"
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        # print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        return None

def open_blog_window():
    subprocess.run(["python", "Pages/Blogs.py"])

# Insert a new blog post
def insert_blog_post(title, description, date, author):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Blogs (title, description, date, author) VALUES (%s, %s, %s, %s)"
            data = (title, description, date, author)
            cursor.execute(query, data)
            connection.commit()
            messagebox.showinfo("Blog added successfully!","Thank you for sharing youe experience")
            open_blog_window()
        except mysql.connector.Error as err:
            print(f"Error inserting blog post: {err}")
        finally:
            cursor.close()
            connection.close()


def submit_blog():
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END)
    date = date_entry.get()
    author = author_entry.get()

    insert_blog_post(title, description, date,author)


def set_bg_image():
    global photo  # Declare photo as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open(r"assets\nature.png")  # Use raw string and backslashes
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo
    
    


# Main Tkinter window
root = tk.Tk()
root.title("Add Blog")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

# Add a label at the top with the welcome message
welcome_label = tk.Label(bg_label, text="Add your own Travel blog", font=('Courier New', 20, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Label and entry for Title
title_label = tk.Label(root, text="Title:", font=('Courier New', 12), bg='#016A70', fg='white')
title_label.place(relx=0.3, rely=0.3, anchor=tk.CENTER)
title_entry = tk.Entry(root, font=('Courier New', 12))
title_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Label and entry for Description
description_label = tk.Label(root, text="Description:", font=('Courier New', 12), bg='#016A70', fg='white')
description_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
description_entry = tk.Text(root, font=('Courier New', 12), width=20, height=5)
description_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Label and entry for Date
date_label = tk.Label(root, text="Date:", font=('Courier New', 12), bg='#016A70', fg='white')
date_label.place(relx=0.3, rely=0.6, anchor=tk.CENTER)
date_entry = tk.Entry(root, font=('Courier New', 12))
date_entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Label and entry for Author
author_label = tk.Label(root, text="Author:", font=('Courier New', 12), bg='#016A70', fg='white')
author_label.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
author_entry = tk.Entry(root, font=('Courier New', 12))
author_entry.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Button to submit the blog
submit_button = ttk.Button(root, text="Submit", command=submit_blog)
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()