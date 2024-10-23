# Проверяем координаты на недопустимые значения
def is_valid_coordinates(latitude, longitude):
    try:
        lat = float(latitude)
        lon = float(longitude)
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return True
        else:
            return False
    except ValueError:
        return False


# Собираем словарь с информацией, которую отправим для отображения
def give_main_info(condition):
    d = {}
    try:
        d['Temperature'] = condition["Temperature"]["Metric"]["Value"]
        d['WindSpeed'] = condition["Wind"]["Speed"]["Metric"]["Value"]
        d['AverageHumidity'] = condition["RelativeHumidity"]
        # d['Rain'] = condition[""]
        d['Pressure'] = round(condition['Pressure']['Metric']['Value'])
        d['WeatherText'] = condition['WeatherText']
        return d
    except:
        print(' - ERROR - condition обрабатывается некорректно -')
        print(condition)
        return False


# Модель оценки благоприятных условий
def weather_is_good(d):
    if (35 > int(d['Temperature']) > 5
            and int(d['WindSpeed']) < 35
            and 90_000 < int(d['Pressure'] * 100) < 110_000
            and 30 < d['AverageHumidity'] < 80):
        return True
    return False
