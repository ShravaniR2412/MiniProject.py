import tkinter as tk
from tkinter import ttk
import requests

def get_weather(destination_name):
    # Create the main window
    top_level = tk.Toplevel()
    top_level.title("Weather App")

    # Style for widgets
    style = ttk.Style()
    style.configure("TFrame", background="#E1F5FE")
    style.configure("TLabel", background="#E1F5FE", foreground="black", font=("Arial", 20))
    style.configure("TButton", background="#016A70", foreground="black", font=("Arial", 12))

    # Create and place widgets
    main_frame = ttk.Frame(top_level, style="TFrame")
    main_frame.pack(side="top", fill="both", expand=True)

    # Add heading
    heading_label = ttk.Label(main_frame, text=f"The Weather of {destination_name} is", style="TLabel", font=("Arial", 16, "bold"), foreground="green")
    heading_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky=tk.W+tk.E)

    result_label = ttk.Label(main_frame, text="", style="TLabel")
    result_label.grid(row=2, column=0, columnspan=2, pady=20, padx=10, sticky=tk.W+tk.E)

    try:
        # Fetch data from API
        api_key = "abe27cb6b54fc0eb319a531434dc2d05"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={destination_name}&appid={api_key}"
        response = requests.get(api_url)
        data = response.json()

        # Extracting relevant weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        # Displaying the weather information
        result_label.config(text=f'Temperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%')

    except requests.exceptions.RequestException as e:
        result_label.config(text='Error fetching weather data')

    # Add a "Close" button to the window
    close_button = ttk.Button(main_frame, text="Close", command=top_level.destroy, style="TButton")
    close_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W+tk.E)

    # Run the Tkinter event loop
    top_level.mainloop()

# Call the get_weather function with a specific destination
# For example, get_weather("Paris")