```markdown
# 🐾 Pet Adoption Management System


A full-stack web-based **Pet Adoption Management System** designed to provide an efficient platform for users to discover pets, submit adoption applications, and allow administrators to manage the entire adoption workflow.

The system enables users to:

- Register and login securely
- Browse available pets
- View pet care information
- Submit adoption applications
- Track adoption progress

Administrators can manage:

- Users
- Administrators
- Pets
- Adoption applications


The project is developed using:

- Python Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap


The system follows a Flask MVC-style architecture with a relational database design.


---

# 📌 Project Overview


## Background


Pet adoption organizations require an efficient system to manage:

- Pet information
- User applications
- Adoption decisions
- User records
- Administrative operations


Traditional adoption processes may cause:

- Difficult application tracking
- Inefficient communication
- Poor data management
- Lack of transparency


This project provides a digital adoption management solution where:

- Users can easily find suitable pets.
- Users can submit adoption requests online.
- Administrators can review and manage applications.
- All information is stored systematically in a database.


---

# 🎯 Project Objectives


The objectives of this project are:


1. Build an online pet adoption platform.

2. Provide secure user authentication.

3. Implement administrator management functions.

4. Create a complete adoption approval workflow.

5. Provide advanced searching functions.

6. Maintain structured database management.

7. Improve efficiency of adoption organizations.


---

# 👥 User Roles


The system contains two main roles:


# 1. Normal User


Normal users can:


- Register an account
- Login/logout
- Browse pets
- View pet care knowledge
- Submit adoption applications
- Track application status


User workflow:

```

Register

↓

Login

↓

Browse Pets

↓

Submit Adoption Application

↓

Admin Review

↓

Approved / Rejected

```


---

# 2. Administrator


Administrators manage the entire platform.


Admin functions:


- Dashboard overview
- User management
- Administrator management
- Pet management
- Adoption application management


Admin workflow:

```

Admin Login

```
  ↓
```

Dashboard

```
  ↓
```

Manage System Data

```
  ↓
```

Review Adoption Applications

```
  ↓
```

Approve / Reject

```


---

# ✨ Main Features


# User Side Features


## 1. User Registration


Users can create accounts with:


- Username
- Password
- Gender
- Age
- Telephone
- Email
- Address
- Profile picture


The system validates:

- Duplicate username
- Duplicate email


---

# 2. Secure Authentication


The system uses password hashing for security.


Password storage:

```

Plain Password

```
    ↓
```

generate_password_hash()

```
    ↓
```

Encrypted Hash

```
    ↓
```

Database

```


Password verification:

```

User Input Password

```
    ↓
```

check_password_hash()

```
    ↓
```

Login Success / Failed

```


Passwords are never stored as plain text.


Authentication includes:


- Login
- Logout
- Session management
- User avatar display


---

# 3. Pet Browsing


Users can view:


- Pet image
- Pet name
- Pet type
- Gender
- Birthday
- Description
- Adoption status


Pet images are stored in:


```

static/pets/

```


The database stores image paths:

Example:

```

pets/buddy.jpg

```


---

# 4. Pet Care Knowledge


Users can access pet care information including:


- Feeding knowledge
- Daily care
- Basic pet requirements


---

# 5. Adoption Application


Users can submit adoption requests.


Each application contains:


| Field | Description |
|---|---|
| User | Applicant information |
| Pet | Selected pet |
| Message | Adoption reason |
| Apply Time | Submission time |
| Status | Application status |


Application workflow:


```

User submits application

```
    ↓
```

Pending

```
    ↓
```

Admin Review

```
    ↓
```

Approved / Rejected

```


Application states:


| State | Meaning |
|---|---|
| 0 | Pending |
| 1 | Approved |
| 2 | Rejected |
| -1 | Deleted |


---

# 🖥 Admin Dashboard Features


The administrator dashboard provides centralized management.


Dashboard modules:


```

Dashboard

|
|-- User Management
|
|-- Admin Management
|
|-- Pet Management
|
|-- Adoption Management

```


---

# 1. User Management


Administrators can:


## CRUD Operations


### Create

Add users.


### Read

View user information.


### Update

Modify user information.


### Delete

Remove users.



---

## Advanced User Search


The system supports multiple conditions.


Search fields:


| Field | Method |
|-|-|
| ID | Exact match |
| Username | Fuzzy search |
| Gender | Exact match |
| Age | Exact match |
| Telephone | Fuzzy search |
| Email | Fuzzy search |
| Address | Fuzzy search |
| Status | Exact match |



Example:


Input:

```

Username:
Tom

Gender:
Male

