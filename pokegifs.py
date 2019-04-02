import os
import requests
import json
import requests

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"])

key = os.environ.get("GIPHY_KEY")


url = "https://api.giphy.com/v1/gifs/search?api_key=2ZvDWyUWRleLV9905xUu9TFJolpRULZN&q=videogames&rating=g".format(key)
requests.get(url)
print(url)
