# API School & Students with logs

## Requirements

Create a simple API using the Django Rest Framework backend application allowing management of schools. Time spent on each feature is covered below. To speed up the development, the project was made using existing code and templates from various projects.

## Step 1 - Django setup and models.

1. Create a Django app, with:
    - Use **Postgres** as a database (10 minutes)
    - Use **Pipenv** as a Python dependency manager. (4 hours, having a hard time to make it work)
    - Environment file (for sensitive information, etc.) (10 minutes)
2. Add models to create the following structure: (10 minutes)
    - Students have a first name, the last name, and a student identification string (20 characters max for each)
    - Schools have a name (20 char max) and a maximum number of students (any positive integer)
    - Each student object must belong to a school object
3. The Django app must be running on Docker. (20 minutes)

**Total:** 4 hours, 50 minutes

## Step 2 - Django Rest Framework (DRF).

1. Add **Django REST framework** library to the project by using Pipenv (1 minute)
2. Enable and use the DRF browsable API for testing things manually. (5 minutes)
3. Design the API according to the specifications below (make sure to test and customize the solution) by creating URLs, views, serializers, tests for all the models so that: (30 minutes)
    - Endpoint `students/` will return all students (GET) and allow student creation (POST)
    - Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
    - Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
    - Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of the choice)
    - Trying to add a student in a full school (maximum number of students reached) will return a DRF error message

**Total:** 36 minutes

## Step 3 - **Django Nested Routers**.

1. Add Django Nested Routers library to the project by using Pipenv (2 minute)
2. Design the API according to the specifications below: (30 minutes)
    - Endpoint /schools/:id/students will return students who belong to school :id (GET)
    - Endpoint /schools/:id/students will allow student creation in the school :id (POST)
    - The nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
    - The nested endpoint will respect the same two last rules of Step 2 too

**Total:** 31 minutes

## Step 4

1. Each change in each of the model instance **must be tracked** with which values were changed (1 hour)
    - Ex: Student with name `A` was edited to be named `B` ****, Student `A` was added to School `X`

**Total:** 1 hour