```


SQL logic:


```

username LIKE '%Tom%'
AND gender='Male'

```


Result:


```

Tom
Tommy

```


---

# 2. Administrator Management


Administrators can:


- Add administrators
- Update administrators
- Delete administrators
- Search administrators


Search supports:


- ID
- Admin name
- Real name
- Gender
- Email
- Telephone


Admin passwords are also stored using password hashing.


---

# 3. Pet Management


Administrators can:


- Add pets
- Edit pets
- Delete pets
- Search pets


Pet search supports:


| Field | Method |
|-|-|
| ID | Exact |
| Pet name | Fuzzy |
| Pet type | Exact |
| Gender | Exact |
| Status | Exact |


---

# 4. Adoption Management


Administrators can:


- View adoption requests
- Approve requests
- Reject requests
- Delete applications


Workflow:


```

Pending Application

```
    ↓
```

Approve

```
    ↓
```

Approved Applications

Pending Application

```
    ↓
```

Reject

```
    ↓
```

Rejected Applications

```


---

# 🏗 System Architecture


The project follows a Flask MVC-style structure.


```

Browser

```
|
```

HTML Templates
(Jinja2)

```
|
```

Flask Routes

```
|
```

Database Layer

```
|
```

SQLite Database

```


---

# 🛠 Technology Stack


## Backend


| Technology | Purpose |
|-|-|
| Python | Programming language |
| Flask | Web framework |
| SQLite | Database |
| Jinja2 | Template engine |
| Werkzeug Security | Password hashing |


---

## Frontend


| Technology | Purpose |
|-|-|
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Dynamic interaction |
| Bootstrap | UI components |


---

# 📂 Project Structure


```

Pet_Adoption_System

│
├── app.py
│
├── requirements.txt
│
├── database
│   │
│   ├── schema.sql
│   │
│   ├── init_db.py
│   │
│   └── create_demo_data.py
│
│
├── instance
│   └── pet_adoption.db
│
│
├── templates
│
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   │
│   └── admin
│       ├── layout.html
│       ├── dashboard.html
│       ├── users.html
│       ├── admins.html
│       ├── pets.html
│       ├── adopt.html
│       ├── approved.html
│       └── rejected.html
│
│
└── static
│
├── css
│
├── js
│
└── pets
├── buddy.jpg
├── luna.jpg
├── max.jpg
├── milo.jpg
├── coco.jpg
├── charlie.jpg
├── oliver.jpg
└── nala.jpg

```


---

# 🗄 Database Design


The system uses SQLite database.


Main tables:


## Users


Stores registered users.


```

users

id
username
password
sex
age
telephone
email
address
pic
state

```


---

## Admins


Stores administrator accounts.


```

admins

id
admin_name
admin_password
real_name
telephone
email
birthday
gender
profile_image
remark

```


---

## Pets


Stores pet information.


```

pets

id
pet_name
pet_type
sex
birthday
pic
state
remark

```


---

## Applications


Stores adoption applications.


```

applications

id
user_id
pet_id
message
apply_time
state

```


Relationship:


```

User

1
|
|
*

Applications

*

|

|

1

Pet

````


---

# 🚀 Installation Guide


## 1. Clone Repository


```bash
git clone <repository-url>

cd pet_adoption_system
````

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Initialize Database

Create database:

```bash
python database/init_db.py
```

Generate demo data:

```bash
python database/create_demo_data.py
```

This will create:

* Demo users
* Demo administrators
* Sample pets

---

# 5. Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5001
```

---

# 🔑 Demo Accounts

## Admin Account

```
Username:
demo_admin


Password:
Admin123
```

Admin URL:

```
/admin/login
```

---

## User Account

```
Username:
demo_user


Password:
User123
```

---

# 🔮 Future Improvements

Possible improvements:

## 1. Pagination

Add pagination for:

* Users
* Admins
* Pets
* Adoption applications

---

## 2. Email Notification

Notify users when:

* Application submitted
* Application approved
* Application rejected

---

## 3. Image Upload System

Replace image filename input with:

* File upload
* Cloud storage

---

## 4. Permission Management

Support multiple administrator roles:

* Super Admin
* Manager
* Reviewer

---

## 5. Deployment

Deploy using:

* Docker
* Cloud hosting
* Production database

---

# 👨‍💻 Development Skills Demonstrated

This project demonstrates:

* Full-stack web development
* Flask application design
* Database design
* CRUD operations
* Authentication system
* Password security
* Session management
* AJAX interaction
* Advanced searching
* Admin dashboard development
* Relational database management

---

# License

This project is developed for educational and portfolio purposes.

```

---
