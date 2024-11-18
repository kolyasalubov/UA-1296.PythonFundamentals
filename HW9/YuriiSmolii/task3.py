from OWM_weather import get_weather_data
import tkinter as tk
from tkinter import font

HEIGHT = 600
WIDTH = 500

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 10),
    command=lambda: get_weather(),
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Courier", 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

def get_weather():
    location = entry_field.get()
    data = get_weather_data(location)
    final_message = (
        f"Weather in {location}:\n"
        f"-----------------------\n"
        f"Status: {data.detailed_status}\n"
        f"Temperature: \n"
        f"  temperature {data.temperature('celsius')['temp']}°C\n"
        f"  temperature max {data.temperature('celsius')['temp_max']}°C\n"
        f"  temperature min {data.temperature('celsius')['temp_min']}°C\n"
        f"  temperature fils like {data.temperature('celsius')['feels_like']}°C\n"
        f"Rain: {data.rain}\n"
        f"Humidity: {data.humidity}%\n"
        f"heat_index: {data.heat_index}\n"
        f"Wind Speed: {data.wind()['speed']} m/s\n"
        f"Clouds: {data.clouds}%"
    )

    label.config(text=final_message, justify="left", anchor="nw")
    entry_field.delete(0, "end")


root.mainloop()
