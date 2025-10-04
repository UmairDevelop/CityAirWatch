import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")

def get_countries():
    url = "https://api.openaq.org/v3/countries"
    headers = {
        "X-API-Key": api_key
    }
    params = {
        "order_by": "id",
        "sort_order": "asc",
        "limit": 200
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        print(f"Error: {response.status_code}")

countries = get_countries()
api_country_collection = pd.json_normalize(countries)
trim_countries = api_country_collection[["id", "name"]]

trim_countries.to_csv("countries.csv", index=False)