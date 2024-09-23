from celery import Celery
from transformers import pipeline
import json
celery = Celery(
    "myapp",
    broker="redis://localhost:6379/0",
    backend= "redis://localhost:6379/0"
)

pipe = pipeline("text-generation", model="openai-community/gpt2")


@celery.task()
def PCB_defection(message):
    x={
        'image_link': 'cat.png',
        'no_defection':0,
        'defection_list':'missing hole'
    }
    return json.dumps(x)