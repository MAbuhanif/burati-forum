# Burati Forum

Burati Forum is a web application built with Django that allows users to ask questions, post answers, and engage in discussions. The application includes user authentication, profile management, and the ability to update and delete questions and answers.

## Features

- User registration and authentication
- User profile management
- Ask questions and post answers
- Edit and delete questions and answers
- View user profiles
- Search for questions
- Responsive design with Bootstrap

## Technologies Used

- Python 3.8+
- Django 3.2+
- Bootstrap 4.5
- django-summernote
- SQLite (Development)
- PostgreSQL (Production-ready)


## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/MAbuhanif/burati-forum.git
   cd burati-forum
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Configuration

Create a .env file in the root directory and add the following environment variables:

```markdown
DATABASE_URL=postgresql://username:password@hostname:port/dbname
SECRET_KEY=your_secret_key
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

## Static and Media Files

Ensure that your settings.py is configured to handle static and media files:

```markdown
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Usage

- **Register** for an account or log in if you already have one.
- **Ask a question** by navigating to the "Ask a Question" page.
- **Post an answer** to a question by navigating to the question's detail page.
- **Edit or delete** your questions and answers.
- **View and update** your profile information.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- Stack Overflow community inspiration
- Code Institute Slack Channels and Tutor support
