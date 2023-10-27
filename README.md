# SimuStocks

SimuStocks is a project that simulates stock-related functionalities. The project is containerized using Docker and orchestrated with Docker Compose.

## Project Structure

- **[docker-compose.yml](https://github.com/ASEMFAX422A/SimuStocks/blob/main/docker-compose.yml)**: This file defines the services required for the project. The main services include:
  - `flask`: A Flask application container.
  - `mongodb`: A MongoDB container for database operations.
  - `webserver`: A web server container.

- **[test.py](https://github.com/ASEMFAX422A/SimuStocks/blob/main/test.py)**: A simple Python script for testing purposes.

## Setup & Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run `docker-compose up` to start the services.

## Configuration

The `docker-compose.yml` file contains environment variables that can be modified as per your requirements. Ensure to update the MongoDB credentials and other relevant configurations before running the project.

## Time intervals
Following time intervals sawn as functional:
Day = 10 min
Week = 1 hour
Month = 4 hours
Year = 1 day