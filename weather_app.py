# import libraries
import requests
import tkinter as tk

# make function to request the weather information of a city
def get_weather(city_name):
    base_url = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=87bbf71e501894c887bb31ccf9700670&units=metric")
    response = requests.get(base_url)

    # make sure that the connection was successful
    if response.status_code != 200:
        error1 = (f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        error_label1.config(text=error1)
    
    # return the weather information of the city
    else:
        weather_data = response.json()
        return (weather_data['main']['temp'], 
                weather_data['main']['humidity'], 
                weather_data['main']['pressure'], 
                weather_data['wind']['speed'])

# make a search funcution to show weather inforamtion in gui
def search():
    # empty used labels
    temprature_label_result.config(text='')
    humidity_label_result.config(text='')
    wind_speed_label_result.config(text='')
    pressure_label_result.config(text='')
    precipitation_label_result.config(text='')

    error_label1.config(text='')
    error_label2.config(text='')
    
    # put user input in a variable
    city_name = search_entry.get()

    # make sure that user entered an input
    if not city_name:
        # show massage error if user didn't enter anythig
        error2 = "you should enter the city name"
        error_label2.config(text=error2)
    else:
        # make sure again that connection was successful
        try:
            # put user information in variables
            temprature, humidty, pressure, wind_speed= get_weather(city_name)
            precipitation = 20

            # adjust variables
            temprature_result = f"{temprature} C"
            humidity_result = f"{humidty} %"
            wind_speed_result = f"{wind_speed} Km/h"
            pressure_result = f"{pressure} hPa"
            precipitation_result = f"{precipitation} %"

            # show results in labels of gui
            temprature_label_result.config(text=temprature_result)
            humidity_label_result.config(text=humidity_result)
            wind_speed_label_result.config(text=wind_speed_result)
            pressure_label_result.config(text=pressure_result)
            precipitation_label_result.config(text=precipitation_result)

        except:
            # show massage error if the connection lost
            error2 = "Unable to display weather information."
            error_label2.config(text=error2)


# make a gui window
root = tk.Tk()
root.title("Weather forcast")
root.geometry("600x600")

# make search items
location_label = tk.Label(root, text="Location: ", padx=30)
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="search", command=search)

# make labels to show the name of weather information
temprature_label = tk.Label(root, text="temrapture:")
humidity_label = tk.Label(root, text="humidity:")
wind_speed_label = tk.Label(root, text="wind speed:")
pressure_label = tk.Label(root, text="pressure:")
precipitation_label = tk.Label(root, text="precipitation:")

# make labels to show weather inforamtion
temprature_label_result = tk.Label(root)
humidity_label_result = tk.Label(root)
wind_speed_label_result = tk.Label(root)
pressure_label_result = tk.Label(root)
precipitation_label_result = tk.Label(root)

# make labels to show errors
error_label1 = tk.Label(root)
error_label2 = tk.Label(root)


# put search items on screen
location_label.grid(column=0, row=0)
search_entry.grid(column=1, row=0)
search_button.grid(column=2, row=0)

# put names labeles on screen
temprature_label.grid(column=0, row=1)
humidity_label.grid(column=0, row=2)
wind_speed_label.grid(column=0, row=3)
pressure_label.grid(column=0, row=4)
precipitation_label.grid(column=0, row=5)

# put information labeles on screen
temprature_label_result.grid(column=1, row=1, sticky='w')
humidity_label_result.grid(column=1, row=2, sticky='w')
wind_speed_label_result.grid(column=1, row=3, sticky='w')
pressure_label_result.grid(column=1, row=4, sticky='w')
precipitation_label_result.grid(column=1, row=5, sticky='w')

# put errors labeles on screen
error_label1.grid(column=0, row=6, columnspan=3)
error_label2.grid(column=0, row=7, columnspan=3)

# run gui
root.mainloop()