import pandas as pd 
import os
from dotenv import load_dotenv
from pipeline.location_search import locations
from pipeline.api_data_fetcher import api_data

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")

location = input("Enter the location: ")
location_data = locations(location).city_choices()

data = api_data(location_data, api_key).metrics_fetcher()
filtered_data = data.sort_values(by="datetime", ascending=False
                                 ).groupby("sensor_id", as_index=False
                                           ).first()
print(filtered_data)