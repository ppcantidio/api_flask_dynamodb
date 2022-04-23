import os
import uuid
import json
import redis
from webapi.extensions.database import dynamo
from flask import Blueprint, request, jsonify
from webapi.utils.genius import songs_by_artist


artists_routes = Blueprint('artists_routes', __name__)

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT')
)


class ArtistsRoutes:

    @artists_routes.route('/', methods=['POST'])
    def get_artist():
        artist = request.form.get('artist')
        cache = request.args.get('cache')

        if cache != 'False':
            response_cache = redis_client.get(artist)
            if response_cache is not None:
                response_cache = response_cache.decode('utf-8')
                response_cache = str(response_cache).replace("'", '"')
                response_cache = json.loads(response_cache)
                return jsonify(response_cache)

        songs = songs_by_artist(artist)
        if songs == None or songs == []:
            return jsonify({
                'status': 'error'
            })

        songs_list = []
        for song in songs:
            song_dict = {}
            song_dict['title'] = song['result']['title']
            song_dict['artists'] = song['result']['artist_names']
            songs_list.append(song_dict)

        document = {
            'UUID': str(uuid.uuid4()),
            'name': artist,
            'songs': songs_list
        }

        dynamo.tables['artists'].update_item(
            Key={
                'name': artist
            },
            UpdateExpression="set songs=:s",
            ExpressionAttributeValues={
                ":s": songs_list
            }
        )
        
        response_document = {
            'status': 'success',
            'artist': document,
        }

        redis_client.delete(artist)
        redis_client.set(artist, str(response_document))
        redis_client.expire(artist, 604800)

        return jsonify(response_document)
            