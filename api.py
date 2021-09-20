from decouple import config
import requests


def make_request(city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config('SECRET_API_KEY')}"
    response = requests.get(api_url)
    return response.json()


def format_response(data):
    temperature_in_celsius = convert_kelvin_to_celsius(data['main']['temp'])
    conditions = data['weather'][0]['description']
    return f"The temperature of {data['name']} is {temperature_in_celsius}\N{DEGREE SIGN}c and the conditions are {conditions}, " \
           "have a great day!"


def convert_kelvin_to_celsius(value_in_kelvin):
    return str(value_in_kelvin - 273.15)[:5]


def send_response():
    pass


if __name__ == '__main__':
    # print(format_response(make_request("Dubai")))
    for item in make_request("London"):
        print(item)
