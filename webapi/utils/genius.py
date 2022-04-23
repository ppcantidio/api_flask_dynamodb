import os
import requests


def songs_by_artist(artist_name):
    token = os.environ.get('GENIUS_TOKEN')
    base_url = os.environ.get('GENIUS_BASE_URL')

    url = f'{base_url}search/?q={artist_name}'

    data = {'access_token': token}

    response = requests.get(
        data=data,
        url=url
    )

    status = response.status_code
    if status != 200:
        return None

    response = response.json()

    if 'response' not in response:
        return None

    songs = response['response']['hits']
    return songs
    