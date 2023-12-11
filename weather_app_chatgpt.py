import tkinter as tk
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change the unit to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            update_labels(data)
            error_label.config(text="")
        else:
            error_label.config(text=f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        error_label.config(text=f"Connection Error: {e}")

def update_labels(data):
    temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
    humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
    wind_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")
    pressure_label.config(text=f"Pressure: {data['main']['pressure']} hPa")

def search_weather():
    city = city_entry.get()
    if city:
        get_weather(api_key, city)
    else:
        error_label.config(text="Please enter a city name.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# API Key
api_key = '87bbf71e501894c887bb31ccf9700670'

# Create and set up the GUI components
city_label = tk.Label(root, text="City:")
city_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_weather)

temp_label = tk.Label(root, text="Temperature:")
humidity_label = tk.Label(root, text="Humidity:")
wind_label = tk.Label(root, text="Wind Speed:")
pressure_label = tk.Label(root, text="Pressure:")
error_label = tk.Label(root, text="", fg="red")

# Arrange the components in the grid
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry.grid(row=0, column=1, padx=10, pady=10)
search_button.grid(row=0, column=2, padx=10, pady=10)
temp_label.grid(row=1, column=0, padx=10, pady=10)
humidity_label.grid(row=2, column=0, padx=10, pady=10)
wind_label.grid(row=3, column=0, padx=10, pady=10)
pressure_label.grid(row=4, column=0, padx=10, pady=10)
error_label.grid(row=5, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
root.mainloop()
