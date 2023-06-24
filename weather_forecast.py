import requests
import json

API_KEY = 'b14e5040c1d5762d29e31f406a58a1b1' 


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)

    if response.status_code == 200:

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"Error: {data['message']}")


if __name__ == '__main__':
    city_name = input("Enter a city name: ")
    get_weather(city_name)
