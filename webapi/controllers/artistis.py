from flask import Blueprint
from utils.database import Database


artists_routes = Blueprint('users_routes', __name__)
db = Database()

class ArtistsRoutes:

    @artists_routes.route('/', methods=['GET'])
    def get_artist():
        pass
