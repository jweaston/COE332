import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/animals', methods=['GET'])
def animals():
    return json.dumps(get_all_data())

@app.route('/animals/head/<htype>', methods=['GET'])
def animals_by_head(htype):
    return json.dumps(get_head_data(htype))

@app.route('/animals/legs/<nlegs>', methods=['GET'])
def  animals_by_legs(nlegs):
    return json.dumps(get_leg_data(nlegs))

def get_all_data():
    with open("data_file.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

def get_head_data(htype):
    with open("data_file.json", "r") as json_file:
        userdata = json.load(json_file)
    output = [x for x in userdata if x['head'] == htype]
    return output

def get_leg_data(nlegs):
    with open("data_file.json", "r") as json_file:
        userdata = json.load(json_file)
    output = [x for x in userdata if x['legs'] == int(nlegs)]
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')