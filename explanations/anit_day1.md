 Day 1 - Environment Setup and DVWA Preparation

 Objective

The objective of Day 1 was to set up the development environment on Windows, clone the shared GitHub repository, confirm the Flask application runs successfully, prepare DVWA on Kali Linux for future testing, and understand HTTP security headers used in web application security.

---
Python Environment Setup
 Python 3.11+

Verified Python installation.

Command used:

```bash
python --version
```

Purpose:

* Run the Flask application
* Support backend development
* Run project dependencies

---
 Package Installation

Installed the same Python packages used by Sajan to maintain a consistent development environment.

Installed packages:

```bash
pip install flask flask-login flask-sqlalchemy bcrypt bandit python-dotenv requests reportlab google-generativeai
```

Purpose:

* Flask → Web application framework
* Flask-Login → User authentication and session management
* Flask-SQLAlchemy → Database ORM
* Bcrypt → Password hashing
* Bandit → Static security analysis
* Requests → HTTP requests
* ReportLab → PDF report generation
* Google Generative AI → AI-powered explanations
* Python-Dotenv → Environment variable management

---
Repository Setup

Cloned the shared GitHub repository after Sajan completed the initial setup.

Command:

```bash
git clone <repository-url>
```

Purpose:

* Obtain the latest project files
* Synchronize development environments

---

 Flask Application Verification

Ran the application locally.

Command:

```bash
python run.py
```

Result:

The application successfully ran at:

```text
http://127.0.0.1:5000
```

This verified that the project was functioning correctly on multiple systems.

---

 DVWA Setup on Kali Linux

DVWA (Damn Vulnerable Web Application) is an intentionally vulnerable web application used for learning and testing web security concepts safely.

Tasks completed:

* Verified Apache, PHP, and MariaDB installations
* Installed and configured DVWA
* Created the DVWA database
* Configured database credentials
* Accessed DVWA through the browser
* Set the security level to Low

Purpose:

DVWA will act as the testing target for AppShield Module 2 during web vulnerability scanning.

---

HTTP Security Headers

Read about OWASP Secure Headers and understood their purpose.

1.Strict-Transport-Security (HSTS)

Forces browsers to communicate using HTTPS only.

2. Content-Security-Policy (CSP)

Restricts which resources can be loaded by a webpage and helps reduce XSS attacks.

3.X-Frame-Options

Prevents clickjacking attacks by restricting iframe usage.

4. X-Content-Type-Options

Prevents MIME type sniffing by browsers.

5. Referrer-Policy

Controls how much referrer information is shared.

6. Permissions-Policy

Controls browser features such as camera, microphone, and geolocation access.

---

 Outcome of Day 1

Successfully completed:

* Python environment setup
* Package installation
* GitHub repository cloning
* Flask application verification
* DVWA installation and configuration
* HTTP security headers study
* Prepared Kali Linux testing environment for future web scanning modules
