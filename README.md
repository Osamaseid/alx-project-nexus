# Job Board Backend 🏢💼

A Django REST Framework backend for a Job Board platform with role-based authentication (JWT), job posting management, optimized job search, and Swagger API documentation.

## 🚀 Features

✅ **Role-Based Access Control**: Admins can manage jobs; users can apply.  
✅ **JWT Authentication**: Secure login and token-based authentication.  
✅ **Job Posting Management**: CRUD operations for job posts.  
✅ **Optimized Job Search**: Filter by location, category, and keyword.  
✅ **Swagger API Docs**: Auto-generated interactive API documentation.  
✅ **PostgreSQL Database**: Scalable and efficient database management.

## ⚙️ Tech Stack

- **Django & Django REST Framework** – Backend API
- **PostgreSQL** – Database
- **JWT (SimpleJWT)** – Authentication
- **Swagger (drf-yasg)** – API Documentation
- **Django Filters** – Query optimization
- **Gunicorn & WhiteNoise** – Deployment

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/job-board-backend.git
cd job-board-backend
```

### 2️⃣ Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```env
DB_NAME=jobboard_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

API is now available at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) 🚀

## 📌 API Endpoints

### Authentication

| Method | Endpoint              | Description                |
| ------ | --------------------- | -------------------------- |
| POST   | `/api/auth/register/` | Register a new user        |
| POST   | `/api/auth/login/`    | Login and get JWT token    |
| GET    | `/api/auth/me/`       | Get logged-in user details |

### Job Management

| Method | Endpoint          | Description                   |
| ------ | ----------------- | ----------------------------- |
| GET    | `/api/jobs/`      | List all jobs                 |
| POST   | `/api/jobs/`      | Create a new job (Admin only) |
| GET    | `/api/jobs/{id}/` | Get job detail                |
| PUT    | `/api/jobs/{id}/` | Update job (Admin only)       |
| DELETE | `/api/jobs/{id}/` | Delete job (Admin only)       |

### Applications

| Method | Endpoint                    | Description                  |
| ------ | --------------------------- | ---------------------------- |
| POST   | `/api/jobs/{job_id}/apply/` | Apply for a job              |
| GET    | `/api/applications/`        | View user's job applications |

## 📌 API Documentation

📌 **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)  
📌 **ReDoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)

## 🎯 Deployment

### Deploy on Render

1. Push code to GitHub
2. Create a Render Web Service
3. Set environment variables
4. Use Gunicorn as start command:

```bash
gunicorn job_board.wsgi:application
```

### Deploy on Heroku

1. Install Heroku CLI:

```bash
heroku login
```

2. Create a Heroku app:

```bash
heroku create job-board-api
```

3. Add a PostgreSQL database:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Deploy to Heroku:

```bash
git push heroku main
```

## 🛠️ Contributing

1. Fork the repository
2. Clone your forked repository
3. Create a new branch:

```bash
git checkout -b feature-name
```

4. Commit your changes:

```bash
git commit -m "Added a new feature"
```

5. Push to GitHub:

```bash
git push origin feature-name
```

6. Create a Pull Request 🚀

## 📜 License

This project is licensed under the **MIT License**.

## 📞 Contact

For questions or support, reach out to:
📧 **Email**: support@example.com  
🌐 **Website**: [example.com](http://example.com)
