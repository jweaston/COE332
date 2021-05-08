# worker.py
import json
import os
import time
from jobs import q, update_job_status, jobdb, propertydb
import requests
from math import sin, cos, sqrt, atan2, radians
import numpy as np
import matplotlib.pyplot as plt

access_key = 'b9cd99a14c67eaaf8dc948ebc27b51c2'
UT_lat = radians(30.2849)
UT_lon = radians(-97.7341)

worker_ip = os.environ.get('WORKER_IP')
if not worker_ip:
    raise Exception()

def latlon_distance(pid):
    query = propertydb.hget(pid, 'Address').decode('utf-8')
    payload = {
        'access_key': access_key,
        'query': query + ' Austin, TX',
    }
    response = requests.get(url='http://api.positionstack.com/v1/forward', params = payload)
    propertydata = response.json().get('data')[0]
    lat = propertydata.get('latitude')
    lon = propertydata.get('longitude')
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
    if(jobdb.hget('job.{}'.format(jid), 'jtype').decode('utf-8') == 'distance'):
        selector = json.loads(jobdb.hget('job.{}'.format(jid), 'selector'))
        pid = selector['id']
        distance = latlon_distance(pid)
        jobdb.hset('job.{}'.format(jid), 'distance', json.dumps(distance))

    if(jobdb.hget('job.{}'.format(jid), 'jtype').decode('utf-8') == 'distvsprice'):
        selector = json.loads(jobdb.hget('job.{}'.format(jid), 'selector'))
        distance_array = np.array([])
        price = np.array([])
        for key in propertydb.keys():
            flag1 = True
            # testList = []
            for arg in selector:
                # testList.append(arg)
                if propertydb.hget(key, arg).decode("utf-8") == str(selector[arg]):
                    continue
                else:
                    flag1 = False
                    break
            if flag1:
                try:
                    dist = latlon_distance(key.decode('utf-8'))
                    if dist > 50:
                        print('distance is too far for property', key.decode('utf-8'))
                        continue
                    else:
                        distance_array = np.insert(distance_array, 0, dist)
                        price = np.insert(price, 0, float(propertydb.hget(key, 'Total Rent').decode('utf-8')[1:].replace(',','')))
                except:
                    print('could not get distance of address in database of property ', key.decode('utf-8'))
                    continue
            else: 
                continue
        plt.scatter(distance_array, price)
        plt.show()
        plt.savefig('{}.png'.format(jid))
        file_bytes = open('{}.png'.format(jid), 'rb').read()
        jobdb.hset('job.{}'.format(jid), 'plot', file_bytes)

        # jobdb.hset('job.{}'.format(jid), 'ratio', json.dumps(distance_array.tolist()))
        # jobdb.hset('job.{}'.format(jid), 'price', json.dumps(price.tolist()))

    if(jobdb.hget('job.{}'.format(jid), 'jtype').decode('utf-8') == 'ratiovsprice'):
        selector = json.loads(jobdb.hget('job.{}'.format(jid), 'selector'))
        ratio = np.array([])
        price = np.array([])
        for key in propertydb.keys():
            flag1 = True
            # testList = []
            for arg in selector:
                # testList.append(arg)
                if propertydb.hget(key, arg).decode("utf-8") == str(selector[arg]):
                    continue
                else:
                    flag1 = False
                    break
            if flag1:
                try:
                    ratio = np.insert(ratio, 0,int(propertydb.hget(key, 'Bed'))/int(propertydb.hget(key,'Bath')))
                    price = np.insert(price, 0, float(propertydb.hget(key, 'Total Rent').decode('utf-8')[1:].replace(',','')))
                except:
                    continue
            else: 
                continue
        plt.scatter(ratio, price)
        plt.show()
        plt.savefig('{}.png'.format(jid))
        file_bytes = open('{}.png'.format(jid), 'rb').read()
        jobdb.hset('job.{}'.format(jid), 'plot', file_bytes)

        # jobdb.hset('job.{}'.format(jid), 'ratio', json.dumps(ratio.tolist()))
        # jobdb.hset('job.{}'.format(jid), 'price', json.dumps(price.tolist()))
    update_job_status(jid, 'complete', worker_ip)
    

# @q.worker
# def execute_job(jid):
#     update_job_status(jid, 'in progress')
#     # todo - replace with real job
#     time.sleep(15)
#     update_job_status(jid, 'complete')