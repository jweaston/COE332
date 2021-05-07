# api.py
import json
from flask import Flask, request
import jobs
import uuid 

app = Flask(__name__)

jobdb = jobs.jobdb
propertydb = jobs.propertydb

@app.route('/', methods=['GET'])
def list_routes():
    return """
    Routes:

    /               list routes
    /reloaddb       reloads property database
    /run            (GET) route instructions
    /run            (POST) submit job
    /properties     get instructions for route 
    /jobs           get list of jobs
    /jobs/<UUID>    get job results
    """

@app.route('/reloaddb', methods=['GET', 'POST'])
def load_database():
    if request.method == 'POST':
        init_database()
        return "Property database initialized"
    else:
        return """
            This is a route for loading the property data base. Use:
            
            curl -X POST localhost:5009/reloaddb
        """

@app.route('/run', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        try:
            job = request.get_json(force=True)
        except Exception as e:
            return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
        return json.dumps(jobs.add_job(job['start'], job['end']))
    else:
        return """
    This is  a route for POSTing jobs. Use:

    curl -X POST -d '{"start": "distance", "end": <propertyID>}' localhost:5009/run
    """

@app.route('/jobs', methods=['GET'])
def get_jobs():
    redis_dict = {}
    for key in jobdb.keys():
        redis_dict[str(key.decode('utf-8'))] = {}
        redis_dict[str(key.decode('utf-8'))]['status'] = jobdb.hget(key, 'status').decode('utf-8')
    return json.dumps(redis_dict, indent=4)

@app.route('/jobs/<jobuuid>', methods=['GET'])
def get_job(jobuuid):
    bytes_dict = jobdb.hgetall(jobuuid)
    final_dict = {}
    for key, value in bytes_dict.items():
        final_dict[key.decode('utf-8')] = value.decode('utf-8')
    return json.dumps(final_dict, indent=4)

@app.route('/properties', methods=['GET'])
def crud_properties():
    return """
    This is a route for CRUD operations. Use:

    /properties/create

    /properties/read

    /properties/update

    /properties/delete
    routes
    """

@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    if request.method == 'POST':
        uid = 'property.{}'.format(uuid.uuid4())
        property_data = request.get_json(force=True)
        propertydb.hmset(uid, property_data)
        return propertydb.hgetall(uid)
    else:
        return """
        Example
        curl -X POST -d '{
            "Property Name": "800 Leonard St",
            "Address": "800 Leonard St",
            "Total Rent": "$8,995",
            "Bed": "6",
            "Bath": 5,
            "Move-In Date": "08/07/21",
            "Property Manager": "Respace",
            "Available Units": "House",
            "Neighborhood": "Noth Campus",
            "Commission Paid": "30-60 Days Post Paperwork Completion"
            }' 
            localhost:5009/properties/create
        """

@app.route('/properties/read', methods=['GET', 'POST'])
def read_property():
    if request.method == 'POST':
        if request.args.lists() == "":
            redis_dict = {}
            for key in propertydb.keys():
                redis_dict[str(key.decode('utf-8'))] = {}
                for att in ['Property Name', 'Address', 'Total Rent', 'Bed','Bath', 'Available Units', 'Neighborhood' ,'Property Manager']:
                    redis_dict[str(key.decode('utf-8'))][att] = propertydb.hget(key, att).decode('utf-8')
            return json.dumps(redis_dict, indent=4)
        else:
            redis_dict = {}
            for key in propertydb.keys():
                flag1 = True
                # testList = []
                for arg in request.args.lists():
                    # testList.append(arg)
                    if propertydb.hget(key, arg[0]).decode("utf-8") == str(arg[1][0]):
                        continue
                    else:
                        flag1 = False
                        break
                if flag1:
                    redis_dict[str(key.decode('utf-8'))] = {}
                    for att in ['Property Name', 'Address', 'Total Rent', 'Bed','Bath', 'Available Units', 'Neighborhood' ,'Property Manager']:
                        redis_dict[str(key.decode('utf-8'))][att] = propertydb.hget(key, att).decode('utf-8')
                else: 
                    continue
            # return json.dumps(testList)
            return json.dumps(redis_dict, indent=4)
    else:
        return """
        curl -X POST localhost:5009/properties/read?<arg>=<parameter>&<arg>=<parameter>
        example:
        curl -X POST localhost:5009/properties/read?Neighborhood=West%20Campus
        To get all properties:
        curl -X POST localhost:5009/properties/read
        """
@app.route('/properties/update', methods=['GET', 'POST'])
def update_property():
    if request.method == 'POST':
        uid = request.args.get('uid')
        property_data = request.get_json(force=True)
        for attribute in property_data:
            propertydb.hset(uid, attribute[0], attribute[1][0])
        return propertydb.hgetall(uid)
    else:
        return """
        curl -X POST localhost:5009/properties/update?uid=<propertyID>
        example:
        curl -X POST localhost:5009/properties?/update?uid=property.3d6f6346-3003-4afc-b02f-52b5e492b4c0
        """    
@app.route('/properties/delete', methods=['GET', 'POST'])
def delete_property():
    if request.method == 'POST':
        uid = request.args.get('uid')
        propertydb.delete(uid)
        return "property deleted"
    else:
        return """
        curl -X POST localhost:5009/properties/delete?uid=<propertyID>
        example:
        curl -X POST localhost:5009/properties?/delete?uid=property.3d6f6346-3003-4afc-b02f-52b5e492b4c0
        """ 

def init_database():
    propertydb.flushdb()
    with open("./Housing_data.json", "r", encoding="utf8") as json_file:
        property_data = json.load(json_file)
        for prop in property_data:
            propertydb.hmset('property.{}'.format(uuid.uuid4()), prop)

if __name__ == '__main__':
    init_database()
    app.run(debug=True, host='0.0.0.0')