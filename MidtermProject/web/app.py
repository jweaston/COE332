import json
import redis
import datetime
from flask import Flask, request

rd = redis.StrictRedis(host='redis', port=6379, db=0)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    with open("../data_file.json", "r") as json_file:
            userdata = json.load(json_file)
            index = 0
            rd.flushdb()
            for animal in userdata:
                rd.hmset('k'+str(index), animal)
                index += 1
    return 'Data base initialized \n'
    
@app.route('/reset', methods=['GET'])
def reset():
    with open("../data_file.json", "r") as json_file:
        userdata = json.load(json_file)
        index = 0
        rd.flushdb()
        for animal in userdata:
            rd.set('k'+str(index), animal)
            index += 1
    return 'Data base reset \n'

@app.route('/totalCount', methods=['GET'])
def totalCount():
    return json.dumps(str(getCount()) + '\n') 

@app.route('/avgLegs', methods=['GET'])
def avgLegs():
    return json.dumps(str(getAvgLegs()) + '\n')

@app.route('/queryDates', methods=['GET'])
def queryDates():
    startDate = datetime.datetime.strptime(request.args.get('start'), '%Y-%m-%d %H:%M:%S')
    endDate = datetime.datetime.strptime(request.args.get('end'), '%Y-%m-%d %H:%M:%S')

    return json.dumps(str(getDateQuery(startDate, endDate)) + '\n')

@app.route('/rmDates', methods=['GET'])
def rmDates():
    startDate = datetime.datetime.strptime(request.args.get('start'), '%Y-%m-%d %H:%M:%S')
    endDate = datetime.datetime.strptime(request.args.get('end'), '%Y-%m-%d %H:%M:%S')
    rmDateQuery(startDate, endDate)
    return 'Aniamls remove \n'

@app.route('/returnAnimal', methods=['GET'])
def  returnAnimal():
    uid = request.args.get('uid')
    return json.dumps(str(getAnimal(uid)) + '\n' )

@app.route('/editAnimal', methods=['GET'])
def  editAnimal():
    uid = request.args.get('uid')
    return json.dumps(str(returnEditedAnimal(uid)) + '\n')

def getCount():
    size = rd.dbsize()
    return size

def getAvgLegs():
    totalLegs = 0
    size = rd.dbsize()
    for key in rd.scan_iter():
        totalLegs += int(rd.hget(key, 'legs'))
    return totalLegs/size

def getDateQuery(start, end):
    returnValues = []
    for key in rd.scan_iter():
        if(datetime.datetime.strptime(rd.hget(key, 'created_on'), '%Y-%m-%d %H:%M:%S') > start and datetime.datetime.strptime(rd.hget(key, 'created_on'), '%Y-%m-%d %H:%M:%S') < end):
            returnValues.append(rd.hgetall(key))

    return returnValues

def rmDateQuery(start,end):
    for key in rd.scan_iter():
        if(datetime.datetime.strptime(rd.hget(key, 'created_on')) > start and datetime.datetime.strptime(rd.hget(key, 'created_on')) < end):
            rd.hdel(key)
    
def getAnimal(uid):
    return rd.hgetall(uid)

def returnEditedAnimal(uid):
    return rd.hgetall(uid)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')