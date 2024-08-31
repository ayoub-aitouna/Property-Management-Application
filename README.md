# Property Management Application

## Overview

This application is a property management system that allows property managers to add new properties, manage tenants, and monitor rent payments. The app is built using Docker for easy deployment and includes Swagger UI for API documentation.

## Prerequisites

To run this project, you will need the following tools installed on your system:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Make** (Linux only): This is usually pre-installed on most Linux distributions. If not, install it using your package manager.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone git@github.com:ayoub-aitouna/Property-Management-Application.git
cd Property-Management-Application
```

### 2. Environment Configuration

Copy the example environment file and fill out the necessary values:

```bash
mv .example.env .env
```

Edit the `.env` file to include your database credentials and other required settings.

### 3. Running the Application

#### On Linux (Using Make)

The `Makefile` simplifies Docker commands. You can use the following commands:

- **Start the application**:
  ```bash
  make up
  ```
- **Stop the application**:
  ```bash
  make down
  ```
- **Run tests**:
  ```bash
  make test
  ```
- **Access the container shell**:
  ```bash
  make shell
  ```
- **View logs**:
  ```bash
  make logs
  ```

#### On Windows (Using PowerShell)

You can manually run the corresponding Docker commands:

- **Start the application**:
  ```powershell
  docker-compose up --build
  ```
- **Stop the application**:
  ```powershell
  docker-compose down --remove-orphans
  ```
- **Run tests**:
  ```powershell
  docker exec backend python3 manage.py test
  ```
- **Access the container shell**:
  ```powershell
  docker exec -it backend zsh
  ```
- **View logs**:
  ```powershell
  docker-compose logs -f
  ```

### 4. Accessing the Application

Once the application is running, you can access the following services:

- **Backend API**: [http://localhost:8000/](http://localhost:8000/)
- **Swagger UI Documentation**: [http://localhost:8000/api/v1/schema/swagger-ui/](http://localhost:8000/api/v1/schema/swagger-ui/)
- **Adminer (Database Management Interface)**: [http://localhost:8080/](http://localhost:8080/)

### 5. Running Tests

You can run unit tests for the application with the following command:

- **Linux**:
  ```bash
  make test
  ```
- **Windows**:
  ```powershell
  docker exec backend python3 manage.py test
  ```

## Additional Notes

- Ensure your Docker and Docker Compose installations are up to date to avoid any compatibility issues.
- The `.env` file should contain all necessary environment variables to connect to the PostgreSQL database.
- For troubleshooting, refer to the Docker logs using the `make logs` command on Linux or the equivalent PowerShell command on Windows.

## Conclusion

This README provides detailed instructions on setting up and running the Property Management Application. If you encounter any issues, please refer to the Docker and Docker Compose documentation or contact me at aitounaayoub05@gmail.com.
