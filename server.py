import json
import os
import sys

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data', methods=["POST", "GET"])
def ready():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = str(dir_path)+"/gomel.json"
    # data = request.get_json()
    f = open(filename)
    coordinates = json.load(f)
    f.close()
    print("awdawd")
    return jsonify(coordinates)

app.run(host="0.0.0.0")

