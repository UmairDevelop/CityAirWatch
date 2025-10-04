from openaq import OpenAQ
from math import ceil
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")
api = OpenAQ(api_key=api_key)

locations = api.locations.list()
meta = locations.meta
found = meta.found

limit = 1000

data = pd.DataFrame()
for dat in range(30):
    data = pd.concat([data, pd.DataFrame(api.locations.list(limit=limit, page=dat+1).results)], ignore_index=True)
    
data.to_csv("locations.csv", index=False)

api.close()