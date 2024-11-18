from pyowm import OWM


API_KEY = "ef2206ff5da67de63306d0b143e20872"


def get_weather_data(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    return observation.weather
