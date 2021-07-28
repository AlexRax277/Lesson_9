import requests


def the_smartest_hero(*heroes):
    list_heroes = list(heroes)
    token = 1232818720514474
    url = f'https://superheroapi.com/api/{token}/search/'
    dict_heroes = {}
    for hero in list_heroes:
        url_hero = f'{url}{hero}'
        resp_hero = requests.get(url_hero)
        intellect_hero = int(resp_hero.json()['results'][0]['powerstats']['intelligence'])
        dict_heroes[hero] = intellect_hero
    sorted_dict_heroes = dict(sorted(dict_heroes.items(), key=lambda x: x[0]))
    return f'The smartest hero is {list(sorted_dict_heroes.keys())[-1]}'


print(the_smartest_hero('Hulk', 'Captain America', 'Thanos'))
