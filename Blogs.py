import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

def fetch_blogs_from_database():
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shravani0212",
        database="login"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Blogs")
    blogs_data = cursor.fetchall()

    # Close the database connection
    connection.close()

    return blogs_data

def set_bg_image():
    global photo  # Declare photo as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open("assets/paris.png")  # Use raw string and backslashes
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 120)  # 150 is the alpha value for the background image (59% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

def next_blog():
    global current_index
    for widget in bg_label.winfo_children():
        if widget != next_button:
            widget.destroy()
    current_index = (current_index + 1) % len(blogs_data)
    display_blog(current_index)


def display_blog(index):
    global title_label, description_label, date_label, author_label

    title, description, date, author = blogs_data[index][1:]
    # title_label.config(text=title)
    # description_label.config(text=description)
    # date_label.config(text="Date: " + date)
    # author_label.config(text="Author: " + author)

    # Title Label
    title_label = tk.Label(bg_label, text=title, font=('Courier New', 18, 'bold'), fg='white',  bd=10, bg='#016A70')
    title_label.place(relx=0.5, rely=0.2 , anchor=tk.CENTER)

    # Description Frame
    description_frame = tk.Frame(bg_label, bd=5, relief=tk.GROOVE)  # Adding border to the frame
    description_frame.place(relx=0.5, rely=0.3 , anchor='n', relwidth=0.8, relheight=0.3)

    # Description Label
    description_label = tk.Label(description_frame, text=description, font=('Comic Sans MS', 12), fg='white', bg='#016A70', wraplength=800, justify='left')
    description_label.pack(fill='both', expand=True)

    date_label = tk.Frame(bg_label, bd=5, relief=tk.GROOVE)  # Adding border to the frame
    date_label = tk.Label(bg_label, text="Date: " + date , font=('Courier New', 12), fg='white', bg='#016A70')
    date_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # Author Label
    author_label = tk.Label(bg_label, text="Author: " + author , font=('Courier New', 12), fg='white', bg='#016A70')
    author_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Main Tkinter window
root = tk.Tk()
root.title("Blogs")

# Background Image
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

# Add a label at the top with the welcome message
welcome_label = tk.Label(bg_label, text="WELCOME TO Blog section", font=('Courier New', 20, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
welcome_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Fetch blogs from the database
blogs_data = fetch_blogs_from_database()

# Display the first blog initially
current_index = 0
display_blog(current_index)

# Next Button
style = ttk.Style()
style.configure("TButton", font=('Courier New', 15, 'bold'), foreground='#016A70', background='#016A70', borderwidth=5, relief="ridge")
style.map("TButton", background=[('active', '#9AD0C2')])

next_button = ttk.Button(bg_label, text="Next", style="TButton", command=next_blog)
next_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Add a border to all widgets
for widget in root.winfo_children():
    widget.config(bd=5, relief=tk.GROOVE)

root.mainloop()