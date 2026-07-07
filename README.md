
# 🐾 Pet Adoption Management System

A full-stack web-based **Pet Adoption Management System** designed to connect users with adoptable pets and provide administrators with a complete management platform for handling users, pets, administrators, and adoption applications.

The system allows users to register accounts, browse available pets, submit adoption applications, and track adoption progress. Administrators can manage the entire platform through an integrated dashboard, including user management, pet management, administrator management, and adoption application review.

The project is developed using **Flask**, **SQLite**, **HTML/CSS**, **JavaScript**, and **Bootstrap**, following a client-server web application architecture.

---

# 📌 Project Overview

## Background

Pet adoption platforms require an efficient way to manage pet information, user applications, and adoption workflows.

Traditional adoption processes often rely on manual communication, which can lead to:

* Difficult application tracking
* Poor information management
* Slow approval processes
* Lack of transparency between users and organizations

This project provides a digital adoption management solution where:

* Users can easily discover pets and apply for adoption.
* Administrators can efficiently manage adoption requests.
* The system maintains structured records of users, pets, and applications.

---

# 🎯 Project Objectives

The main objectives of this system are:

1. Provide an online platform for pet adoption.
2. Allow users to create accounts and manage personal information.
3. Provide administrators with a centralized management dashboard.
4. Implement a complete adoption approval workflow.
5. Provide efficient searching and filtering functions for management data.
6. Maintain consistent data storage using a relational database.

---

# 👥 User Roles

The system contains two main types of users:

---

# 1. Normal User

Normal users can:

* Register an account
* Login/logout
* Browse pets
* View pet care information
* Submit adoption applications
* Track adoption status

User workflow:

```
Register
   |
   ↓
Login
   |
   ↓
Browse Pets
   |
   ↓
Submit Adoption Application
   |
   ↓
Wait for Admin Review
   |
   ↓
Approved / Rejected
```

---

# 2. Administrator

Administrators manage the entire system.

Admin functions include:

* Dashboard overview
* User management
* Administrator management
* Pet management
* Adoption application management

Admin workflow:

```
Admin Login
      |
      ↓
Dashboard
      |
      ↓
Manage System Data
      |
      ↓
Review Adoption Applications
      |
      ↓
Approve / Reject Applications
```

---

# ✨ Main Features

# User Side Features

---

## 1. User Registration

Users can create new accounts by providing:

* Username
* Password
* Gender
* Age
* Telephone
* Email
* Address
* Profile picture

Registration process:

```
Input information
        |
        ↓
Validate data
        |
        ↓
Store into database
        |
        ↓
Login available
```

The system prevents duplicate accounts using database validation.

---

## 2. User Authentication

The system provides:

* Login
* Logout
* Session management

After successful login:

* User session is created.
* Navigation bar updates automatically.
* User avatar is displayed.

---

## 3. Pet Browsing

Users can browse pet information including:

* Pet name
* Type
* Gender
* Age
* Description
* Adoption status

---

## 4. Pet Care Knowledge

The system provides educational information about pet care.

Users can learn:

* Feeding information
* Daily care requirements
* Basic pet knowledge

---

## 5. Adoption Application

Users can submit adoption requests.

Each application contains:

| Field      | Description               |
| ---------- | ------------------------- |
| User       | Applicant information     |
| Pet        | Selected pet              |
| Message    | Adoption reason           |
| Apply Time | Submission time           |
| Status     | Current application state |

---

Application status:

| Status   | Meaning            |
| -------- | ------------------ |
| Pending  | Waiting for review |
| Approved | Adoption accepted  |
| Rejected | Adoption declined  |

Workflow:

```
User submits application

        ↓

Pending

        ↓

Admin review

        ↓

Approved / Rejected
```

---

# Admin Dashboard Features

The administrator dashboard provides a centralized control panel.

---

# 1. Dashboard

The dashboard provides access to:

* User management
* Admin management
* Pet management
* Adoption management

Layout:

```
--------------------------------
Sidebar       Dashboard Content
--------------------------------
Users
Admins
Pets
Adoptions
--------------------------------
```

