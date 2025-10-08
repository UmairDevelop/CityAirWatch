import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

class api_data:
    def __init__(self, data, api_key):
        self.data = data
        self.api_key = api_key

    def metrics_fetcher(self):
        selected_location = self.data
        datetime_from = datetime.now(timezone.utc) - timedelta(days=1)
        datetime_to = datetime.now(timezone.utc)

        datetime_from_str = datetime_from.strftime("%Y-%m-%dT%H:%M:%SZ")
        datetime_to_str = datetime_to.strftime("%Y-%m-%dT%H:%M:%SZ")

        api_url = "https://api.openaq.org/v3/sensors"
        headers = {"X-API-Key": self.api_key}

        all_data = []

        # Loop through each sensor for the city
        for _, row in selected_location.iterrows():
            sensor_id = row["sensor_id"]
            sensor_name = row["name"]
            sensor_unit = row["unit"]

            url = f"{api_url}/{sensor_id}/hours"
            params = {"datetime_from": datetime_from_str, "datetime_to": datetime_to_str}

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                results = response.json().get("results", [])
                if results:
                    for entry in results:
                        all_data.append({
                            "sensor_id": sensor_id,
                            "parameter": sensor_name,
                            "unit": sensor_unit,
                            "value": entry.get("value"),
                            "datetime": entry["period"]["datetimeTo"]["utc"]
                        })
                else:
                    print(f"⚠️ No data found for {sensor_name} ({sensor_id})")
            else:
                print(f"❌ API error for {sensor_id}: {response.status_code}")

        # Convert list to DataFrame
        df = pd.DataFrame(all_data)
        return df