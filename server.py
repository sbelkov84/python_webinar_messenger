from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/status")
def status():
    time = datetime.strftime(datetime.now(), "%H:%M:%S")

    return {
        "status": True,
        "name": "Mesa",
        "time": time
    }


app.run()