Day 2 - Database Models and Authentication System

Objective

The objective of Day 2 was to build the database layer, create application models, implement user authentication, and protect routes using Flask-Login.

⸻

Database Configuration

File:

config.py

Configuration:

SQLALCHEMY_DATABASE_URI = "sqlite:///appshield.db"

Purpose:

Creates a local SQLite database for storing application data.

⸻

Flask Extensions

SQLAlchemy

Initialized in:

app/__init__.py

Code:

db = SQLAlchemy()

Purpose:

Provides Object Relational Mapping (ORM) functionality.

Benefits:

* No need to write raw SQL queries
* Easier database management
* Python-based table definitions

⸻

LoginManager

Code:

login_manager = LoginManager()

Purpose:

Handles user sessions and authentication.

Features:

* Login protection
* Session persistence
* User loading

⸻

Bcrypt

Code:

bcrypt = Bcrypt()

Purpose:

Secure password hashing.

⸻

Database Models

File:

app/auth/models.py

User Model

Purpose:

Stores application users.

Fields:

Field	Description
id	Primary key
email	User email
password_hash	Encrypted password
created_at	Account creation date

Relationship:

One User can have multiple Scans.

⸻

Scan Model

Purpose:

Stores scan information.

Fields:

Field	Description
id	Primary key
user_id	Owner of scan
scan_type	static/web/both
target	File or URL scanned
risk_score	Security score
created_at	Scan timestamp

Relationship:

One Scan can contain multiple Findings.

⸻

Finding Model

Purpose:

Stores vulnerabilities detected during scans.

Fields:

Field	Description
id	Primary key
scan_id	Related scan
title	Finding title
description	Vulnerability details
severity	Criticality level
owasp_id	OWASP mapping
ai_explanation	AI-generated explanation

⸻

Authentication Routes

File:

app/auth/routes.py

Register Route

Endpoint:

/register

Methods:

GET
POST

Purpose:

Create a new user account.

Process:

1. Receive email and password.
2. Check if user already exists.
3. Hash password using bcrypt.
4. Save user to database.
5. Redirect to login page.

⸻

Login Route

Endpoint:

/login

Methods:

GET
POST

Purpose:

Authenticate existing users.

Process:

1. Receive credentials.
2. Search database for email.
3. Verify password hash.
4. Create login session.
5. Redirect to dashboard.

⸻

Logout Route

Endpoint:

/logout

Purpose:

Terminate user session.

Process:

1. Remove active session.
2. Redirect user to login page.

⸻

User Loader Function

Code:

@login_manager.user_loader
def load_user(user_id):

Purpose:

Loads a user from the database using the stored session ID.

Why Needed:

Flask-Login must know how to retrieve the current user for each request.

⸻

Route Protection

Code:

@login_required

Purpose:

Prevents unauthorized access to protected pages.

Example:

@app.route("/dashboard")
@login_required

Result:

Users must login before accessing the dashboard.

⸻

Password Security

Passwords are never stored directly.

Example:

User enters:

123456

Stored in database:

$2b$12$A6TOHuIqnx...

Benefits:

* Prevents password theft
* Industry-standard security practice

⸻

Testing Performed

Successfully verified:

* User registration
* Duplicate user prevention
* Password hashing
* User login
* User logout
* Session creation
* Dashboard protection
* Database record creation

⸻

Outcome of Day 2

Successfully completed:

* Database setup
* User model creation
* Scan model creation
* Finding model creation
* Authentication system
* Login/logout functionality
* Session management
* Protected routes
* Password hashing
* SQLite integration