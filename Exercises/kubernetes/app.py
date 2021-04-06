import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello world\n"

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    return "Hello {}\n".format(name)

@app.route('/hello', methods=['GET'])
def hello_name1():
    print(request.args)
    for i in request.args.keys():
        print(i, '\n')
    name = request.args.get('name')
    return "(round 2 electric boogaloo) Hello {}\n".format(name)

@app.route('/animals', methods=['GET'])
def  get_animals():
    return json.dumps(get_data())

def get_data():
    with open("data_file.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')