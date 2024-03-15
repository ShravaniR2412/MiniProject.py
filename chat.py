import tkinter as tk
from tkinter import ttk
import requests
import wikipedia
import webbrowser

class TravelChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Chatbot")
        self.root.geometry("400x600")
        self.root.configure(background='#016A70')

        self.user_preferences = {
            "name": ""
        }

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TEntry', font=('Comic Sans MS', 12))
        style.configure('TButton', font=('Comic Sans MS', 12), width=20)

        self.chat_history = tk.Text(self.root, width=40, height=20, wrap=tk.WORD, font=('Comic Sans MS', 12))
        self.chat_history.pack(padx=10, pady=10)

        self.user_input = ttk.Entry(self.root, width=50, font=('Comic Sans MS', 12))
        self.user_input.pack(padx=6, pady=4, side=tk.TOP, fill=tk.X)

        self.send_button = ttk.Button(self.root, text="Send", command=self.process_input, style='TButton')
        self.send_button.pack(pady=4, side=tk.BOTTOM)

        self.send_message("Hello Buddy! Ready to explore!", sent_message=True)

    def process_input(self):
        user_message = self.user_input.get()
        self.display_message(f"You: {user_message}", sent_message=True)

        response = self.generate_response(user_message)
        self.display_message(f"Chatbot: {response}", sent_message=False)

        self.user_input.delete(0, tk.END)  # Clear the user input

    def generate_response(self, user_message):
        # Check if user is providing their name
        if not self.user_preferences["name"]:
            self.user_preferences["name"] = user_message
            return f"Hi,Nice to meet you! How can I assist you further?"
        
        # Check if user is asking for the weather
        elif "weather" in user_message.lower():
            place = user_message.split("weather of ")[-1]
            return self.get_weather_response(place)

        # Check if user is asking for information about a place
        elif "about" in user_message.lower():
            place = user_message.split("about ")[-1]
            return self.get_place_info_response(place)

        # Check if user is asking for information about famous food
        elif "food" in user_message.lower():
            place = user_message.split("food of ")[-1]
            return self.get_food_info_response(place)

        # Check if user is asking for hotels in a location
        elif "hotels in" in user_message.lower():
            location = user_message.split("hotels in ")[-1]
            return self.get_hotel_info_response(location)

        else:
            return "I'm sorry, I didn't understand that. How else can I assist you?"

    def get_weather_response(self, place):
        api_key = "abe27cb6b54fc0eb319a531434dc2d05"
        url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={place}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"The weather in {place} is {weather} with a temperature of {temp}°C."
        else:
            return f"Sorry, I couldn't fetch weather information for {place}."

    def get_place_info_response(self, place):
        try:
            summary = wikipedia.summary(place, sentences=2)
            return f"Here's some information about {place}: {summary}"
        except wikipedia.exceptions.DisambiguationError:
            return f"Which {place} are you referring to? Please be more specific."
        except wikipedia.exceptions.PageError:
            return f"I couldn't find information about {place}."

    def get_food_info_response(self, place):
        try:
            food_info = wikipedia.summary(place + " cuisine", sentences=2)
            return f"Here's some information about famous {place}: {food_info}"
        except wikipedia.exceptions.DisambiguationError:
            return f"Which {place} are you referring to? Please be more specific."
        except wikipedia.exceptions.PageError:
            return f"I couldn't find information about the famous food of {place}."

    def get_hotel_info_response(self, location):
        google_search_url = f"https://www.google.com/search?q=hotels+in+{location}"
        webbrowser.open_new(google_search_url)
        return f"Here are some hotels in {location}. Opening search results in your browser..."

    def display_message(self, message, sent_message=False):
        self.chat_history.config(state=tk.NORMAL)
        if sent_message:
            self.chat_history.tag_configure('sent', foreground='black', background='white')
            self.chat_history.insert(tk.END, message + "\n", 'sent')
        else:
            self.chat_history.tag_configure('received', foreground='#016A70', background='white')
            self.chat_history.insert(tk.END, message + "\n", 'received')
        self.chat_history.config(state=tk.DISABLED)

    def send_message(self, message, sent_message=False):
        self.display_message(f"Chatbot: {message}", sent_message)

# Main Tkinter window
root = tk.Tk()
app = TravelChatbot(root)
root.mainloop()
