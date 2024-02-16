# test_task_django_bot
# Django Telegram Bot

This project is created to register users via Telegram bot and send them messages.

## Requirements

1. Python 3.x
2. Django 3.x
3. aiogram 2.x

## Installation Instructions

1. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # for Linux/Mac
    .\env\Scripts\activate   # for Windows
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a Django superuser for accessing the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. Create a `.env` file based on the `.env.sample` file provided and enter the Telegram bot token.

## Usage

1. Start the Django server:

    ```bash
    python manage.py runserver
    ```

2. Run the bot:

    ```bash
    python manage.py bot
    ```

3. Open the Django admin panel in your browser at `http://localhost:8000/admin/` and log in with your credentials.

4. In the admin panel, you can view and manage registered users, as well as send them messages via the bot.

## Running with Shell Scripts (Experimental)

There are also options to run the project using `.sh` files, but they are still in testing.

## Project Features

1. Registration of users(one or many) via the Telegram bot.
2. Sending messages to registered users via the bot.
3. Ability to manage users through the Django admin panel.

## TODO

1. Add the ability to send messages to all users using Celery.
2. Refactor code
## Author

Petrykiv Dmytro / petrykiv.dmytro19@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<p align="center">
<img style="width: 100%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>