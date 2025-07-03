import requests


def get_city_name():
    try:
        city_name = input("Enter city name: ")
        get_weather(city_name)
    except Exception as e:
        print(f"Error: {e}")
        get_city_name()


def get_weather(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=07bf0aa66592a5f05be1020a41fe073a&units=metric")
    data = response.json()

    print(f"Weather Information in {city_name}")
    print(f"Weather: {data['weather'][0]['main']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Wind Speed: {data['wind']['speed']} m/s")


get_city_name()
