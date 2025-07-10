import requests
from StateService import StateServiceMixin
class WeatherApiServise(StateServiceMixin):
    def __init__(self, api_key: str):
        self._url = f"https://api.weatherapi.com/v1/current.json?key={api_key}"
        self._forecast = {}
        self.load_data()
    def add_city(self, city_name: str) -> int:
        try:
            response = requests.get(self._url + f'&q={city_name}')
            weather_data = response.json()

            if "error" in weather_data:
                print("\nNot found the city")
                return -1

            self.add(weather_data, city_name)
            return 0
        except requests.exceptions.RequestException:
            print("\nAn error occured!")
            return -1
    def get_cities(self):
        for city, info in self._forecast.items():
            yield city, info
    def get_city(self, city_name: str):
        city = self.get(city_name)
        if city:
            return city
        else:
            print('No city with this name!')
            self.add_city(city_name)
            return self.get_city(city_name)
    def exit(self):
        self.save_state()
    