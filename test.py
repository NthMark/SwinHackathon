import json
import base64
import cv2 
def PCB_defection():
    img = cv2.imread('cat.png')
    _, im_arr = cv2.imencode('.jpg', img)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64
PCB_defection()