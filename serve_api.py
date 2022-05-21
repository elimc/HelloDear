import waitress
from api.app import app


def serve_api(listen):
    waitress.serve(app, listen=listen)
