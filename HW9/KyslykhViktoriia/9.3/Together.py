import tkinter as tk
from tkinter import font
from pyowm import OWM
from config import KEY

HEIGHT = 350
WIDTH = 450

owm = OWM(KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()

    if not city:
        label['text'] = "Please enter a city!"
        return
    
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        
        detailed_status = w.detailed_status
        wind = w.wind()
        humidity = w.humidity
        temperature = w.temperature('celsius')

        label['text'] = (
            f"Weather: {detailed_status.capitalize()}\n"
            f"Temperature: {temperature['temp']}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind['speed']} m/s")
    
    except Exception as e:
        label['text'] = "City not found or unavailable."
        print(f"Error: {e}")


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="sky blue", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()


