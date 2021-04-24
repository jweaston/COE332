# Homework 7
---
### Part A:

## Start Deployments for Redis and Flask and the Worker
```
kubectl apply -f deploy/db
kubectl apply -f deploy/api
kubectl apply -f deploy/worker
```

## Create python debug deployment
```
kubectl apply -f deployment-python-debug.yml
```

## Exec into pythong debug deployment
First find the name of the python debug pod
```
[jweaston@isp02 ~]$ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE    IP             NODE                         NOMINATED NODE   READINESS GATES
jweaston-hw7-flask-deployment-5f7c557d97-tcp25    1/1     Running   0          93m    10.244.15.94   c03                          <none>           <none>
jweaston-hw7-redis-deployment-7c7c7495d-kvh24     1/1     Running   0          32m    10.244.15.99   c03                          <none>           <none>
jweaston-hw7-worker-deployment-6d6fb75465-xxlp9   1/1     Running   3          93m    10.244.15.93   c03                          <none>           <none>
py-debug-deployment-5cc8cdd65f-bvhmn              1/1     Running   0          22h    10.244.15.55   c03                          <none>           <none>
py-debug-deployment-5cc8cdd65f-vrlj4              1/1     Running   0          5d4h   10.244.4.226   c02                          <none>           <none>
```
Then exec into it with the following
```
[jweaston@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-bvhmn  -- /bin/bash
root@py-debug-deployment-5cc8cdd65f-bvhmn:/# 
```

## Sending jobs to the Flask app 
Install curl in the container using 
```
pip install curl
```
Then test the Flask app by curling the flask service ip at port 5000 at /jobs
```
root@py-debug-deployment-5cc8cdd65f-bvhmn:/# curl 10.102.186.30:5000/jobs
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```
You can send jobs to the ip
```
root@py-debug-deployment-5cc8cdd65f-bvhmn:/# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "73669359-b65d-484c-9aab-78e5c69c43fd", "status": "submitted", "start": "START TEST", "end": "END TEST"}root@py-debug-deployment-5cc8cdd65f-bvhmn:/#
```

## Check the status in the database
In a separte terminal start an interative python shell
```
root@py-debug-deployment-5cc8cdd65f-vrlj4:/# ipython
Python 3.9.2 (default, Feb 19 2021, 17:11:58) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.22.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```
Import redis and create a database
```
In [1]: import redis

In [2]: rd = redis.StrictRedis(host='10.98.243.144', port=6379, db=0)

In [3]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
   ...: 
{b'id': b'73669359-b65d-484c-9aab-78e5c69c43fd', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'd564e9e9-ad76-4f7a-b330-7df01be62c9f', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'19f39b2c-7bbf-4c1c-be8d-cd8cb0c683e2', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'30b068b3-ed59-43ea-8c72-2d1bfd988381', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'11d6dcfa-f7c1-4d1e-b42e-19fe3c67f3cb', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'dcdd59a4-c50a-4416-96f0-03a669f75dfc', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'e0ac3931-8561-4189-a210-db723a0141fe', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'f86c228e-0aaa-4aed-9150-19cc4645f459', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
```

## Update database
Going back to the other terminal shell try posting another job and run the same command in the python shell
```
root@py-debug-deployment-5cc8cdd65f-bvhmn:/# curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "7ae5e966-3187-494d-8627-831673699edd", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
```
In [4]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
   ...: 
{b'id': b'7ae5e966-3187-494d-8627-831673699edd', b'status': b'in progress', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'19f39b2c-7bbf-4c1c-be8d-cd8cb0c683e2', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'd564e9e9-ad76-4f7a-b330-7df01be62c9f', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'dcdd59a4-c50a-4416-96f0-03a669f75dfc', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'11d6dcfa-f7c1-4d1e-b42e-19fe3c67f3cb', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'30b068b3-ed59-43ea-8c72-2d1bfd988381', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'73669359-b65d-484c-9aab-78e5c69c43fd', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'e0ac3931-8561-4189-a210-db723a0141fe', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'f86c228e-0aaa-4aed-9150-19cc4645f459', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
```
You can now see there is a new job in progress and if we check again after a few seconds
```
In [5]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
   ...: 
{b'id': b'7ae5e966-3187-494d-8627-831673699edd', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'19f39b2c-7bbf-4c1c-be8d-cd8cb0c683e2', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'd564e9e9-ad76-4f7a-b330-7df01be62c9f', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'dcdd59a4-c50a-4416-96f0-03a669f75dfc', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'11d6dcfa-f7c1-4d1e-b42e-19fe3c67f3cb', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'30b068b3-ed59-43ea-8c72-2d1bfd988381', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'73669359-b65d-484c-9aab-78e5c69c43fd', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'e0ac3931-8561-4189-a210-db723a0141fe', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
{b'id': b'f86c228e-0aaa-4aed-9150-19cc4645f459', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST'}
```
The job is now complete

### Part B
Check worker.py and jweaston-hw7-worker-deployment.yml for updates

This what the job database looks like now 
```
In [3]: for key in rd.keys():
   ...:     print(rd.hgetall(key))
   ...: 
{b'id': b'7015db0a-0317-44b7-b780-3079c29463dc', b'status': b'in progress', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
```
We now have a worker ip 

### Part C
If you send 10 curl requests
```
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "b58e1cb0-b1ce-47a6-8d7c-b2b64ce0696c", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "f0e25fb4-acbc-4b2a-9859-85d6ffe57a27", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "4c0409cc-38db-49e2-b3ba-f472a5fa7eee", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "c0e2c58f-441c-4c17-aa1c-72f3cff3a386", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "5c8e96e1-1d0f-493a-8986-2a029ddd9dad", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "5fc5cb7d-d2c3-47bd-a2ab-4cc1127a5bfa", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "b74280fe-8f65-46ce-af83-41d528c3d1ec", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "26399f84-c394-4fc1-a79b-f09290cb2ced", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "cdc2e39d-577e-47f9-8184-f45236bfa928", "status": "submitted", "start": "START TEST", "end": "END TEST"}
curl -X POST -H "content-type: application/json" -d '{"start": "START TEST", "end": "END TEST"}' 10.102.186.30:5000/jobs
{"id": "ebea3fe3-4c19-4571-81d9-77d05e7a5fda", "status": "submitted", "start": "START TEST", "end": "END TEST"}
```
Results in this database
```
In [22]: for key in rd.keys():
    ...:     print(rd.hgetall(key))
    ...: 
{b'id': b'ea743ff7-2a40-4e94-ae59-db311e38c0df', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
{b'id': b'7015db0a-0317-44b7-b780-3079c29463dc', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
{b'id': b'1afe430f-c8e5-41c8-b24d-81b39fe763cc', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.15.138'}
{b'id': b'9aca540c-63b6-4dd7-97bf-a82dc774beb3', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
{b'id': b'724c88a3-1f66-4b17-8473-248ec7385d38', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
{b'id': b'b1fabb0d-7633-4917-9407-8ec931104479', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.15.138'}
{b'id': b'4336a5b0-54c6-4a35-8391-52373d426971', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.15.138'}
{b'id': b'b8ba8377-850b-459b-a2cf-5999f24641ad', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.15.138'}
{b'id': b'cf627dd9-e4bc-4593-b3a5-a3e115a9858a', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.7.118'}
{b'id': b'798244a1-1bf2-4310-bd41-1587f21ad7b6', b'status': b'complete', b'start': b'START TEST', b'end': b'END TEST', b'worker_ip': b'10.244.15.138'}
```
Each worker did 5 jobs