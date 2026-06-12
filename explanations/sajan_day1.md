Day 1 - Environment Setup and Project Initialization

Objective

The objective of Day 1 was to set up the development environment, create the GitHub repository, initialize the Flask project structure, and ensure that the application runs successfully on the local machine.

⸻

Software and Libraries Installed

Python

Python is the primary programming language used for the AppShield project.

Command used:

python3 --version

Purpose:

* Backend development
* Security analysis modules
* API integration
* Database operations

Flask

Flask is a lightweight Python web framework used to build the backend application.

Installation:

pip install flask

Purpose:

* Create routes
* Handle HTTP requests and responses
* Serve HTML pages
* Connect frontend and backend

Flask-Login

Installation:

pip install flask-login

Purpose:

* User authentication
* Session management
* Route protection

Flask-SQLAlchemy

Installation:

pip install flask-sqlalchemy

Purpose:

* Database management
* ORM functionality
* Table creation and relationships

Flask-Bcrypt

Installation:

pip install flask-bcrypt

Purpose:

* Password hashing
* Secure credential storage

Bandit

Installation:

pip install bandit

Purpose:

* Static Application Security Testing (SAST)
* Detect insecure coding practices in Python files

Requests

Installation:

pip install requests

Purpose:

* Send HTTP requests
* Perform web security analysis

ReportLab

Installation:

pip install reportlab

Purpose:

* Generate PDF security reports

Google Generative AI

Installation:

pip install google-generativeai

Purpose:

* AI-powered vulnerability explanations
* Security remediation suggestions

⸻

Project Folder Structure

Created the following structure:

appshield/
│
├── app/
│   ├── auth/
│   ├── scanner/
│   ├── ai/
│   ├── reports/
│   ├── templates/
│   └── static/
│
├── tests/
├── explanations/
├── run.py
├── config.py
├── requirements.txt
└── .gitignore

Purpose:

This structure separates project modules and keeps the application organized.

⸻

Virtual Environment

Created a virtual environment:

python3 -m venv venv

Activated:

source venv/bin/activate

Purpose:

A virtual environment isolates project dependencies from the system Python installation.

⸻

GitHub Repository Setup

Initialized Git:

git init

Connected repository:

git remote add origin <repository-url>

First commit:

git add .
git commit -m "Initial project structure"

Purpose:

Version control and collaboration.

⸻

Flask Application Factory Pattern

File:

app/__init__.py

Main Function:

create_app()

Purpose:

Creates and configures the Flask application instance.

Benefits:

* Modular architecture
* Easier testing
* Better scalability
* Industry standard Flask structure

⸻

Application Entry Point

File:

run.py

Purpose:

Starts the Flask server.

Execution:

python run.py

Result:

Application successfully launched on:

http://127.0.0.1:5000

⸻

Outcome of Day 1

Successfully completed:

* Environment setup
* Package installation
* GitHub repository creation
* Flask project structure creation
* Flask application initialization
* First successful application run
* Initial project commit