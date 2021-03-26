# Homework 3
---
app.py is the python file which continues the routes to access data about the moreau animals. The Dockerfile has instructions when creating the docker image and container. The data_file.json is the data file with 100 moreau animals which the container will access through flask. The consumer_requestor.py file is a consumer which accesses and consumes data from another student's url. The requirements.txt file tells the docker which version of Flask is needed. 

animals\_consumer.py querys the web server for data from the date_file.json about the animals

---
## Downloading and Running Directly
Download the files by getting the files off of github
```
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework03/app.py
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework03/animals_consumer.py
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework03/requirements.txt
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework03/Dockerfiler
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework03/data_file.json
```
## How to Build Image with Dockerfile 
The docker file already contains all the commands needed to build your image. To do so type in the following code:
```
[isp02]$ docker build -t jweaston/webapp:1.0 .
```
Check it has been made by using docker images
```
[isp02]$ docker images
```
## How to the run the Container and use th urls
Run the containr created by the image 
```
[isp02]$ docker run --name "jweaston-hw3-flask" -d -p 5009:5000 jweaston/homework03:1.0
```
Now you should be able to curl into the flask using the container that is running. Check it using the animals route
```
[isp02]$ curl localhost:5009/animals
```

To access animals with a specific head use the url localhost:5009/animals/head?name= '\<nameofhead\>'. Here are some examples.
```
# This will return all of the animals with a snake head
[isp02]$ curl localhost:5009/animals/head?name='snake' 
# This will return all of the animals with a bunny head
[isp02]$ curl localhost:5009/animals/head?name='bunny'
```
To access animals with a certain number of legs use the url localhost:5009/animals/legs?number=\<numberoflegs\>. Here are some examples.
```
# This will return all animals with 6 legs
[isp02]$ curl localhost:5009/animals/legs?number=6
# This will return all animals with 12 legs
[isp02]$ curl localhost:5009/animals/legs?number=12
```
## How to run the Consumer
The consumer file will run some test urls listed above. After the container is running call the consumer with the following line:
```
[isp02]$ python3 animals_consumer.py
```
## Exiting
To stop the container run
```
[isp02]$ docker stop "jweaston-hw3-flask"
```