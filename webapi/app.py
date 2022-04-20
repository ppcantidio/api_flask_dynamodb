from flask import Flask
from dotenv import load_dotenv
from webapi.config import DevelopmentConfig

load_dotenv('.env')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from webapi.controllers.artistis import artists_routes
app.register_blueprint(artists_routes, url_prefix='/api/v1/artistas')

