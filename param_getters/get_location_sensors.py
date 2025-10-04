import pandas as pd
import ast

class get_location_sensors:
    locations = pd.read_csv("../locations.csv")
    def __init__(self, city):
        self.city = city

    def get_sensor_ids(self):
        self.city = self.city
        city_locations = self.locations[self.locations["name"].str.contains(self.city, case=False, na=False)]
        
        city_data = pd.DataFrame({
            "id": city_locations["id"].values,
            "location": city_locations["name"].values,
            "sensor": city_locations["sensors"].values,
        })

        city_data["sensor"] = city_data["sensor"].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else x
        )
        city_data["sensor"] = city_data["sensor"].apply(
            lambda sensor: [s["id"] for s in sensor] if isinstance(sensor, list) else []
        )

        # explode + deduplicate
        sensors_explode = city_data.explode("sensor").reset_index(drop=True)
        sensors_explode = sensors_explode.drop_duplicates(subset=["id"]).reset_index(drop=True)

        return sensors_explode


print(get_location_sensors("Lahore").get_sensor_ids())