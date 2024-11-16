from pyowm import OWM

API_KEY = "ef2206ff5da67de63306d0b143e20872"
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather_for_city(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_info = {
            "status": w.detailed_status,
            "temperature": w.temperature("celsius")["temp"],
            "humidity": w.humidity,
            "wind": w.wind(),
            "clouds": w.clouds,
        }
        return weather_info
    except Exception as e:
        return None
