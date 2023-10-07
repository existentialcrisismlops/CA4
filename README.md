# Prerequisites
Before creating the Docker Compose file, make sure you have the following prerequisites installed on your system:
1. Docker
2. Docker Compose

# Docker Compose Configuration
The docker-compose.yml file defines two services:
app: Represents the web application.
db: Represents the MySQL database.
Images for both services are pulled from Docker Hub.

# Run Docker Compose Stack
Follow these steps to run the My App stack:

Clone this repository to your local machine:

 ```bash
git clone https://github.com/existentialcrisismlops/CA4.git
cd my-app
Start the Docker Compose stack:

bash
Copy code
docker-compose up -d
Wait for the containers to start. You can check the logs to monitor the progress:

bash
Copy code
docker-compose logs -f
To stop the stack and remove the containers when you're done, run:

bash
Copy code
docker-compose down
