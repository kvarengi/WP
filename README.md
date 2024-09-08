# N-Options

## Running the project

The project requires `poetry` - python packager and dependency manager:

```sh
brew install poetry # macOS
poetry install # in project root

# Or
poetry update # in project root to update packages
```

Run with:

```sh
# To run telegram bot
poetry run python -m binary_options_bot

# To run webapp
poetry run python ./binary_options_webapp/manage.py makemigrations core # if db is not initialized
poetry run python ./binary_options_webapp/manage.py migrate # if db is not initialized
poetry run python ./binary_options_webapp/manage.py runserver

# You may also create superuser with
poetry run python ./binary_options_webapp/manage.py createsuperuser
```

## Required environment variables

`TELEGRAM_BOT_TOKEN` - Telegram bot token

`WEBAPP_URL` - URL of the hosted telegram webapp page
