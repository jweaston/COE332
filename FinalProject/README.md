# Final
---
By James Easton
This is a repository for my COE332 final project. It consistis of a REST API that interface with a datebase of properties near
campus. It contains full CRUD opertaions to interact with the database as well as analysis of the data. 

This includes: 
    1) Getting the distance to campus of any of the properties in km, 
    2) Getting the ratio of bed/bathrooms to the price and plotting its, 
    3) Plotting the distance to campus vs price for the properties.

## Flask API Front End
On the IP https://isp-proxy.tacc.utexas.edu/jweaston/ all the routes can be found for the api
```
curl https://isp-proxy.tacc.utexas.edu/jweaston/ -k
    Routes:

    /               list routes
    /reloaddb       reloads property database
    /run            (GET) route instructions
    /run            (POST) submit job
    /properties     get instructions for route 
    /jobs           get list of jobs
    /jobs/<UUID>    get job results
```
Doing a get request to any of these routes will give you more information on what they do as well as examples.
Also by going to http://jweaston99.myddns.me/COE332_FinalProject.php a web interface as been create to interact with the Flask API.