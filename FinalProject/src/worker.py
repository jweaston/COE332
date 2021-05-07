# worker.py
import json
import os
import time
from jobs import q, update_job_status, jobdb, propertydb
import requests
from math import sin, cos, sqrt, atan2, radians

access_key = 'b9cd99a14c67eaaf8dc948ebc27b51c2'
UT_lat = radians(30.2849)
UT_lon = radians(-97.7341)

worker_ip = os.environ.get('WORKER_IP')
if not worker_ip:
    raise Exception()

def latlon_distance(lat,lon):
    R = 6373.0
    lat = radians(lat)
    lon = radians(lon)
    dlon = UT_lon - lon
    dlat = UT_lat - lat
    a = sin(dlat/2)**2 + cos(lat) * cos(UT_lat) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    dist = R * c
    return dist

for jid in q.consume():
    update_job_status(jid, 'in progress', worker_ip)
    if(jobdb.hget('job.{}'.format(jid), 'start').decode('utf-8') == 'distance'):
        pid = jobdb.hget('job.{}'.format(jid), 'end').decode('utf-8')
        query = propertydb.hget(pid, 'Address').decode('utf-8')
        payload = {
            'access_key': access_key,
            'query': query + ' Austin, TX',
        }
        response = requests.get(url='http://api.positionstack.com/v1/forward', params = payload)
        propertydata = response.json().get('data')[0]
        lat = propertydata.get('latitude')
        lon = propertydata.get('longitude')
        distance = latlon_distance(lat,lon)
        jobdb.hset('job.{}'.format(jid), 'distance', json.dumps(distance))
    
    update_job_status(jid, 'complete', worker_ip)

# @q.worker
# def execute_job(jid):
#     update_job_status(jid, 'in progress')
#     # todo - replace with real job
#     time.sleep(15)
#     update_job_status(jid, 'complete')