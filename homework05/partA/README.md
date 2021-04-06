# Part A
---

## Create pod
```
[jweaston@isp02 partA]$ kubectl apply -f hello-pod.yml 
```

## Get pod
```
[jweaston@isp02 partA]$ kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
hello   1/1     Running   0          18s
```

## Check logs
```
[jweaston@isp02 partA]$ kubectl logs hello
Hello, 
```

## Delete pod
```
[jweaston@isp02 partA]$ kubectl delete pods hello
pod "hello" deleted
```