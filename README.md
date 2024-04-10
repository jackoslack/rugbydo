# rugbydo

This is a Django project that will run on DigitOcean App Platform.

## Configuration

You need to provide a number of environment variables

## Development

In development, you can use a `.env` file in the root of the project instead of environment variable files.

A typical setup will look like:

```ini
DEBUG=True
SECRET_KEY=django-insecure-r-io#@p!=jg5ckjks+d_a&=6@!la^7s6)=ou=ey0r^zs*i%1-3
DATABASE_URL=sqlite:///db.sqlite3
```

If you want to use a _real_ database, you can start up a PostgreSQL instance using `docker compose`.

    docker compose up -d

This will be accessible on port `5555` (editable in `docker-compose.yml`) and can be accessed with the following environment variable:

```ini
DATABASE_URL=postgresql://rugby:rugby@localhost:5555/rugby
```

You will need to populate your database.

    python manage.py migrate

To login to the admin interface you will need a superuser account.

    python manage.py createsuperuser --username admin
