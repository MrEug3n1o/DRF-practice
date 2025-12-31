# Library API Service

This project is a **Library Management REST API** built with **Django** and **Django REST Framework**.  
It allows users to browse books, borrow them, return them, and pay for borrowings, while administrators manage the library inventory and monitor user activity.

---

## Technology Stack

- **Backend:** Django 4.x, Django REST Framework  
- **Database:** PostgreSQL (production), SQLite (development)  
- **Authentication:** Token Authentication  
- **Containerization:** Docker & Docker Compose  

---

# Installation and Run

--- 

## Prerequisites
- Python 3.12+
- Docker

## Installation

### Clone and set up the project

- git clone https://github.com/MrEug3n1o/DRF-practice.git
- cd DRF-practice
- python -m venv venv 
- source venv/bin/activate (windows: venv\Scripts\activate)
- pip install -r requirements.txt

### Configure environment variables

###### Create a file ".env" in the main directory:
```
POSTGRES_DB=airport_db
POSTGRES_USER=airport_user
DB_PASSWORD=your_password
POSTGRES_PORT=5432
POSTGRES_HOST=db
SECRET_KEY=your_secret_key
```

### Run migrations and start server

- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### Docker run
###### Make sure your docker is running
- docker-compose build
- docker-compose up -d

