from django.shortcuts import render

from anfisa.models import friends_db
from anfisa.services import what_conclusion, what_temperature, what_weather
from icecream.models import icecream_db

CITY_WEATHER = 'В городе {city} погода: {weather}'
FRIEND_OUTPUT = '{friend}, тебе прислали {icecream}!'


def index(request):
    icecreams = ''
    friends = ''
    city_weather = ''
    friend_output = ''
    selected_icecream = ''
    conclusion = ''

    for friend in friends_db:
        friends += (f'<input type="radio" name="friend"'
                    f' required value="{friend}">{friend}<br>')

    for i in range(len(icecream_db)):
        ice_form = (
            f'<input type="radio" name="icecream" required'
            f' value="{icecream_db[i]["name"]}">{icecream_db[i]["name"]}'
        )

        ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
        icecreams += f'{ice_form} | {ice_link} <br>'

    if request.method == 'POST':
        selected_friend = request.POST['friend']
        selected_icecream = request.POST['icecream']
        city = friends_db[selected_friend]
        weather = what_weather(city)
        parsed_temperature = what_temperature(weather)
        conclusion = what_conclusion(parsed_temperature)
        friend_output = FRIEND_OUTPUT.format(friend=selected_friend,
                                             icecream=selected_icecream)
        city_weather = CITY_WEATHER.format(city=city, weather=weather)
    context = {
        'icecreams': icecreams,
        'friends': friends,
        'friend_output': friend_output,
        'city_weather': city_weather,
        'conclusion': conclusion,
    }
    return render(request, 'homepage/index.html', context)
