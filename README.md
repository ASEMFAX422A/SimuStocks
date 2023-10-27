# SimuStocks

SimuStocks is a project that simulates stock-related functionalities. The project is containerized using Docker and orchestrated with Docker Compose.

## Project Structure

- **[docker-compose.yml](https://github.com/ASEMFAX422A/SimuStocks/blob/main/docker-compose.yml)**: This file defines the services required for the project. The main services include:
  - `flask`: A Flask application container.
  - `mongodb`: A MongoDB container for database operations.
  - `webserver`: A web server container.

- **[test.py](https://github.com/ASEMFAX422A/SimuStocks/blob/main/test.py)**: A simple Python script for testing purposes.

## Design and Architecture Patterns

- **Application Factory Pattern**: Used for the dynamic creation of the Flask app instance.
- **Configuration Management**: Separate configuration settings based on the environment (default, development, etc.).
- **Database Configuration**: Use of MongoDB with MongoEngine for database operations.
- **Custom Logging**: Implementation of custom logging where logs are saved to the MongoDB database.

## Setup & Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run `docker-compose up` to start the services.

## Configuration

The `docker-compose.yml` file contains environment variables that can be modified as per your requirements. Ensure to update the MongoDB credentials and other relevant configurations before running the project.

## Instructions

### Running Tests Locally
To run all tests locally, use the following command:
```
python -m unittest discover tests
```
### Building Docker Containers
To build all Docker containers, use:
```
docker-compose up -d --build
```
If you wish to rebuild a specific container, for example `flask`, use:
```
docker-compose up -d --build flask
```
