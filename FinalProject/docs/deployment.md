### Flask API Front End

Mapped to port 5009 on ISP. 
Deploying on the ISP machine:
```
make clean-api     # remove api container
make test-api      # build dockerfile and start api container
```
### Redis DB
The Redis db configuration is located at ./data/redis.conf. It is mounted
inside the container at /data/ when doing `docker run`. It is customized to have
a more frequent save interval and bind to 0.0.0.0. It uses the default Redis
port inside the container (6379), and is mapped to 6389 on ISP 
Deploying on the ISP machine:
```
make clean-db     # remove db container
make test-db      # build dockerfile and start db container
```

### Worker 
Deploying on the ISP machine:
```
make clean-wrk    # remove worker container
make test-wrk     # build dockerfile and start worker container
```
### Docker Bridge Network

The Makefile assumes that there is a bridge network called:
`${NSPACE}-network-test`, where ${NSPACE} is something unique, like your
username, as defined in the top of the Makefile. To create it, do, e.g.:

```
docker network create jweaston-network-test
```
### Compose

The above commands are useful for launching and testing individual parts of
the app. Docker-compose targets have also been written into the Makefile to
test orchestration of all components as a unit. Before doing this, though, it
is a good idea to clean up all of the test containers:

```
make clean-all 
```

The following will pull the version of containers from Docker Hub that are
specified in the top of the Makefile as 'VER', and it will launch each of the
three services one by one. There is a slight (sleep 5) before launching the
worker because the worker will terminate with a failure if it cannot connect
to the redis db.

```
make compose-up
```

### Kubernetes

Currently supporting a Kubernetes test and prod environment. Manual changes needed
in the yml files for each include the image tag (in all the deployment files), and
the redis service IP in the api / wrk deployment files. Once those changes are made,
you can do this to launch everything:

```
kubectl apply -f kubernetes/test/
kubectl apply -f kubernetes/prod/
```

Easiest way to test for now is to kubectl exec into the python debug pod and curl
whatever routes. Still need to set up nodeport service to see it from the outside
world.


To update to a new version of the containers on Docker Hub, follow these steps:

```
# first edit the three deployment yml files to point to the new image tag.

kubectl apply -f kubernetes/test/*deployment.yml

# check to make sure pods terminate and restart as appropriate, curl routes
```

If that works, do the same thing for prod.

To tear down all three services:

```
make compose-down
```