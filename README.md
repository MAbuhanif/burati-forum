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

## Site Pages

### Home Page
![Home Page](screenshots/home_page.png)

### Register Page
![Register Page](screenshots/register_page.png)

### Login Page
![Login Page](screenshots/login_page.png)

### Profile Page
![Profile Page](screenshots/profile_page.png)

### Ask a Question Page
![Ask a Question Page](screenshots/ask_question_page.png)

### Question Detail Page
![Question Detail Page](screenshots/question_detail_page.png)

### Update Question Page
![Update Question Page](screenshots/update_question_page.png)

### Delete Question Page
![Delete Question Page](screenshots/delete_question_page.png)

### Post an Answer
![Post an Answer](screenshots/post_answer.png)

### Update Answer Page
![Update Answer Page](screenshots/update_answer_page.png)

### Delete Answer Page
![Delete Answer Page](screenshots/delete_answer_page.png)


## Tools & Technologies Used

- **HTML** - used for the main site content.
- **CSS** used for the main site design and layout.
- **Python** used as the back-end programming language.
- **Git** used for version control. (git add, git commit, git push)
- **GitHub** used for secure online code storage.
- **Gitpod** used as a cloud-based IDE for development.
- **Django** used as the Python framework for the site.
- **Bootstrap** used as the front-end CSS framework for modern responsiveness and pre-built components.
- **SQLite (Development)**
- **PostgreSQL (Production-ready)** used as the relational database management.
- **Crispy Forms** used for auto-formatting of front-end forms
- **Allauth** used as the user authentication system
- **Heroku** used for hosting the deployed back-end site.

## Database Design

  - While planning this project, I drew up an Entity Relationship Diagram to help me to visualise the database models and their relationships.


  ### Users Table
| Column          | Type         | Description       |
|-----------------|--------------|-------------------|
| id (PK)         | Integer      | Primary Key       |
| username        | String       | Unique identifier |
| password        | String       | Hashed password   |
| email           | String       | User email        |
| first_name      | String       | First name        |
| last_name       | String       | Last name         |
| date_joined     | DateTime     | Registration date |

### Profile Table
| Column          | Type         | Description            |
|-----------------|--------------|------------------------|
| id (PK)         | Integer      | Primary Key            |
| user_id (FK)    | Integer      | References Users.id    |
| bio             | Text         | User biography         |
| phone           | String       | Contact number         |
| profile_image   | String       | Image URL/path         |

### Question Table
| Column          | Type         | Description            |
|-----------------|--------------|------------------------|
| id (PK)         | Integer      | Primary Key            |
| user_id (FK)    | Integer      | References Users.id    |
| title           | String       | Question title         |
| detail         | Text         | Question details       |
| created_on      | DateTime     | Creation timestamp     |

### Answer Table
| Column          | Type         | Description            |
|-----------------|--------------|------------------------|
| id (PK)         | Integer      | Primary Key            |
| question_id (FK)| Integer      | References Question.id |
| user_id (FK)    | Integer      | References Users.id    |
| detail         | Text         | Answer text            |
| created_on      | DateTime     | Creation timestamp     |
| approved        | Boolean      | Moderation status      |

### Relationships
1. **One-to-One**:  
   `Users` ←→ `Profile` (One user has one profile)

2. **One-to-Many**:  
   `Users` ←→ `Questions` (One user can have many questions)  
   `Users` ←→ `Answers` (One user can have many answers)  
   `Questions` ←→ `Answers` (One question can have many answers)
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
