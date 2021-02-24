# Homework 2
---
generate\_animals.py randomly generates 20 animal hybrids and stores them in a json that lists out their features.It takes a parameter that is the name of the file you wish to write to.  

read\_animals.py prints out 1 randomly selected animal from the json file made using. It takes the file name as a parameter when called. It then will choose to random parents from the list and will breed to make a child, which combines the heads and bodies of the parents and has the average number of arms and legs from the parents and the number of tails is the sum of the number of arms and legs.

---
## Downloading and Running Directly
Download the files by getting the files off of github
```
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework02/generate_animals.py
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework02/read_animals.py
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework02/test_read_animals.py
[isp02]$ wget https://raw.githubusercontent.com/jweaston/COE332/main/homework02/Dockerfile
```
First generate\_animals.py nameOfFile.json and read\_animals.py naomeOfFile.json (and also test\_read\_animals.py if you want)
```
[isp02]$ chmod +rx generate_animals.py
[isp02]$ chmod +rx read_animals.py
[isp02]$ chmod +rx test_read_animals.py
```
Then to run directly without making a container
```
[isp02]$ python3 generate_animals.py animals.json
[isp02]$ python3 read_animals.py animals.json
[isp02]$ python3 test_read_animals.py
```
## How to Build Image with Dockerfile 
The docker file already contains all the commands needed to build your image. To do so type in the following code:
```
[isp02]$ docker build -t jweaston/json-parser:1.0 .
```
Check it has been made by using docker images
```
[isp02]$ docker images
```
## How to the run the scripts in the Container
Run the containr created by the image 
```
[isp02]$ docker run --rm -it jweaston/json-parser:1.0 /bin/bash
```
The files will be in the container, run them like you would directly
```
[root@p6cf05afdfdc /]# generate_animals.py animals.json
[root@p6cf05afdfdc /]# read_animals.py animals.json
```
## How to run the unit test 
Leave the container and run the test\_read\_animals.py file
```
[isp02]$ python3 test_read_animals.py
```
