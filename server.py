import json
import os
import sys

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data', methods=["POST", "GET"])
def ready():
    # data = request.get_json()
    f = open("/gomel.json")
    coordinates = json.load(f)
    f.close()
    print("awdawd")
    return jsonify(coordinates)

app.run(host="0.0.0.0", port=os.environ["PORT"])

