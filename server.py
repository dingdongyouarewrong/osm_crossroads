import json
import os

# git push heroku master
from flask import Flask, jsonify, request

app = Flask(__name__,template_folder='template')


@app.route('/get_data', methods=["POST", "GET"])
def get_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = str(dir_path) + "/gomel.json"
    f = open(filename)
    coordinates = json.load(f)
    f.close()
    return jsonify(coordinates)

@app.route('/get_data_by_city', methods=["POST", "GET"])
def get_data_by_city():
    city = request.args.get('city')
    print(city)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = str(dir_path) + f"json_geodata/{city}.json"
    f = open(filename)
    coordinates = json.load(f)
    f.close()
    return jsonify(coordinates)

app.run(host="0.0.0.0", port=os.environ["PORT"])
