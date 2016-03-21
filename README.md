# serious-games-framework

Serious Games Framework

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

Create a database (defaults to Postgres):

```bash
$ createdb serious_games_framework
```

Install requirements:

```bash
$ pip install -r requirements.txt
```

Setup your `DJANGO_SETTINGS_MODULE` to use:

```bash
$ export DJANGO_SETTINGS_MODULE=config.settings.local
```

Sync models to database:

```bash
$ ./manage.py migrate
```

Create a superuser account to access the admin:

```bash
$ ./manage.py createsuperuser
```

Start the web server:

```bash
$ ./manage.py runserver
```

## Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
$ coverage run manage.py test
$ coverage html
$ open htmlcov/index.html
```

### Running tests with py.test

```bash
$ py.test
```

## Celery

This app comes with Celery.

To run a celery worker:

```bash
cd serious_games_framework
celery -A serious_games_framework.taskapp worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Email Server

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use [`MailHog`](https://github.com/mailhog/MailHog) when generating the project a local SMTP server with a web interface will be available.

To start the service, make sure you have nodejs installed, and then type the following:

```bash
$ npm install
$ grunt serve
```

(After the first run you only need to type `grunt serve`) This will start an email server that listens on `127.0.0.1:1025` in addition to starting your Django project and a watch task for live reload.

To view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

The email server will exit when you exit the Grunt task on the CLI with Ctrl+C.
