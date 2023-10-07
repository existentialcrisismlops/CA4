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
   
   ```shell
   git clone https://github.com/technotrio/CA4.git
   cd my-app
Start the Docker Compose stack:

shell
Copy code
docker-compose up -d
Wait for the containers to start. You can check the logs to monitor the progress:

shell
Copy code
docker-compose logs -f
To stop the stack and remove the containers when you're done, run:

shell
Copy code
docker-compose down
