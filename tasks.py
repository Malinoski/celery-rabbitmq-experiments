from celery import Celery
from time import sleep

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672', backend='db+sqlite:///db.slite3')

@app.task
def reverse(text):
    sleep(4)
    return text[::-1]
