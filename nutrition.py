from decouple import config
import requests


def get_nutrition_data(food):
    api_url = f"https://api.calorieninjas.com/v1/nutrition?query={food}"
    response = requests.get(api_url, headers = {
        "X-Api-Key": config('NUTRITION_API_KEY')
    })
    return response.json()


def convert_to_kilo(item):
    return item * 10


if __name__ == "__main__":
    # save to database
    print(get_nutrition_data("ribeye")['items'][0]['calories'])