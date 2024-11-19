import tkinter as tk
from tkinter import font
from OWM import get_weather

HEIGHT = 350
WIDTH = 450


def display_weather():
    city = entry_field.get()
    weather = get_weather(city)
    
    if "error" in weather:
        message = f"Error: {weather['error']}"
    else:
        temp = weather["temperature"]
        message = (
            f"Status: {weather['status']} \n"
            f"Temperature: {temp['temp']}°C \n"
            f"Clouds: {weather['clouds']}% \n"
            f"Rain: {weather['rain']} \n"
            f"Humidity: {weather['humidity']}% \n"
            f"Heat Index: {weather['heat index']} \n"
            f"Wind: {weather['wind']}"
        )
    label['text'] = message


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
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

