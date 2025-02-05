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


## User Stories

All user stories can be found in a linked GitHub project [here](https://github.com/users/MAbuhanif/projects/8/views/1)

## Site Pages

### Home Page
![Home Page](static/images/screenshots/home.png)

### About Page
![About Page](static/images/screenshots/about.png)

### Register Page
![Register Page](static/images/screenshots/signup.png)

### Login Page
![Login Page](static/images/screenshots/login.png)

### Profile Page
![Profile Page](static/images/screenshots/profile.png)

### Update Profile Page
![Update Profile Page](static/images/screenshots/update_profile.png)

### Ask a Question Page
![Ask a Question Page](static/images/screenshots/ask_question.png)

### Question Detail Page
![Question Detail Page](static/images/screenshots/question_detail.png)

### Update Question Page
![Update Question Page](static/images/screenshots/update_question.png)

### Delete Question Page
![Delete Question Page](static/images/screenshots/delete_question.png)

### Post an Answer
![Post an Answer](static/images/screenshots/post_answer.png)

### Update Answer Page
![Update Answer Page](static/images/screenshots/update_answer.png)

### Delete Answer Page
![Delete Answer Page](static/images/screenshots/delete_answer.png)


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
| user_id (FK)    | Integer      | References User.id    |
| bio             | Text         | User biography         |
| phone           | String       | Contact number         |
| profile_image   | String       | Image URL/path         |

### Question Table
| Column          | Type         | Description            |
|-----------------|--------------|------------------------|
| id (PK)         | Integer      | Primary Key            |
| user_id (FK)    | Integer      | References User.id    |
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

### Manual Testing

#### Test Cases Overview

| Feature Tested         | Action Performed                                                                 | Expected Result                                      | Pass/Fail |
|------------------------|----------------------------------------------------------------------------------|------------------------------------------------------|-----------|
| **User Registration**  | Filled signup form with valid credentials                                        | Account created, redirected to login page            | Pass      |
|                        | Attempted registration with existing username/email                             | Error message displayed                              | Pass      |
| **Login**              | Logged in with correct credentials                                              | Successful redirect to homepage                      | Pass      |
|                        | Attempted login with invalid credentials                                        | Error message displayed                              | Pass      |
| **Question Creation**  | Logged-in user submitted form with title/content                                | Question appears in homepage list                    | Pass      |
|                        | Attempted question creation without title                                       | Form validation error displayed                      | Pass      |
| **Question Editing**   | Author modified question title/content                                          | Updated content visible in question detail view      | Pass      |
|                        | Non-author attempted to edit question                                           | Edit button hidden/access denied                     | Pass      |
| **Question Deletion**  | Author deleted question                                                         | Question removed from all listings                   | Pass      |
|                        | Non-author attempted deletion                                                   | Delete button hidden/access denied                   | Pass      |
| **Answer Submission**  | Logged-in user posted answer to question                                        | Answer appears in question thread                    | Pass      |
|                        | Attempted empty answer submission                                               | Form validation error displayed                      | Pass      |
| **Content Visibility** | Anonymous user viewed questions/answers                                        | Content visible, action buttons hidden               | Pass      |
| **Admin Moderation**   | Admin approved/rejected answer via admin panel                                  | Approval status reflected in public view             | Pass      |
| **Responsive Design**  | Tested on mobile (≤768px), tablet (769-992px), desktop (≥993px)                 | Consistent layout and functionality across devices   | Pass      |
| **Form Validation**    | Submitted forms with:<br>- HTML tags in content<br>- Extremely long inputs      | Proper sanitization/validation                       | Pass      |

### Deployment
- The live deployed application can be found deployed on [Heroku](https://buratiforum-c036b7903a26.herokuapp.com/).

This project uses **Heroku**, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select New in the top-right corner of your **Heroku** Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set your environment variables.
  
   |       KEY       | VALUE           |
   |-----------------|-----------------|
   | DATABASE_URL	   | user's own value|
   | SECRET_KEY      | user's own value|
   | CLOUDINARY_URL  | user's own value|

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

**Install the dependencies:**

   - pip install -r requirements.txt

> If you have your own packages that have been installed, then the requirements file needs updated using:

   - pip3 freeze --local > requirements.txt

> The **Procfile** can be created with the following command:

- echo web: gunicorn app_name.wsgi > Procfile
- replace app_name with the name of your primary Django app name; the folder where settings.py is located

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

### Configuration

Create a .env file in the root directory and add the following environment variables:

```markdown
DATABASE_URL=postgresql://username:password@hostname:port/dbname
SECRET_KEY=your_secret_key
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

### Static and Media Files

Ensure that your settings.py is configured to handle static and media files:

```markdown
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Usage

- **Register** for an account or log in if you already have one.
- **Ask a question** by navigating to the "Ask a Question" page.
- **Post an answer** to a question by navigating to the question's detail page.
- **Edit or delete** your questions and answers.
- **View and update** your profile information.

### File Structure

burati-forum/
├── buratiforum/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── forum/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── forumuser/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── static/
│   ├── css/
│   │   └── style.css
│   └── ...
├── templates/
│   ├── base.html
│   ├── forum/
│   │   ├── ask_question.html
│   │   ├── question_detail.html
│   │   ├── answer_form.html
│   │   ├── confirm_delete.html
│   │   ├── confirm_delete_answer.html
│   │   ├── update_question.html
│   │   └── ...
│   ├── forumuser/
│   │   ├── profile.html
│   │   ├── profile_update.html
│   │   ├── about.html
│   │   └── ...
│   ├── 400.html
│   ├── 403.html
│   ├── 404.html
│   ├── 500.html
│   └── ...
├── .env
├── .gitignore
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt

### Contributing

Contributions are welcome! Please follow these steps to contribute:

   1. Fork the repository.
   2. Create a new branch: git checkout -b my-feature-branch.
   3. Make your changes and commit them: git commit -m 'Add some feature'.
   4. Push to the branch: git push origin my-feature-branch.
   5. Submit a pull request.

### License

   - This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- Stack Overflow community inspiration
- Code Institute Slack Channels and Tutor support
