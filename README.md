# 🏡 HBnB Evolution

## 🎯 Objective
The goal of this project is to design, implement, and deploy a simplified AirBnB-like platform with a scalable backend and an interactive frontend. The project is built in four main phases:<br>

Part1: Technical Documentation<br>

Part2: API and Business Logic Implementation<br>

Part3: Database Integration & Authentication<br>

Part4: Web Client Development<br>

## ⚙️ INSTALLATION

### 🔧 Requirements

・Python 3.8+ <br>
・pip <br>
・Flask <br>
・SQLAlchemy <br>
・flask-restx<br>
・flask-jwt-extended      <br>
・flask-cors<br>

### 🧪Set Up

1. Clone the repository:<br>
 ``` 
 https://github.com/Emi-H106/holbertonschool-hbnb.git
 ``` 

 2. Create a Virtual Environment (Recommended) <br>
```  
python3 -m venv venv  
source venv/bin/activate  
``` 
 3. Install Dependencies<br>
  ```
pip install -r requirements.txt
```
4.Run the application<br>
```
 python run.py
 ```
 Visit: http://localhost:5000<br>

### ✏️ The Project Directory Structure:
```
hbnb/
├── app/                     # Core application package
│   ├── __init__.py          # App factory for Flask initialization
│   ├── api/                 # API route definitions (Flask-Restx namespaces)
│   ├── models/              # SQLAlchemy models and data structures
│   ├── services/            # Business logic and facade classes
│   ├── persistence/         # Database sessions, schemas, and queries
├── migration/               # Alembic migration scripts for DB schema changes
├── sql/                     # Optional raw SQL scripts (e.g., initial schema or seed data)
├── static/                  # Frontend static files (CSS, JavaScript, images)
├── templates/               # Jinja2 HTML templates for the web interface
├── run.py                   # Entry point to start the Flask app
├── config.py                # App configuration for different environments
├── requirements.txt         # List of Python dependencies
├── README.md                # Project overview and setup instructions

```

## 🧩 Tech Stack

**:small_orange_diamond:Backend**<br>

・Python / Flask<br>

・SQLAlchemy / SQLite / MySQL<br>

・JWT Authentication<br>

・Flask-Restx / Flask-Migrate / Flask-CORS<br>

**:small_orange_diamond:Frontend**<br>

・HTML5 / CSS3<br>

・JavaScript (ES6)<br>

・Fetch API<br>

・Jinja2 templates<br>

## 🔐 Features
・User Auth: JWT login, role-based access (admin)<br>

・CRUD: Users, Places, Reviews, Amenities<br>

・Secure: Passwords hashed with bcrypt, CORS setup<br>

・Dynamic UI: Review forms and filters rendered with JS<br>

・Diagrams: UML class/sequence/package, ER schema (Mermaid.js)<br>

## Authors
[Emi Hatano](https://github.com/Emi-H106)