---

# 2. User Management

Administrators can:

## CRUD Operations

### Create

Add new users.

### Read

View all registered users.

### Update

Modify user information.

### Delete

Remove user accounts.

---

## Advanced User Search

The system supports multi-condition searching.

Search fields:

| Field     | Method       |
| --------- | ------------ |
| ID        | Exact match  |
| Username  | Fuzzy search |
| Gender    | Exact match  |
| Age       | Exact match  |
| Telephone | Fuzzy search |
| Email     | Fuzzy search |
| Address   | Fuzzy search |
| Status    | Exact match  |

Example:

Search:

```
Username: Tom
Gender: Male
```

SQL condition:

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

# 3. Administrator Management

Administrators can manage administrator accounts.

Functions:

* Add administrator
* Update administrator
* Delete administrator
* Search administrator

Search supports:

* ID
* Admin name
* Real name
* Gender
* Email
* Telephone

---

# 4. Pet Management

Administrators can manage pet records.

Functions:

* Add pets
* Edit pets
* Delete pets
* Search pets

Search fields:

| Field    | Method |
| -------- | ------ |
| ID       | Exact  |
| Pet name | Fuzzy  |
| Type     | Exact  |
| Gender   | Exact  |
| Status   | Exact  |

---

# 5. Adoption Management

This is the core workflow of the system.

Administrators can:

* View adoption requests
* Approve requests
* Reject requests
* Delete requests

Application states:

```
0 → Pending

1 → Approved

2 → Rejected

-1 → Deleted
```

---

## Approved Applications

After approval:

```
Pending Application

        ↓

Approve Button

        ↓

state = 1

        ↓

Approved Adoption Page
```

---

## Rejected Applications

After rejection:

```
Pending Application

        ↓

Reject Button

        ↓

state = 2

        ↓

Rejected Adoption Page
```

---

# 🏗 System Architecture

The project follows a Flask MVC-style structure.

```
Browser

   |
   |

HTML Templates
(Jinja2)

   |
   |

Flask Routes

   |
   |

Database Layer

   |
   |

SQLite Database
```

---

# 🛠 Technology Stack

## Backend

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming language |
| Flask      | Web framework        |
| SQLite     | Database             |
| Jinja2     | Template rendering   |

---

## Frontend

| Technology | Purpose             |
| ---------- | ------------------- |
| HTML5      | Page structure      |
| CSS3       | Styling             |
| JavaScript | Dynamic interaction |
| Bootstrap  | UI components       |

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
│   └── pet_adoption.db
│
├── templates
│
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│
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

    ├── css
    │   ├── style.css
    │   └── admin.css
    │
    └── js
```

---

# 🗄 Database Design

The system uses SQLite.

---

## Users Table

Stores registered users.

Example:

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
```

---

## Admins Table

Stores administrator accounts.

Example:

```
admins

id
admin_name
password
real_name
telephone
email
gender
profile_image
```

---

## Pets Table

Stores pet information.

Example:

```
pets

id
pet_name
pet_type
sex
age
description
status
```

---

## Applications Table

Stores adoption applications.

Example:

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
```

---

# 🚀 Installation Guide

## Clone Project

```bash
git clone <repository-url>

cd pet_adoption_system
```

---

## Create Virtual Environment

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5001
```

---

# 🔮 Future Improvements

Possible improvements:

## 1. Pagination

Add pagination for:

* Users
* Admins
* Pets
* Adoption records

## 2. Email Notification

Notify users when:

* Application submitted
* Application approved
* Application rejected

## 3. Image Upload

Replace image URL input with:

* File upload
* Cloud storage

## 4. Permission System

Support multiple admin roles:

* Super Admin
* Manager
* Reviewer

## 5. Deployment

Deploy system using:

* Docker
* Cloud server
* Production database

---

# 👨‍💻 Development

This project demonstrates:

* Full-stack web development
* Database design
* CRUD operations
* Authentication
* Session management
* AJAX interaction
* Dynamic searching
* Admin dashboard design
