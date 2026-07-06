# pet_adoption_system# 🐾 Pet Adoption Management System

A full-stack web application for managing pet adoption processes, built with Flask and SQLite.  
The system includes user authentication, admin dashboard, and complete CRUD management for pets, users, and adoption applications.

---

## 🚀 Features

### 👤 User Features
- User registration and login system
- Browse available pets
- Submit adoption applications
- View pet details and adoption status

### 🛠 Admin Features
- Secure admin login with session authentication
- Admin dashboard with sidebar navigation
- User management (view / manage users)
- Pet management (add / edit / delete pets)
- Adoption application management
- Comment and blog management system

---

## 🧱 Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Version Control:** Git & GitHub

---

## 📊 System Modules

- User Module
- Admin Module
- Pet Module
- Adoption Module
- Comment System
- Blog / Activity System

---

## 🗂 Database Schema

The system uses a relational SQLite database including:

- users
- admins
- pets
- applications
- adoption_records
- comments
- answers
- blogs

---

## 🖥 Admin Dashboard

The admin panel includes:

- Dashboard overview
- User management
- Pet management
- Adoption request processing
- Content moderation (comments & blogs)
- Volunteer/application handling

---

## 🔐 Authentication

- Session-based admin authentication
- Role-based access control (user/admin separation)

---

## 📷 UI Overview

The admin interface uses a sidebar-based layout:

- Clean navigation structure
- Sectioned management modules
- Responsive dashboard design

---

## 📦 Installation

```bash
git clone https://github.com/your-repo/pet_adoption_system.git
cd pet_adoption_system
pip install -r requirements.txt
python app.py