from flask import *
from urllib.parse import quote_plus, urlencode
from app import app, oauth
from os import environ as env

@app.route("/")
def index():
    if "user" in session:
        print(session["user"])
    return "<p>Hello, render!</p>"

@app.route("/api/fact", methods=["GET"])
def getFact():
    return jsonify({"a": [1], "b": [2, 3]})

@app.route("/api/fact", methods=["POST"])
def postFact():
    response = request.json
    print(response)
    return jsonify({"state": True})

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("index", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )