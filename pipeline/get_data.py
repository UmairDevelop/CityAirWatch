from dotenv import load_dotenv
from pipeline.data_cleaner import get_location_sensors
import os

load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")

class data_retriver:
    def __init__(self, city):
        self.city = city

    def get_data(self):
        data = get_location_sensors(self.city).get_data()
        return data