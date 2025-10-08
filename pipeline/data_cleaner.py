import pandas as pd
import os

class get_location_sensors:
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    csv_path = os.path.join(base_dir, "../locations.csv") 
    locations = pd.read_csv(csv_path)
    def __init__(self, city):
        self.city = city

    def get_data(self):
        self.city = self.city
        city_locations = self.locations[self.locations["name"].str.contains(self.city, case=False, na=False)]
        
        city_data = pd.DataFrame({
            "ids": city_locations["id"].values,
            "locations": city_locations["name"].values,
            "sensors": city_locations["sensors"].values,
        })

        # city_data["sensor"] = city_data["sensor"].apply(
        #     lambda x: ast.literal_eval(x) if isinstance(x, str) else x
        # )
        # city_data["sensor"] = city_data["sensor"].apply(
        #     lambda sensor: [s["id"] for s in sensor] if isinstance(sensor, list) else []
        # )

        # explode + deduplicate
        sensors_explode = city_data.explode("sensors").reset_index(drop=True)
        sensors_explode = sensors_explode.drop_duplicates(subset=["ids"]).reset_index(drop=True)

        return city_data