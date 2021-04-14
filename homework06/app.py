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
            rd.hmset(animal['uid'], animal)
            index += 1
    return 'Data base initialized \n'
    
@app.route('/reset', methods=['GET'])
def reset():
    with open("../data_file.json", "r") as json_file:
        userdata = json.load(json_file)
        index = 0
        rd.flushdb()
        for animal in userdata:
            rd.hmset(animal['uid'], animal)
            index += 1
    return 'Data base reset \n'

@app.route('/totalCount', methods=['GET'])
def totalCount():
    return json.dumps(str(getCount())) 

@app.route('/avgLegs', methods=['GET'])
def avgLegs():
    return json.dumps(str(getAvgLegs()))

@app.route('/queryDates', methods=['GET'])
def queryDates():
    startDate = datetime.datetime.strptime(request.args.get('start'), '%Y-%m-%d')
    endDate = datetime.datetime.strptime(request.args.get('end'), '%Y-%m-%d')

    return json.dumps(str(getDateQuery(startDate, endDate)))

@app.route('/rmDates', methods=['GET'])
def rmDates():
    startDate = datetime.datetime.strptime(request.args.get('start'), '%Y-%m-%d')
    endDate = datetime.datetime.strptime(request.args.get('end'), '%Y-%m-%d')
    rmDateQuery(startDate, endDate)
    return 'Aniamls remove \n'

@app.route('/returnAnimal', methods=['GET'])
def  returnAnimal():
    uid = request.args.get('uid')
    return json.dumps(str(getAnimal(uid)))

@app.route('/editAnimal', methods=['GET'])
def  editAnimal():
    uid = request.args.get('uid')
    return json.dumps(str(returnEditedAnimal(uid, request.args.lists())))

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
        if(datetime.datetime.strptime(rd.hget(key, 'created_on'), '%Y-%m-%d %H:%M:%S') > start and datetime.datetime.strptime(rd.hget(key, 'created_on'), '%Y-%m-%d %H:%M:%S') < end):
            rd.delete(key)
    
def getAnimal(uid):
    return rd.hgetall(uid)

def returnEditedAnimal(uid, attributeList):
    #testList = []
    for attribute in attributeList:
        #testList.append(attribute[1][0])
        rd.hset(uid, attribute[0], attribute[1][0])
    #return testList
    rd.hset(uid, 'created_on', '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    return rd.hgetall(uid)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')