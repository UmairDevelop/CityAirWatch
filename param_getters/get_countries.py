import pandas as pd
import ast

class get_countries:
    locations = pd.read_csv("../locations.csv")
    countries = locations["country"].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
    countries_data = pd.DataFrame(countries.tolist())
    countries_data = countries_data.drop_duplicates().reset_index(drop=True)
    countries_data["name"] = countries_data["name"].str.lower()

    def __init__(self, country):
        self.country = country
    
    def get_country_param(self):
        self.country  = self.country.lower()
        if self.country in self.countries_data["name"].values:
            raw = self.countries_data[self.countries_data["name"] == self.country]
            id, code, name = raw["id"].values, raw["code"].values, raw["name"].values
            return id[0], code[0], name[0]
        else:
            return None