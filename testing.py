import pandas as pd
import requests
import os

from dotenv import load_dotenv
load_dotenv()

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market": "classic", "iso_date": "2018-12-01", "federation": "UEFA"}

headers = {"X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'), "X-RapidAPI-Host": os.getenv('X-RapidAPI-Host')}

response = requests.get(url, headers=headers, params=querystring)

my_set = pd.DataFrame(response.json()['data'])
print(my_set)
