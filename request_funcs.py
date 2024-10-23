from flask import redirect

from numbers_funcs import *
import requests

API_KEY = "lOqUGEnwX0RpmUMu8moAAwAGxj9wHYrb"
# https://developer.accuweather.com/
# (только 50 запросов с ключа, тут свеженький)


# Получаем данные о погоде
def get_data(locationKey):
    condition_data = None
    my_rate = None
    try:
        url_cond = (f'http://dataservice.accuweather.com/currentconditions/v1/'
                    f'{locationKey}?apikey={API_KEY}&details=true&language=ru')
        condition = requests.get(url_cond).json()[0]
        condition_data = give_main_info(condition)
        print(f'- Получено состояние по locationKey')
        my_rate = "Погода супер, можно выходить" if weather_is_good(condition_data) \
            else "Погода кошмар, сиди дома"
    except:
        print("- ОШИБКА - condition не получен -")
    return condition_data, my_rate  # Данные о погоде, моя оценка погода


# Из города получаем locationKey
def get_location_key_and_name(lat, lon, city):
    locationKey = None
    city_name = None
    error_type = None
    if city is not None and city != "":
        try:
            language = 'ru' if 'а' < city[0].lower() < 'я' else 'en'
            url_city = f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey={API_KEY}&q={city}&language={language}"
            req = requests.get(url_city).json()[0]
            locationKey = req["Key"]
            city_name = f"{req['Country']['LocalizedName']},\n{req['AdministrativeArea']['LocalizedName']}, {req["LocalizedName"]}"
            print(f'- Получен locationKey: {locationKey}')
        except:
            error_type = 'city_error'
            print("- ОШИБКА - город не преобразован в locationKey -")

    elif lat is not None and lat != "" and lon is not None and lon != "":
        if is_valid_coordinates(lat, lon):
            try:
                url_geo = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={lat}%2C{lon}%20'
                locationKey = requests.get(url_geo).json()['Key']
                print(f'- Получен locationKey: {locationKey}')
            except:
                error_type = 'lat_error'
                print("- ОШИБКА - locationKey не получен из lan и lon -")
        else:
            error_type = "lat_error"
    return locationKey, city_name, error_type  # Ключ точки, название точки, ошибки(если возникли)


# Тестируем подключение
def try_api():
    try:
        test_link = f"http://dataservice.accuweather.com/locations/v1/{1314058}?apikey={API_KEY}"
        test_api = requests.get(test_link).json()['EnglishName']
        if test_api == "Agamcagam":
            return True
    except:
        return False
