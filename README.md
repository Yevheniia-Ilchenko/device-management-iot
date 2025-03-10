# Device Management IoT Application

This is an IoT device management application built with Aiohttp and Peewee ORM. It provides APIs to create, read, update, and delete devices, locations, and users.

## Requirements

- Docker
- Docker Compose

## Getting Started

Follow these instructions to get the project up and running on your local machine.

# Installation

**Clone the repository**

```
  git clone https://github.com/Yevheniia-Ilchenko/device-management-iot
  python3 -m venv venv
  venv\Scripts\activate (on Windows)
  source venv/bin/activate (on macOS)
  pip install -r requirements.txt
```
**Set up environment variables**

Create  **.env** file in the root directory and add the following content:
```
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

# Running the Application

## Running the Application via Docker Hub
You can also pull and run the Docker image from Docker Hub.

Login into the Docker:
```
docker login
```

Pull the Image
```
docker pull evgeniiailchenko/device-management-iot-app

```
### Run the Container



## Running the Application via Docker compose
**Build and start the containers**

Use Docker Compose to build and start the containers:
```
docker-compose up --build
```
This command will:

 - Build the Docker images for the application and the database.
 - Start the containers.
 - Run the database migrations to create the necessary tables. 

## .env file
Open file .env.sample and change environment variables to yours. Also rename file extension to .env

## Running on local server
- Install PostgreSQL, create DB and User
- Connect DB
- Run:
```
python models.py
```




The application will be running at http://localhost:8000. You can interact with the API using tools like **_Postman_** or CURL.

API Endpoints
Create a User

**URL:** `POST /users`

Request Body:
```
{
  "name": "Test User",
  "email": "test@example.com",
  "password": "password"
}

```
Create a Location

**URL:** `POST /locations`

Request Body:
```

{
  "name": "Test Location"
}
```

Create a Device

**URL:**  `POST /devices`

Request Body:
```
{
  "name": "Test Device",
  "type": "Type A",
  "login": "testlogin",
  "password": "testpassword",
  "location_id": 1,
  "api_user_id": 1
}
```
- **Get All Devices**
  - **URL:** `GET /devices`
  - **Response:** List of all devices

- **Get a Device by ID**
  - **URL:** `GET /devices/{id}`
  - **Response:** Details of the requested device

- **Update a Device**
  - **URL:** `PATCH /devices/{id}`
  - **Request Body:** Fields to be updated for the device
  - **Response:** Details of the updated device

- **Delete a Device**
  - **URL:** `DELETE /devices/{id}`
  - **Response:** Confirmation message of the device deletion

**Logging**

The application uses Python's built-in logging module to log various actions and errors. Logs include:

- Creation, retrieval, updating, and deletion of devices.
- Creation of users and locations.
- Errors encountered during these operations.
