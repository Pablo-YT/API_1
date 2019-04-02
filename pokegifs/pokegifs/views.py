from django.http import JsonResponse
from django.urls import path
import json 
import requests
import os 

key = os.environ.get("GIPHY_KEY")

def pokemon(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]

    gif_url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}".format(key, name)
    print(gif_url)
    gif_res = requests.get(gif_url)
    gif_body = json.loads(gif_res.content)
    gif = gif_body['data'][0]['url']
    




    return JsonResponse({
        "id": id,
        "name": body["name"],
        "types": body["types"],
        "gif" : ggif

    })

