import json
import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')


try:
    with open("weather_application.txt", "r") as file:
        data = file.read().strip()
        forecast = json.loads(data) if data else {}
except (FileNotFoundError, json.JSONDecodeError):
    forecast = {}

app_status = True

while app_status:
    print("\n Please enter your choice: add / view / search / delete / exit")
    option = input("\n Your choice: ").strip().lower()

    if option == "add":
        city = input("Please input the name of the city p: ").strip().lower()
        if not city.isalpha():
            print("\nThe name must contain only letters!")
            continue

        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

        try:
            response = requests.get(url)
            weather_data = response.json()

            if "error" in weather_data:
                print("\nNot found the city")
                continue

            temp = weather_data['current']['temp_c']
            time_of_data = weather_data['location']['localtime']

            forecast[city] = {"temperature": temp, "time": time_of_data}
            print(f"\n✅ {city.title()} was added: {temp}°C ({time_of_data})")

        except requests.exceptions.RequestException:
            print("\nAn error occured!")

    elif option == "view":
        if forecast:
            print("\n📋Saved weather forecast :")
            for city, info in forecast.items():
                print(f"{city.title()} --> {info['temperature']}°C (Time: {info['time']})")
        else:
            print("\n There isn't any weather forecast!")

    elif option == "search":
        search_city = input("Enter the name of the city you are looking for: ").strip().lower()

        if search_city in forecast:
            info = forecast[search_city]
            print(f"\n🔍 {search_city.title()} --> {info['temperature']}°C (Time: {info['time']})")
        else:
            print("\n📡 There isn't this city in local data, checking online...")
            url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={search_city}&aqi=no"

            try:
                response = requests.get(url)
                weather_data = response.json()

                if "error" in weather_data:
                    print("\n Not found the city!")
                else:
                    temp = weather_data['current']['temp_c']
                    time_of_data = weather_data['location']['localtime']
                    forecast[search_city] = {"temperature": temp, "time": time_of_data}
                    print(f"\n {search_city.title()} --> {temp}°C (Timet: {time_of_data}) (Newly was added!)")
            except requests.exceptions.RequestException:
                print("\n An error occured!")

    elif option == "delete":
        delete_city = input("Enter the name of the city you are deleting : ").strip().lower()
        if delete_city in forecast:
            del forecast[delete_city]
            print(f"\n {delete_city.title()} data was deleted!")
        else:
            print("\nNot found appropriate city !")

    elif option == "exit":
        with open("weather_application.txt", "w") as file:
            json.dump(forecast, file, indent=4)

        print("\n Data was saved in memory")
        print(" Existing from programme... See you later!")
        app_status = False

    else:
        print("\n Wrong choice! Please enter correctly!")