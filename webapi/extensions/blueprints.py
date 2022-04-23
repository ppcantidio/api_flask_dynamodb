from webapi.routes.artists import artists_routes


def init_app(app):
    app.register_blueprint(artists_routes, url_prefix='/api/v1/artists')
    