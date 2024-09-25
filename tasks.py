from celery import Celery
from transformers import pipeline
import json
import base64
import cv2 
celery = Celery(
    "myapp",
    broker="redis://localhost:6379/0",
    backend= "redis://localhost:6379/0"
)

pipe = pipeline("text-generation", model="openai-community/gpt2")


@celery.task()
def PCB_defection(message):
    img = cv2.imread('cat.png')
    _, im_arr = cv2.imencode('.jpg', img)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64
    # return json.dumps(x)