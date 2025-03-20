import requests
from random import randint


def download_random_comic():
    latest_comic = requests.get("https://xkcd.com/info.0.json").json()
    random_comic_num = randint(1, latest_comic["num"])

    random_comic_url = f"https://xkcd.com/{random_comic_num}/info.0.json"
    response = requests.get(random_comic_url)
    response.raise_for_status()

    return response.json()
