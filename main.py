from WeatherApiService import WeatherApiServise as wapi
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('API_KEY')
api = wapi(API_KEY)

while True:
    print("\n Please enter your choice: add / view / search / delete / exit")
    option = input("\n Your choice: ").strip().lower()

    if option == "add":
        city = input("Please input the name of the city p: ").strip().lower()
        if not city.isalpha():
            print("\nThe name must contain only letters!")
            continue
        api.add_city(city)

    elif option == "view":
        for city, info in api.get_cities():
            print(f"{city.title()} --> {info['temperature']}°C (Time: {info['time']})")

    elif option == "search":
        search_city = input("Enter the name of the city you are looking for: ").strip().lower()
        api.get_city(search_city)

    elif option == "delete":
        delete_city = input("Enter the name of the city you are deleting : ").strip().lower()
        api.delete(delete_city)

    elif option == "exit":
        api.save_state()
        break

    else:
        print("\n Wrong choice! Please enter correctly!")