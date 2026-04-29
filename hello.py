import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    message = os.getenv("APP_MESSAGE", "Hello, World!")
    return f"<p>{message}</p>"


@app.route("/health")
def health():
    return {"status": "ok"}, 200
