# Homework 6
---

## Start Deployments for Redis and Flask
```
kubectl apply -f jweaston-test-redis-deployment.yml
kubectl apply -f jweaston-test-reids-service.yml
kubectl apply -f jweaston-test-flask-deployment.yml
kubectl apply -f jweaston-test-flask-service.yml
```

## Create python debug deployment
```
kubectl apply -f deployment-python-debug.yml

```

## Exec into pythong debug deployment
First find the name of the python debug pod
```
[jweaston@isp02 homework06]$ kubectl get pods -o wide
NAME                                              READY   STATUS    RESTARTS   AGE     IP              NODE   NOMINATED NODE   READINESS GATES
jweaston-test-flask-deployment-69dd847f6d-lg592   1/1     Running   0          5m52s   10.244.13.226   c11    <none>           <none>
jweaston-test-redis-deployment-8964b8945-49hmq    1/1     Running   0          24h     10.244.13.132   c11    <none>           <none>
<mark>py-debug-deployment-5cc8cdd65f-7qzjl</mark>              1/1     Running   0          24h     10.244.13.131   c11    <none>           <none>
```
Then exec into it with the following
```
[jweaston@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-7qzjl -- /bin/bash
root@py-debug-deployment-5cc8cdd65f-7qzjl:/# 
```

## Test Flask app 
Install curl in the container using 
```
pip install curl
```
Then test the Flask app by curling the ip at port 5000
```
root@py-debug-deployment-5cc8cdd65f-7qzjl:/# curl 10.244.13.226:5000
Data base initialized 
```
You can now run routes on that ip 
```
root@py-debug-deployment-5cc8cdd65f-7qzjl:/# curl 10.244.13.226:5000/avgLegs
"6"root@py-debug-deployment-5cc8cdd65f-7qzjl:/# 
```