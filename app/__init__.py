from flask import Flask
from authlib.integrations.flask_client import OAuth
from os import environ as env

app = Flask(__name__)
app.secret_key = env['FLASK_SECRET']
oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

from app import routes