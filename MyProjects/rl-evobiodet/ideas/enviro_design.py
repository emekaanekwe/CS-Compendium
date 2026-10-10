# the game environment will have the following features

class Environment():
    def __init__(self, weather: str, temperature: int):
        self.weather = weather
        self.temperature = temperature
    
    def get_weather(self):
        return self.weather
    
    def get_temperature(self):
        return self.temperature

# example enviro
hot_sunny = Environment(weather="sunny", temperature=30)
cold_cloudy = Environment(weather="cloudy", temperature=10)

# TODO: enviro modifies cards output. ex: 

        
    