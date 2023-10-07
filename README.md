# CA4
# Db
1. Open a terminal and navigate to the project directory containing the Dockerfile and init.js script. 
2. Build the Docker image for the MongoDB database service:
    docker build -t my-mongodb-image .
3. Start a Docker container with the MongoDB database service using the following command:
    docker run -d --name my-mongodb-container -p 27017:27017 my-mongodb-image
4. The MongoDB database service will now be running in a Docker container.
5. The init.js script is automatically executed when the container starts. It initializes the MongoDB collections and inserts sample data.

# My App Docker Compose README

## Prerequisites
Ensure you have the following installed:
- Docker
- Docker Compose

## Docker Compose Configuration
The `docker-compose.yml` file defines two services:
- `app`: Represents the web application.
- `db`: Represents the MySQL database.

Images for both services are pulled from Docker Hub.

## Running the Docker Compose Stack

Follow these steps to run the My App stack:

1. Clone this repository to your local machine:
   
   git clone https://github.com/existentialcrisismlops/CA4.git


   cd my-app

3. Start the Docker Compose stack:
   
   docker-compose up -d

5. Wait for the containers to start. You can check the logs to monitor the progress:
   
   docker-compose logs -f

7. To stop the stack and remove the containers when you're done, run:
   
   docker-compose down

# Db
1. Open a terminal and navigate to the project directory containing the Dockerfile and init.js script. 
2. Build the Docker image for the MongoDB database service:
    docker build -t my-mongodb-image .
3. Start a Docker container with the MongoDB database service using the following command:
    docker run -d --name my-mongodb-container -p 27017:27017 my-mongodb-image
4. The MongoDB database service will now be running in a Docker container.
5. The init.js script is automatically executed when the container starts. It initializes the MongoDB collections and inserts sample data.
