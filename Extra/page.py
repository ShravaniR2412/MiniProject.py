from tkinter import *
from info import display_destination


def on_home():
    print("Home button clicked")

def on_about_us():
    print("About Us button clicked")

def on_learn_more(image_number, destination_name):
    print(f"Learn More button clicked for image {image_number}")
    display_destination(destination_name)  # Call the function from info.py

# Create the main Tkinter window
root = Tk()
root.title("My Tkinter Page")
root.geometry("800x600")

# Navigation Bar
navbar = Frame(root, bg="green", height=50)
navbar.pack(side=TOP, fill=X)

Label(navbar, text="Navigation Bar", bg="green", fg="white").pack()

home_button = Button(navbar, text="Home", command=on_home)
home_button.pack(side=LEFT, padx=10)

about_us_button = Button(navbar, text="About Us", command=on_about_us)
about_us_button.pack(side=LEFT, padx=10)

# Image Frame
image_frame = Frame(root)
image_frame.pack(pady=20)

# Images and Buttons
image_paths = ["assets/img1.png", "login.png", "login.png"]  # Replace with actual image paths
destinations=['Matheran','Paris','Kyoto']

for index, img_path in enumerate(image_paths):
    original_image = PhotoImage(file=img_path)
    resized_image = original_image.subsample(3)  # Subsample for resizing to 200x200 pixels

    image_label = Label(image_frame, image=resized_image)
    image_label.photo = resized_image  # To prevent garbage collection
    image_label.pack(side=LEFT, padx=10)

    label_below_image = Label(image_frame, text=destinations[index])
    label_below_image.pack(side=LEFT, padx=10)

    # Use a lambda function to pass the destination_name to on_learn_more
    button_below_image = Button(image_frame, text="Know more", command=lambda dest_name=destinations[index]: on_learn_more(index + 1, dest_name))
    button_below_image.pack(side=LEFT, padx=10)


    # button_below_image = Button(image_frame, text="Know more", command=lambda index=index: on_learn_more(index+1))
    # button_below_image.pack(side=LEFT, padx=10)

# Run the Tkinter event loop
root.mainloop()

