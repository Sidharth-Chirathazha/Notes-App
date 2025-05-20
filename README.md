# Django Notes App

A simple yet powerful notes taking web application built with Django. This application allows users to create accounts, log in, and manage their personal notes by creating, viewing, editing, and deleting them.

## Features

- **User Authentication**
  - Registration
  - Login/Logout
  - Secure password management

- **Notes Management**
  - Create new notes
  - View all notes
  - View note details
  - Edit existing notes
  - Delete notes

- **Responsive Design**
  - Built with Django templates
  - Mobile-friendly interface

## Technologies

- Django 
- MySQL
- Docker
- Docker Compose

## Prerequisites

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sidharth-Chirathazha/Notes-App.git
cd notes_app
```

### 2. Environment Setup

Create a `.env` file in the root directory of the project with the following content:

```
DJANGO_SECRET_KEY=Your Djano Secret Key
DEBUG=True(For development)/ False(For production)
MYSQL_ENGINE=django.db.backends.mysql
MYSQL_HOST=Your Db Host
MYSQL_PORT=Your Db Port
MYSQL_DATABASE=Your Db Name
MYSQL_USER=Your Db User Name
MYSQL_PASSWORD=Db Password
MYSQL_ROOT_PASSWORD=Db Root Password
```

You can modify these values if needed, but make sure to update them in both the `.env` file and your Docker Compose configuration if you make changes.

### 3. Run with Docker

Build and start the containers:

```bash
docker-compose up -d
```

The application will be available at [http://localhost:8000](http://localhost:8000)

### 4. Stop the Application

```bash
docker-compose down
```

To remove volumes (this will delete all data):

```bash
docker-compose down -v
```

## Application Structure

```
notes_app/
├── notes/                 # Notes management app
├── notes_app/             # Main project directory
├── static/                # Static files
├── staticfiles/           # Static files
├── templates/             # HTML templates
├── users/                 # User authentication app
├── .dockerignore          # Docker ignore file
├── .env                   # Environment variables
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker configuration
├── manage.py              # Command line
└── Requirements.txt       # Required Packages
```

## API Endpoints

### Authentication Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Home page |
| `/register/` | GET, POST | User registration |
| `/login/` | GET, POST | User login |
| `/logout/` | GET | User logout |

### Notes Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/notes/` | GET | List all notes for the logged-in user |
| `/note/<uuid:note_id>/` | GET | View a specific note's details |
| `/note/add/` | GET, POST | Add a new note |
| `/note/<uuid:note_id>/edit/` | GET, POST | Edit an existing note |
| `/note/<uuid:note_id>/delete/` | GET, POST | Delete a note |

## Usage Guide

1. **Registration**: Visit `/register/` to create a new account
2. **Login**: Visit `/login/` to access your account
3. **View Notes**: After logging in, you'll be directed to `/notes/` to see all your notes
4. **Create Note**: Click on "Add Note" or visit `/note/add/` to create a new note
5. **Edit Note**: Click on a note title to view it, then select "Edit" or visit `/note/<note_id>/edit/`
6. **Delete Note**: From the note detail page, select "Delete" or visit `/note/<note_id>/delete/`

## Development

### Running Migrations

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Creating a Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

### Accessing the Django Admin Interface

After creating a superuser, you can access the admin interface at [http://localhost:8000/admin](http://localhost:8000/admin)

## Database

The application uses MySQL as its database. The database connection is configured through environment variables in the Docker Compose file.

## Troubleshooting

### Database Connection Issues

If you experience database connection issues, ensure:

1. The MySQL container is running: `docker-compose ps`
2. Database credentials are correct in the `.env` file
3. MySQL service has fully started before the web service attempts to connect

### Application Not Loading

If the application doesn't load properly:

1. Check logs for errors: `docker-compose logs web`
2. Ensure all migrations have been applied
3. Verify that the Docker containers are running correctly

## License

[MIT License](LICENSE)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Your Name - sidharthchirathazha@gmail.com

Project Link: [https://github.com/Sidharth-Chirathazha/Notes-App](https://github.com/Sidharth-Chirathazha/Notes-App)
