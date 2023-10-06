# CA4

1. Open a terminal and navigate to the project directory containing the Dockerfile and init.js script. 
2. Build the Docker image for the MongoDB database service:
    docker build -t my-mongodb-image .
3. Start a Docker container with the MongoDB database service using the following command:
    docker run -d --name my-mongodb-container -p 27017:27017 my-mongodb-image
4. The MongoDB database service will now be running in a Docker container.
5. The init.js script is automatically executed when the container starts. It initializes the MongoDB collections and inserts sample data.
