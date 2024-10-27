#DSC 510
#Week 10
#Programming Assignment
#Author Michael Perrine
#10/31/2024

import requests
import json
import urllib.request, urllib.response, urllib.parse, urllib.error


joke_url = 'https://api.chucknorris.io/jokes/random'

params= {"limitTo" : "[science]"}

response = requests.get(joke_url,params)

joke = response.json() ["value"]

print(joke)













