# Part C
---

## Create deployment
```
[jweaston@isp02 partC]$ kubectl apply -f deployment-hello.yml 
deployment.apps/hello created
```

## Get pods
```
[jweaston@isp02 partC]$ kubectl get pods 
NAME                    READY   STATUS    RESTARTS   AGE
hello-b5887866f-pv42c   1/1     Running   0          36s
hello-b5887866f-sxjvb   1/1     Running   0          36s
hello-b5887866f-w76tj   1/1     Running   0          36s
```

## Get logs
```
[jweaston@isp02 partC]$ kubectl get pods 
NAME                    READY   STATUS    RESTARTS   AGE
hello-b5887866f-pv42c   1/1     Running   0          36s
hello-b5887866f-sxjvb   1/1     Running   0          36s
hello-b5887866f-w76tj   1/1     Running   0          36s
[jweaston@isp02 partC]$ kubectl logs hello-b5887866f-pv42c
Hello, James from IP 10.244.6.135
[jweaston@isp02 partC]$ kubectl logs hello-b5887866f-sxjvb
Hello, James from IP 10.244.3.70
[jweaston@isp02 partC]$ kubectl logs hello-b5887866f-w76tj
Hello, James from IP 10.244.10.243
[jweaston@isp02 partC]$ 
```