# Job Board Backend 🏢💼

A Django REST API for a job board platform with role-based authentication, job management, optimized search, and Swagger documentation.

## 🚀 Features

- **Role-Based Access Control** (Admins manage jobs, users apply)
- **JWT Authentication** for secure login
- **Job Posting & Management** with CRUD operations
- **Optimized Job Search** (filter by location, category, and keyword)
- **Swagger API Documentation** for easy testing
- **PostgreSQL Database** for scalable storage
- File Upload Support (Users can upload resumes for job applications)
- Admin Dashboard for managing jobs and applications

## 🔧 Installation

```bash
git clone https://github.com/Osamaseid/alx-project-nexus.git
cd job_board
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 📌 API Endpoints

### Authentication

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login & get JWT token
- `GET /api/auth/me/` - Get logged-in user details

### Jobs

- `GET /api/jobs/` - List all jobs
- `POST /api/jobs/` - Create a job (Admin only)
- `GET /api/jobs/{id}/` - Retrieve job details
- `PUT /api/jobs/{id}/` - Update job (Admin only)
- `DELETE /api/jobs/{id}/` - Delete job (Admin only)

### Applications

- `POST /api/jobs/{job_id}/apply/` - Apply for a job
- `GET /api/applications/` - View user's job applications

## 📌 API Documentation

Swagger UI: [https://alx-project-nexus-pvjg.onrender.com/api/docs/](https://alx-project-nexus-pvjg.onrender.com/api/docs/)

## 🌍 Deployment

Live API: [https://alx-project-nexus-pvjg.onrender.com](https://alx-project-nexus-pvjg.onrender.com)

## 🛠 Tech Stack

- **Django & DRF** - Backend Framework
- **PostgreSQL** - Database
- **JWT (SimpleJWT)** - Authentication
- **Swagger (drf-yasg)** - API Documentation
- **Django Filters** - Optimized search & filtering
- **Gunicorn & WhiteNoise** - Deployment optimizations
