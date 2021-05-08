# Flask API Front End
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