import pandas as pd
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")

def get_country_code(country):
    countries = pd.read_csv("countries.csv")
    countries["name"] = countries["name"].str.lower()
    
    if country.lower() not in countries["name"].values:
        raise ValueError(f"Country '{country}' not found in the dataset.")
    
    country_code = countries[countries["name"] == country.lower()]["id"]
    return country_code.values[0]

def get_data(country):
    url = f"https://api.openaq.org/v3/countries/{get_country_code(country=country)}"
    headers = {"X-API-Key": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        return results
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
    
print(get_data(input("Enter country name: ")))