import requests

api_key = 'd3f6c723859c7c1b409ed0f784be129c'

city_name = input("Enter City Name: ")

weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key}')


if weather_url.status_code == 200:
    print("Successfully retrieved weather data.")

if weather_url.json().get('cod') == '404':
    print("City not found. Please check the city name and try again.")
else:
    weather = weather_url.json()['weather'][0]['main']
    temp = weather_url.json()['main']['temp']

    print(f"The weather in {city_name} is currently {weather} with a temperature of {temp}°F.")
    print(weather_url.json())

 