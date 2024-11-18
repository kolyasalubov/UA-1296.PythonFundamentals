import tkinter as tk
from tkinter import font
from tkinter import ttk
import module.api_weather as api


HEIGHT = 350
WIDTH = 450


def get_emoji_for_weather(status):
    if "clear" in status:
        return "☀️"
    elif "cloud" in status:
        return "☁️"
    elif "rain" in status:
        return "🌧️"
    elif "snow" in status:
        return "❄️"
    else:
        return "🌫️"


def format_weather_info(weather_info):
    temperature = weather_info["temperature"]
    status = weather_info["status"].lower()

    emoji = get_emoji_for_weather(status)

    return (
        f"{emoji} Temperature: {temperature}°C\n"
        f"Condition: {weather_info['status'].capitalize()}\n"
        f"Humidity: {weather_info['humidity']}%\n"
        f"Wind speed: {weather_info['wind']['speed']}\n"
        f"Clouds: {weather_info['clouds']}%"
    )


def get_weather():
    city = entry_field.get()
    weather_info = api.get_weather_for_city(city)
    if weather_info:
        label["text"] = format_weather_info(weather_info)
    else:
        label["text"] = (
            "Error: Unable to get weather data.\nPlease check the city name."
        )


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

style = ttk.Style()
style.configure("TButton", background="#000000", foreground="#FFFFFF")

button = ttk.Button(
    frame,
    text="Get Weather",
    style="TButton",
    command=lambda: get_weather(),
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")


label = tk.Label(lower_frame, font=("Courier", 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
