# School API

## Overview

An API to do basic CRUD function of school and student data. This repository includes the API, documentation, some unit tests, and a Changelog tracker. It was made using Django and Django Rest Framework. This API was made to answer some problem statement [here](./PROBLEM.md).

## How to run

### Use Docker (Recommended)

- Get into the root directory

- Make sure that Docker is installed, type `docker -v`

- Build the Docker Image, type `docker build . && docker-compose build --no-cache`

- Configure the .env file, the file template is provided

- Run the container, type `docker-compose up`

- Docker Desktop is recommended to ease things up

### Using Virtual Environment

- Install the dependencies by either using pip or pipenv. Virtual Environment is optional, but recommended.

- Make migration by running `python manage.py makemigrations` and run the migration by `python manage.py migrate`, by default the database will get connected to sqlite3.

- Run unit test and see code coverage in htmlcov/index.html, type `pytest --cov=api --cov-report=html`. This can be done manually to see the code coverage even though you're using Docker

- Install and run Redis Server (Or set USE_CACHE to False in `core/settings.py`)

- Run the server `python manage.py runserver`

## REST API

The followings are the short documentation of the API. You can also use DRF provided UI to check it out by visiting each endpoints.

### Schools

- Show School List: `GET /api/schools/`
    - Description:
        - Show a list of schools distributed into certain numbers of items per page
        - Page size can be configured in Django config
    - Parameters
        - page: for pagination purpose
    - Response (200)  
        ```json
        {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "name": "Red Horse",
                    "capacity": 300,
                    "address": "Red Street",
                    "phone_number": "0813213"
                },
                {
                    "id": 2,
                    "name": "Blue Sky School",
                    "capacity": 600,
                    "address": "Blue Street",
                    "phone_number": "08128384"
                }
            ]
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'GET' 'http://<URL>/api/schools/' -H 'accept: application/json'
        ```

- Create a School: `POST /api/schools/`
    - Description
        - Insert a new school data
    - Request Data
        - name - School name (string)
        - capacity - The capacity of student for that school (integer)
        - Address - The school address (string)
        - phone_number - The school phone_number (string)
        ```json
        {
            "name": "Yellow High School",
            "capacity": 500,
            "address": "Yellow Street",
            "phone_number": "08123123"
        }
        ```
    - Response (201)  
        ```json
        {
            "id": 3,
            "name": "Yellow High School",
            "capacity": 500,
            "address": "Yellow Street",
            "phone_number": "08123123"
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/schools/' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "name": "Yellow High School",
            "capacity": 500,
            "address": "Yellow Street",
            "phone_number": "08123123"
        }'
        ```

- Update a School Data: `PUT/PATCH /api/schools/<school_id>/`
    - Description
        - Update an existing school data
    - Request Data
        - name - School name (string)
        - capacity - The capacity of student for that school (integer)
        - Address - The school address (string)
        - phone_number - The school phone_number (string)
        ```json
        {
            "name": "Yellow High School",
            "capacity": 500,
            "address": "66th Yellow Street",
            "phone_number": "08123123"
        }
        ```
    - Response (204)
        ```json
        {
            "id": 3,
            "name": "Yellow High School",
            "capacity": 500,
            "address": "66th Yellow Street",
            "phone_number": "08123123"
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/schools/<SCHOOL_ID>/' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "name": "Yellow High School",
            "capacity": 500,
            "address": "66th Yellow Street",
            "phone_number": "08123123"
        }'
        ```

- Delete a School Data: `DELETE /api/schools/<school_id>/`
    - Description
        - Delete an existing school data
    - Request Data
        - None
    - Response (204)
        ```json
        No-Content
        ```
    - cURL Import
        ```cURL
        curl -X 'DELETE' 'http://<URL>/api/schools/<SCHOOL_ID>/' -H 'accept: application/json' \
        -H 'Content-Type: application/json'
        ```

### Students

- Show Student List: `GET /api/students/`
    - Description:
        - Show a list of students distributed into certain numbers of items per page
        - Page size can be configured in Django config
    - Parameters
        - page: for pagination purpose
    - Response (200)  
        ```json
        {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "first_name": "Mark",
                    "last_name": "White",
                    "school": 1,
                    "identification": "dfebb370-c26f-4c53-9bc9-599948288909"
                },
                {
                    "id": 2,
                    "first_name": "Andre",
                    "last_name": "Black",
                    "school": 1,
                    "identification": "958ebdc3-865d-4836-8c7c-3c0fbc73219a"
                }
            ]
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'GET' 'http://<URL>/api/students/?page=1' -H 'accept: application/json'
        ```

