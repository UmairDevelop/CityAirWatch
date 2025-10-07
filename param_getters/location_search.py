from param_getters.get_location_sensors_ids import get_ids_data

class locations:
    def __init__(self, city):
        self.city = city

    def city_choices(self):
        self.city = get_ids_data(self.city).get_unit_values()
        city_choices = self.city["location_name"].unique()

        print("Available Locations: ")
        for i, loc in enumerate(city_choices, 1):
            print(f"{i}. {loc}")
        
        location_choice = int(input("\nSelect a location (number): ").strip())
        if 1 <= location_choice <= len(city_choices):
            selected_location = city_choices[location_choice - 1]
            filtered_location = self.city[self.city["location_name"] == selected_location]
            return filtered_location
        else:
            return KeyError("Wrong Selection-Location not available")