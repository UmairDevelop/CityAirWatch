import pandas as pd
import ast
from param_getters.data_cleaner import get_location_sensors

class get_ids_data:
    def __init__(self, city):
        self.city = city

    def get_unit_values(self):
        locations = get_location_sensors(self.city).get_data()
        locations["sensors"] = locations["sensors"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])

        sensors_list = []
        for _,loc in locations.iterrows():
            location_id = loc["ids"]
            location_name = loc["locations"]
            for s in loc["sensors"]:
                sensors_list.append({
                    "location_id": location_id,
                    "location_name": location_name,
                    "sensor_id": s.get("id"),
                    "name": s["parameter"]["name"],
                    "unit": s["parameter"]["units"]
                })
        sensors_df = pd.DataFrame(sensors_list).drop_duplicates().reset_index(drop=True)
        return sensors_df