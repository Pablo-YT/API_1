import os
import requests

key = os.environ.get("GIPHY_KEY")


url = "https://api.giphy.com/v1/gifs/search?api_key=2ZvDWyUWRleLV9905xUu9TFJolpRULZN&q=videogames&rating=g".format(key)
print(requests.get(url))