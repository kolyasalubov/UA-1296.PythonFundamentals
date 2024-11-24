from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city): 
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_detail = {"status": w.detailed_status,
                        "temperature": w.temperature('celsius'),
                        "clouds": w.clouds,
                        "rain": w.rain,
                        "humidity": w.humidity,
                        "heat index": w.heat_index,
                        "wind": w.wind}
        return weather_detail



# ---------- FREE API KEY examples ---------------------


# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather

# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75





