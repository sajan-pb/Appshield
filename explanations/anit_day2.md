Day 2 - Authentication Frontend Development

 Objective

The objective of Day 2 was to build the frontend authentication pages, connect them with the backend authentication routes, test the complete authentication flow, and understand SQL Injection concepts.

---

 GitHub Synchronization

Pulled the latest changes from the repository to obtain the authentication backend developed by Sajan.

Purpose:

* Synchronize project files
* Ensure compatibility between frontend and backend modules

---

 Authentication Templates

Created:

* login.html
* register.html

Features:

* Email input field
* Password input field
* Submit button
* Navigation links between Login and Register pages

---

 CSS Styling

Created a shared stylesheet:

static/css/style.css


---
 Backend Route Integration

Connected the frontend forms to Flask backend routes using plain HTML POST requests.

Register form:
<form method="POST" action="/register">

Login form:
<form method="POST" action="/login">

Purpose:

Allow users to submit authentication data to the backend.

---
 Authentication Flow Testing

Successfully tested the complete authentication process.

Workflow:
Register
↓

Login

↓

Session Creation

↓

Dashboard

Verified:

* User registration
* Password hashing
* User login
* Session creation
* Dashboard redirection

---

 SQL Injection (OWASP A03)

SQL Injection occurs when user input is inserted directly into SQL queries, allowing attackers to manipulate database commands.

Example of unsafe code:
query = f"SELECT * FROM users WHERE email = '{email}'"


Potential risks:

* Authentication bypass
* Data theft
* Data modification

Prevention methods:

* Parameterized queries
* Input validation
* ORM frameworks

AppShield relevance:

Flask-SQLAlchemy automatically uses safe parameterized queries, reducing SQL Injection risks.

---

Outcome of Day 2

Successfully completed:

* Authentication page creation
* CSS styling
* Backend route integration
* Authentication flow testing
* SQL Injection study
* Frontend and backend synchronization
