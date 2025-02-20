from todo_app.celery import app

from .service import send


@app.task
def send_register_email(user_email):
    send(user_email)
