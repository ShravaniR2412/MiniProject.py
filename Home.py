from tkinter import Tk, Label, Frame, PhotoImage, Button

def open_link(link):
    # Replace this with your logic to open the link in a web browser
    print("Opening link:", link)

def navigate_to_home(label):
    label.config(text="Welcome to the Tourism Website - Home Page")

def navigate_to_destinations(label):
    label.config(text="Explore our Exciting Destinations!")

def navigate_to_contact(label):
    label.config(text="Contact Us for more information.")

class Footer:
    def __init__(self, root):
        self.root = root
        self.footer_frame = Frame(self.root, bg="#333")
        self.footer_frame.pack(side="bottom", fill="x", pady=2)

        # Contact Section
        contact_frame = Frame(self.footer_frame, bg="#333")
        contact_frame.pack(side="left", padx=20, pady=1)

        contact_label = Label(contact_frame, text="Contact Us", font=("Helvetica", 12), fg="white", bg="#333")
        contact_label.grid(row=0, column=0, columnspan=2, pady=1)

        email_label = Label(contact_frame, text="Email: info@mytravelagency.com", font=("Helvetica", 10), fg="white", bg="#333")
        email_label.grid(row=1, column=0, columnspan=2)

        phone_label = Label(contact_frame, text="Phone: 1-800-123-4567", font=("Helvetica", 10), fg="white", bg="#333")
        phone_label.grid(row=2, column=0, columnspan=2)

        # Social Media Section
        social_media_frame = Frame(self.footer_frame, bg="#333")
        social_media_frame.pack(side="right", padx=20, pady=1)

        follow_label = Label(social_media_frame, text="Follow Us", font=("Helvetica", 12), fg="white", bg="#333")
        follow_label.grid(row=0, column=0, columnspan=4, pady=1)

        # Social Media Icons
        placeholder_icon = PhotoImage(width=50, height=50)  # Placeholder image for testing

        facebook_button = Button(social_media_frame, image=placeholder_icon, bg="#333", command=lambda: open_link("#"))
        facebook_button.grid(row=1, column=0, padx=1)

        twitter_button = Button(social_media_frame, image=placeholder_icon, bg="#333", command=lambda: open_link("#"))
        twitter_button.grid(row=1, column=1, padx=1)

        instagram_button = Button(social_media_frame, image=placeholder_icon, bg="#333", command=lambda: open_link("#"))
        instagram_button.grid(row=1, column=2, padx=1)

class ImageSlider:
    def __init__(self, root):
        self.root = root

        self.banner_frame = Frame(root, bg="#333")
        self.banner_frame.pack(side="top", fill="both", expand=True)

        # List of image file paths
        self.image_paths = ["./images/nature.png", "./images/nature2.png", "./images/nature3.png"]
        self.current_image_index = 0

        # Create initial image label
        self.image_label = Label(self.banner_frame)
        self.image_label.pack(fill="both", expand=True)

        # Load and display the first image
        self.load_image()

        # Set up a timer to automatically change the image every few seconds
        self.root.after(3000, self.next_image)

    def load_image(self):
        # Load image from the current index
        image_path = self.image_paths[self.current_image_index]
        image = PhotoImage(file=image_path)
        self.image_label.configure(image=image)
        self.image_label.image = image

    def next_image(self):
        # Move to the next image in the list
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_image()

        # Set up the timer for the next image
        self.root.after(3000, self.next_image)

class ServiceSection:
    def __init__(self, root, title, image_path, description):
        self.root = root

        # Create Service Frame
        service_frame = Frame(self.root, bg="#fff")
        service_frame.pack(pady=10)

        # Service Image
        img = PhotoImage(file=image_path)
        image_label = Label(service_frame, image=img, bg="#fff")
        image_label.image = img
        image_label.grid(row=0, column=0, padx=10)

        # Service Details
        details_frame = Frame(service_frame, bg="#fff")
        details_frame.grid(row=0, column=1, padx=10)

        # Service Title
        title_label = Label(details_frame, text=title, font=("Helvetica", 14), bg="#fff")
        title_label.grid(row=0, column=0, pady=5, sticky="w")

        # Service Description
        description_label = Label(details_frame, text=description, font=("Helvetica", 12), bg="#fff", wraplength=400, justify="left")
        description_label.grid(row=1, column=0, pady=5, sticky="w")

class TourismWebsite:
    def __init__(self, root):
        self.root = root
        self.root.title("Tourism Website")
        self.root.geometry("800x600")

        # Navbar Frame
        navbar_frame = Frame(self.root, bg="#333")
        navbar_frame.pack(side="top", fill="x")

        # Label to display content
        self.label = Label(self.root, text="Welcome to the Tourism Website - Home Page", font=("Helvetica", 16), pady=20)
        self.label.pack()

        # Home Button
        home_button = Button(navbar_frame, text="Home", command=lambda: navigate_to_home(self.label), bg="#333", fg="white")
        home_button.pack(side="right", padx=10)

        # Destinations Button
        destinations_button = Button(navbar_frame, text="Destinations", command=lambda: navigate_to_destinations(self.label), bg="#333", fg="white")
        destinations_button.pack(side="right", padx=10)

        # Contact Button
        contact_button = Button(navbar_frame, text="Contact", command=lambda: navigate_to_contact(self.label), bg="#333", fg="white")
        contact_button.pack(side="right", padx=10)

        # Initialize Footer
        self.footer = Footer(self.root)

        # Initialize Image Slider
        self.image_slider = ImageSlider(self.root)

if __name__ == "__main__":
    root = Tk()
    tourism_website = TourismWebsite(root)
    root.mainloop()
