import json
import os
import netifaces as nif

# git push heroku master
from flask import Flask, jsonify, render_template, request

app = Flask(__name__,template_folder='template')

@app.route('/')
def scum():
    ip = request.remote_addr
    print(ip)
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        addrs = nif.ifaddresses(i)
        # if_mac = addrs[nif.AF_LINK][0]['addr']
        # if_ip = addrs[nif.AF_INET][0]['addr']
        print(addrs)
    return render_template('hello.html')

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
    filename = str(dir_path) + "/gomel.json"
    f = open(filename)
    coordinates = json.load(f)
    f.close()
    print("awdawd")
    return jsonify(coordinates)

app.run(host="0.0.0.0", port=os.environ["PORT"])
