import pandas as pd 
import os, requests
from dotenv import load_dotenv
from param_getters.location_search import locations
from param_getters.api_data_fetcher import api_data

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")

location = input("Enter the location: ")
location_data = locations(location).city_choices()

data = api_data(location_data, api_key).metrics_fetcher()
filtered_data = data.sort_values(by="datetime", ascending=False
                                 ).groupby("sensor_id", as_index=False
                                           ).first()
print(filtered_data)