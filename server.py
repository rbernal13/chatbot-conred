import json
import sys

from flask import Flask, request

from src.intentMap import intentMap

app = Flask(__name__)


@app.route('/test',  methods=["GET"])
def hello_world():
    return 'Chatbot CONRED ejecutandose......'


@app.route('/', methods=["GET", "POST"])
def server():
    try:
        # Obteniendo del obj request que envió Dialogflow
        req = request.get_json(force=True)
        # print('REQ',json.dumps(req, indent=1))
        return intentMap(req)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print(e.message)

    