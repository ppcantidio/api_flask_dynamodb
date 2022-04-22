from flask import Flask
from dotenv import load_dotenv
from webapi.utils.database import Database
from webapi.config import DevelopmentConfig

load_dotenv('.env')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = Database()
db.create_table()

from webapi.controllers.artistis import artists_routes
app.register_blueprint(artists_routes, url_prefix='/api/v1/artists')

