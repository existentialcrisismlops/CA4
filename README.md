# CA4
task 2:
    # My Flask App  
This repository contains a basic Flask app for login and signup. The files look like:
/CA4
|-- /templates
|   |-- login.html
|   |-- signup.html
|   |-- welcome.html 
|-- app.py 

# How to Test the docker image?
1- You can build the image using : docker build -t existentialcrisismlops/myflaskapp .
2- Then run the image using :  docker run -p 4000:5000 existentialcrisismlops/myflaskapp
3- Visit the link to check the flask application: http://localhost:4000
