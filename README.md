# AFB Learning Management System (LMS)

A full-featured Learning Management System built with **Django 5**, allowing teachers to create lessons and assessments, students to view lessons and submit quizzes, and administrators to manage users and content.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
---

## Features

- **User Roles**
  - **Teacher:** Create courses, lessons, and assignments.
  - **Student:** View lessons and submit assessments.
  - **Administrator:** Manage users and view system logs.

- **Courses and Lessons**
  - Teachers can create multiple courses.
  - Lessons can be added to courses with rich-text content.

- **Authentication**
  - User registration and login.
  - Profile roles (student/teacher) are automatically managed.

- **Dashboard**
  - Teacher dashboard: Shows created lessons and courses.
  - Student dashboard: Shows enrolled courses and available lessons.

- **Assessments**
  - Create quizzes or assignments per course.
  - Students can submit and view results.

- **Responsive Design**
  - Styled with light blue and purple themes.

---

## Technologies

- Python 3.13
- Django 5.2.7
- SQLite (default database)
- HTML, CSS (for front-end styling)
- Django Template System
- Django Messages Framework

---
## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd afb_dashboard
```
2. **Create a virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
```
3. **Start Project Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/
