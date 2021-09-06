import requests

WEATHER_URL = 'http://wttr.in/{city}'
MSG_CONNECTION_ERROR = '<сетевая ошибка>'
MSG_SERVER_ERROR = '<ошибка на сервере погоды. попробуйте позже>'
MSG_TEMPERATURE_ERROR = 'Не могу узнать погоду...'

WEATHER_TOO_COLD = 'Как-то холодно, зубы не сводит? Повремени-ка с мороженым'
WEATHER_NICE = 'Думаю в самый раз, время есть мороженое!'
WEATHER_TOO_HOT = 'Фух, жарко! Срочно получите порцию мороженого!'


def what_weather(city):
    url = WEATHER_URL.format(city=city)
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return MSG_CONNECTION_ERROR
    if response.status_code == 200:
        return response.text.strip()
    else:
        return MSG_SERVER_ERROR


def what_temperature(weather):
    if (weather == MSG_CONNECTION_ERROR or weather == MSG_SERVER_ERROR):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature


def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
        if temperature < 18:
            return WEATHER_TOO_COLD
        elif 18 <= temperature <= 27:
            return WEATHER_NICE
        else:
            return WEATHER_TOO_HOT
    except ValueError:
        return MSG_TEMPERATURE_ERROR
