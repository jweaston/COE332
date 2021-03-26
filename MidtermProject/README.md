# Midterm
---
app.py is the python file which continues the routes to access data about the moreau animals. The Dockerfile has instructions when creating the docker image and container. The data_file.json is the data file with 100 moreau animals which the container will access through flask. The consumer_requestor.py file is a consumer which accesses and consumes data from another student's url. The requirements.txt file tells the docker which version of Flask is needed. 

animals\_consumer.py querys the web server for data from the date_file.json about the animals

---

## How to the run the Container and use th urls
The docker-compose file already contains all the commands needed to build your image and run the container. To do so type in the following code:
```
[isp02]$ docker-compose -p jweaston up
```
Check it has been made by using docker ps
```
[isp02]$ docker ps
```
Now you should be able to curl into the flask using the container that is running. Check it using the animals route
```
[isp02]$ curl localhost:5009
```
This should initialize the database

To access specific animal you can use it's uid with the route localhost:5009/returnAnimal?uid= '\<uid of animal\>'. Here are some examples.
```
[isp02]$ curl localhost:5009/returnAnimal?uid=6f7efec6-c15e-4f98-b5d3-ce3db4e2d7de 
[isp02]$ curl localhost:5009/returnAnimal?uid=d07b0333-1115-4c71-b230-6d25a6d7c8b3
```
To access edit animals with a certain uid use the url localhost:5009/editAnimal?uid=\<numberoflegs\>&\<attribute\>=\<value\>. Here are some examples.
```
[isp02]$ curl localhost:5009/editAnimal?uid=eb96bc93-b1b7-40db-ba36-fd8ba89dbb9c&body=lion-snake
[isp02]$ curl localhost:5009/editAnimal?uid=d07b0333-1115-4c71-b230-6d25a6d7c8b3c&head=bird
```
To get the total number of animals use the url localhost:5009/totalCount. 
```
[isp02]$ curl localhost:5009/totalCount
```

To get the average number of legs of all animals use the url localhost:5009/avgLegs. 
```
[isp02]$ curl localhost:5009/avgLegs
```

To query a date range use the url localhost:5009/queryDates?start=\<startDate in YYYY-MM-DD format\>&\end=\<endDate in YYYY-MM-DD format\>. 
```
[isp02]$ curl localhost:5009/queryDates?start=2021-03-23&end=2021-03-24 
```

To remove animals created in a date range use the url localhost:5009/rmDates?start=\<startDate in YYYY-MM-DD format\>&\end=\<endDate in YYYY-MM-DD format\>. 
```
[isp02]$ curl localhost:5009/rmDates?start=2021-03-23&end=2021-03-24 
```

## How to run the Consumer
The consumer file will run some test urls listed above. After the container is running call the consumer with the following line:
```
[isp02]$ python3 animals_requestor.py
```
## Exiting
To stop the container press ctrl+c to end the container
