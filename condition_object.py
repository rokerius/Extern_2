from flask import request
from request_funcs import get_location_key_and_name, get_data


class ConditionObject:
    def __init__(self):
        self.locationKey = None  # Ключ локации
        self.condition_data = None  # Данные о погоде
        self.lat = None  # Широта
        self.lon = None  # Долгота
        self.city = None
        self.city_name = None
        self.my_rate = None
        self.error_type = None

    def add_data_from_post(self, n_of_form):
        self.lat = request.form.get(f'latitude_{n_of_form}')
        self.lon = request.form.get(f'longitude_{n_of_form}')
        self.city = request.form.get(f'city_{n_of_form}')

    def add_locationKey(self):
        self.locationKey, self.city_name, self.error_type = (
            get_location_key_and_name(self.lat, self.lon, self.city))

    def add_condition_data(self):
        self.condition_data, self.my_rate = get_data(self.locationKey)
