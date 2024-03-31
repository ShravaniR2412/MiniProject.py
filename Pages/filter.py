import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

# Global variable to store user preferences
user_preferences = {
    "category": "",
    "preference": "",
    "season": "",
    "duration": "",
    "budget": ""
}

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

# Function to set background image and display UI elements
def set_bg_image():
    global photo  # Declare photo as a global variable
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
    welcome_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Create labels for selected preferences
    global label  # Make label a global variable so it can be accessed outside this function
    label = ttk.Label(bg_label, text="", font=('Courier New', 16))
    label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # Add radio buttons to select the season
    season_frame = ttk.Frame(bg_label)
    season_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    season_label = ttk.Label(season_frame, text="Select Season:", font=('Courier New', 20, 'bold'), foreground='white', background='#016A70')
    season_label.grid(row=0, column=0, padx=10)

    # Create radio buttons for each season
    seasons = ["Summer", "Winter", "Monsoon"]
    for i, season in enumerate(seasons):
        radio_button = ttk.Radiobutton(season_frame, text=season, value=season, command=lambda season=season: select_season(season))
        radio_button.grid(row=i+1, column=0, padx=10, sticky=tk.W)

    # Add checkboxes for selecting preferences
    preferences_frame = ttk.Frame(bg_label)
    preferences_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    preferences_label = ttk.Label(preferences_frame, text="Select Preference:", font=('Courier New', 20, 'bold'), foreground='white', background='#016A70')
    preferences_label.grid(row=0, column=0, padx=10)

    # Create radio buttons for preferences
    preferences = ["Historical", "Adventurous", "Beaches", "Hill Stations", "Wildlife Sanctuaries"]
    for i, preference in enumerate(preferences):
        radio_button = ttk.Radiobutton(preferences_frame, text=preference, value=preference, command=lambda pref=preference: select_preference(pref))
        radio_button.grid(row=i+1, column=0, padx=10, sticky=tk.W)

    # Add radio buttons for selecting duration
    duration_frame = ttk.Frame(bg_label)
    duration_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    duration_label = ttk.Label(duration_frame, text="Select Duration:", font=('Courier New', 20, 'bold'), foreground='white', background='#016A70')
    duration_label.grid(row=0, column=0, padx=10)

    # Create radio buttons for duration
    durations = ["1-3 days", "4-7 days", "1-2 weeks", "2-4 weeks", "More than a month"]
    for i, duration in enumerate(durations):
        radio_button = ttk.Radiobutton(duration_frame, text=duration, value=duration, command=lambda dur=duration: select_duration(dur))
        radio_button.grid(row=1, column=i, padx=10, sticky=tk.W)

    # Add radio buttons for selecting budget
    budget_frame = ttk.Frame(bg_label)
    budget_frame.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    budget_label = ttk.Label(budget_frame, text="Select Budget:", font=('Courier New', 20, 'bold'), foreground='white', background='#016A70')
    budget_label.grid(row=0, column=0, padx=10)

    # Create radio buttons for budget
    budgets = ["Low", "Medium", "High"]
    for i, budget in enumerate(budgets):
        radio_button = ttk.Radiobutton(budget_frame, text=budget, value=budget, command=lambda bud=budget: select_budget(bud))
        radio_button.grid(row=1, column=i, padx=10, sticky=tk.W)

    # Add a button to filter options
    filter_button = ttk.Button(bg_label, text="Filter Options", command=filter_options)
    filter_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# Function to select season
def select_season(season):
    user_preferences["season"] = season
    show_preferences(label)

# Function to select preference
def select_preference(preference):
    user_preferences["preference"] = preference
    show_preferences(label)

# Function to select duration
def select_duration(duration):
    user_preferences["duration"] = duration
    show_preferences(label)

# Function to select budget
def select_budget(budget):
    user_preferences["budget"] = budget
    show_preferences(label)

# Function to show selected preferences
def show_preferences(label):
    selected_options = {}
    if user_preferences["category"]:
        selected_options["Category"] = user_preferences["category"].capitalize()
    if user_preferences["preference"]:
        selected_options["Preference"] = user_preferences["preference"].capitalize()
    if user_preferences["season"]:
        selected_options["Season"] = user_preferences["season"]
    if user_preferences["duration"]:
        selected_options["Duration"] = user_preferences["duration"]
    if user_preferences["budget"]:
        selected_options["Budget"] = user_preferences["budget"]
    label.config(text="Your selected preferences:\n" + "\n".join([f"{key}: {value}" for key, value in selected_options.items()]))

# Function to filter options
def filter_options():
    # Add your filter logic here
    pass

# Create the main application window
root = tk.Tk()
root.title("TRAVEL-BUDDY")
root.geometry("800x600")

# Create a label to display background image
bg_label = tk.Label(root)
bg_label.place(relwidth=1, relheight=1)

# Set background image and display UI elements
set_bg_image()

root.mainloop()
