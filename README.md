<div align="center">

# Pet Shelter Site 
 
<img src="https://github.com/diana-shyrokikh/pet-shelter-site/raw/develop/static/images/logo.svg" height="200">
</div>

<br>

> Let's give a shelter pet a second chance to find a family!

<hr>

## Table of Contents

- [About Project](#about-project)
- [Application functional](#functional)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Accessing the Application](#accessing-the-application)
- [Shutdown](#shutdown)


<hr>

## About Project

Unfortunately, not every cat and dog have a loving family. Someone of them even lost that.
<br>
It is also an important mission to give them back the happiness and faith in goodness that they deserve.
<br>
Whereas shelter volunteers and staff work with a large number of pets, they also need help structuring the large amount of information to make it easier to find new families for pets.

The Pet Shelter Site helps staff save data and help a potential new pet owner choose an pet.

<br>
The main functions of project:

- Help people who wants to find a pet by choosing it on site;
- Manage all pet information;
-  Save information about pet owners to keep in touch with them;
- Allow users get information about their pets, discounts and free vet consultation.

<hr>

## Functional

1. Create staff profiles in admin page (superuser required)
2. Register new user account and pet account (staff required)
3. Add a new cat and dog breed (staff required)
4. Change user's email and phone number
5. Change all pet information (staff required)
6. Search cat or dog who needs family in list by name and breed
7. Search pet in pet list with all info about pet even who founded a family (staff required)
8. Search users by username, first name and last name (staff required)
9. Look extra pet information in pet profile
10. Look user information about pets, discounts in user profile


<hr>

## Technologies

- [Django Official Documentation](https://docs.djangoproject.com/)
Django is a high-level Python Web framework. In this project, it's used to create the backend service. This service builds the Django application and exposes it on port 8080.

<hr>

## Prerequisites

1. Make sure you have Python installed on your system. 
You can check the installation instructions [here for Python](https://www.python.org/downloads/).

<hr>

## Setup

1. Clone the project:
```
git clone https://github.com/diana-shyrokikh/pet-shelter-site.git
```
2. Navigate to the project directory:
```
cd pet-shelter-site
```
3.  Сreate venv and install requirements in it:
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
4. Make migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser to use staff required functions:
```
python manage.py createsuperuser
```
6. Run Django server:
```
python manage.py runserver
```

<hr>

## Accessing the Application

1. Pet Shelter Site is accessible at `http://localhost:8000/`.
2. Django Admin Page is accessible at `http://localhost:8000/admin`.

<hr>

## Shutdown

1. To stop running server use CTRL-BREAK

<hr>

Remember to replace `localhost` with the relevant IP address if you're not accessing these from the same machine where the services are running.

Please make sure to replace placeholders with your actual values in the `.env` file. Also, these instructions are subject to changes in the project, so always refer to the project's README or other documentation for the most accurate information.