- Create a Student Data: `POST /api/students/`
    - Description
        - Insert a new student data
    - Request Data
        - first_name - Student first name (string)
        - last_name - Student last name (string)
        - school - An ID of a school
        ```json
        {
            "first_name": "Paul",
            "last_name": "Parker",
            "school": 1
        }
        ```
    - Response (201)  
        ```json
        {
            "id": 3,
            "first_name": "Paul",
            "last_name": "Parker",
            "school": 1,
            "identification": "46d45433-5780-44ef-ba9e-6b7af552b09c"
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/students/' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "first_name": "Paul",
            "last_name": "Parker",
            "school": 1
        }'
        ```

- Update a Student Data: `PUT/PATCH /api/students/<student_id>/`
    - Description
        - Update an existing student data
    - Request Data
        - id - id of the student
        - first_name - Student first name (string)
        - last_name - Student last name (string)
        - school - An ID of a school
        ```json
        {
            "first_name": "Paul",
            "last_name": "Newman",
            "school": 1
        }
        ```
    - Response (200)  
        ```json
        {
            "id": 3,
            "first_name": "Paul",
            "last_name": "Newman",
            "school": 1,
            "identification": "46d45433-5780-44ef-ba9e-6b7af552b09c"
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/students/<STUDENT_ID>' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "id": 3,
            "first_name": "Paul",
            "last_name": "Parker",
            "school": 1
        }'
        ```

- Delete a Student Data: `DELETE /api/students/<student_id>/`
    - Description
        - Delete an existing student data
    - Request Data
        - None
    - Response (204)
        ```json
        No-Content
        ```
    - cURL Import
        ```cURL
        curl -X 'DELETE' 'http://<URL>/api/students/<STUDENT_ID>/' -H 'accept: application/json' \
        -H 'Content-Type: application/json'
        ```

### Nested Routers

- Show Student List based on School: `GET /api/schools/<SCHOOL_ID>/students/`
    - Description:
        - Show a list of students distributed into certain numbers of items per page
        - Page size can be configured in Django config
    - Parameters
        - page: for pagination purpose
    - Response (200)  
        ```json
        {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "first_name": "Mark",
                    "last_name": "White",
                    "school": 1,
                    "identification": "dfebb370-c26f-4c53-9bc9-599948288909"
                },
                {
                    "id": 2,
                    "first_name": "Andre",
                    "last_name": "Black",
                    "school": 1,
                    "identification": "958ebdc3-865d-4836-8c7c-3c0fbc73219a"
                }
            ]
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'GET' 'http://<URL>/api/students/?page=1' -H 'accept: application/json'
        ```

- Create a Student Data based on School ID: `POST /api/schools/<SCHOOL_ID>/students/`
    - Description
        - Insert a new student data
        - The student will be automatically assigned to the school ID when created
    - Request Data
        - first_name - Student first name (string)
        - last_name - Student last name (string)
        - school - An ID of a school
        ```json
        {
            "first_name": "Michael",
            "last_name": "Walker"
        }
        ```
    - Response (201)  
        ```json
        {
            "id": 4,
            "first_name": "Michael",
            "last_name": "Walker",
            "school": 1,
            "identification": "61b2415f-0fbe-464f-9618-e00ff89122e6""
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/schools/<SCHOOL_ID>/students/' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "first_name": "Paul",
            "last_name": "Parker"
        }'
        ```

- Update a student Data: `PUT/PATCH /api/schools/<SCHOOL_ID>/students/<STUDENT_ID>/`
    - Description
        - Update an existing student data
    - Request Data
        - id - id of the student
        - first_name - Student first name (string)
        - last_name - Student last name (string)
        - school - An ID of a school
        ```json
        {
            "first_name": "Paul",
            "last_name": "Newman",
        }
        ```
    - Response (200)  
        ```json
        {
            "id": 3,
            "first_name": "Paul",
            "last_name": "Newman",
            "school": 1,
            "identification": "46d45433-5780-44ef-ba9e-6b7af552b09c"
        }
        ```
    - cURL Import
        ```cURL
        curl -X 'POST' 'http://<URL>/api/schools/<SCHOOL_ID>/students/' -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "first_name": "Paul",
            "last_name": "Newman"
        }'
        ```

- Delete a Student Data: `DELETE api/schools/<SCHOOL_ID>/students/<STUDENT_ID>/`
    - Description
        - Delete an existing student data
    - Request Data
        - None
    - Response (204)
        ```json
        No-Content
        ```
    - cURL Import
        ```cURL
        curl -X 'DELETE' 'http://<URL>/api/schools/<SCHOOL_ID>/students/' -H 'accept: application/json' \
        -H 'Content-Type: application/json'
        ```


## Author

### Bayu Sasrabau Setiahartono

[LinkedIn](https://linkedin.com/in/setiahartono)