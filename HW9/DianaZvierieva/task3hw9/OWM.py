from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    info_weather = {
        "status": w.detailed_status,
        "wind": w.wind(),
        "humidity": w.humidity,
        "temperature": w.temperature('celsius'),
        "rain": w.rain,
        "heat_index": w.heat_index,
        "clouds": w.clouds
    }

    return info_weather






