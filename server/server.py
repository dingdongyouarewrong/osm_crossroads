import json

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_data', methods=["POST", "GET"])
def ready():
    # data = request.get_json()
    f = open("/Users/dmitry/PycharmProjects/osm_crossroads/gomel.json")
    coordinates = json.load(f)
    f.close()
    print("awdawd")
    return jsonify(coordinates)


app.run()

