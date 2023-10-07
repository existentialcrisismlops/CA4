# My App Docker Compose README

## Prerequisites
Ensure you have the following installed:
1. Docker
2. Docker Compose

## Docker Compose Configuration
The `docker-compose.yml` file defines two services:
- `app`: Represents the web application.
- `db`: Represents the MySQL database.

Images for both services are pulled from Docker Hub.

## Running the Docker Compose Stack

Follow these steps to run the My App stack:

1. Clone this repository to your local machine:
   
   ```shell
   git clone https://github.com/existentialcrisismlops/CA4.git
   cd my-app
2. Start the Docker Compose stack:

  ```shell
  docker-compose up -d
3. Wait for the containers to start. You can check the logs to monitor the progress:

  ```shell
  docker-compose logs -f
4. To stop the stack and remove the containers when you're done, run:

  ```shell
  docker-compose down
