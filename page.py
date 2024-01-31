from tkinter import *

def on_home():
    # Functionality for the Home button
    print("Home button clicked")

def on_about_us():
    # Functionality for the About Us button
    print("About Us button clicked")

def on_learn_more():
    # Functionality for the Learn More button
    print("Learn More button clicked")

# Create the main Tkinter window
root = Tk()
root.title("My Tkinter Page")
root.geometry("800x600")


# Navigation Bar
navbar = Frame(root, bg="green",height=500)  # Use your desired background color
navbar.pack(side=TOP, fill=X)

Label(navbar, text="Navigation Bar", bg="green", fg="white").pack()

# Set a minimum size for the navbar
navbar.update_idletasks()  # Update the widget to get accurate size
navbar.config(width=navbar.winfo_reqwidth(), height=500)

home_button = Button(navbar, text="Home", command=on_home)
home_button.pack(side=LEFT, padx=10)

about_us_button = Button(navbar, text="About Us", command=on_about_us)
about_us_button.pack(side=LEFT, padx=10)

learn_more_button = Button(navbar, text="Learn More", command=on_learn_more)
learn_more_button.pack(side=LEFT, padx=10)

# Image
img_path = "login.png"  # Replace with the actual path to your image
img = PhotoImage(file=img_path)

image_label = Label(root, image=img)
image_label.pack()

# Run the Tkinter event loop
root.mainloop()
