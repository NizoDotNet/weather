import json

class StateServiceMixin:
    def add(self, weather_data: dict, city_name: str):
        temp = weather_data['current']['temp_c']
        time_of_data = weather_data['location']['localtime']
        self._forecast[city_name] = {"temperature": temp, "time": time_of_data}
        print(f"\n✅ {city_name.title()} was added: {temp}°C ({time_of_data})")

    def get_all(self) -> dict:
        return self._forecast

    def get(self, city_name):
        return self._forecast.get(city_name)

    def delete(self, city_name):
        if city_name in self._forecast:
            del self._forecast[city_name]
        else:
            print('There is no city with this name!')

    def save_state(self):
        with open("weather_application.txt", "w") as file:
            json.dump(self._forecast, file, indent=4)
        print("\n✅ Data was saved in memory")
        print("👋 Exiting program... See you later!")
