import os
from flask import Flask, request
from PIL import Image
# import cv2
import numpy as np
import base64
import io

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api')
def api():
    return 'Hello, API!'
    # file = request.files['image'].read()
    # npimg = np.fromstring(file, np.uint8)
    # img = cv2.imdecode(npimg, 1)

    # if img.shape[:2] == (3024, 4032) or img.shape[:2] == (960, 1280):
    #     img = cv2.resize(img, (806, 605))
    # if img.shape[:2] == (4032, 3024) or img.shape[:2] == (1280, 960):
    #     img = cv2.resize(img, (605, 806))

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # mask1 = np.zeros(img.shape[:2], np.uint8)

    # circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200)

    # for i in circles1[0, :]:
    #     i[2] = i[2]+4
    #     cv2.circle(mask1, (i[0], i[1]), i[2], (255, 255, 255), thickness=-1)

    # masked_data = cv2.bitwise_and(img, img, mask=mask1)
    # _, thresh = cv2.threshold(mask1, 127, 255, cv2.THRESH_BINARY)

    # contours = cv2.findContours(
    #     thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    # x, y, w, h = cv2.boundingRect(contours[0])

    # crop = masked_data[y:y+h, x:x+w]
    # output = crop.copy()

    # gray2 = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    # cimg = cv2.fastNlMeansDenoising(gray2, 5, 10, 5)

    # circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 1, 10, param1=15,
    #                            param2=20, minRadius=10, maxRadius=22)
    # circles = np.uint16(np.around(circles))[0, :]
    # count = 0
    # for i in range(len(circles)):
    #     count = count+1
    #     cv2.circle(output, (circles[i][0], circles[i]
    #                         [1]), circles[i][2], (0, 255, 0), 2)

    # img2 = Image.fromarray(output.astype("uint8"))
    # rawBytes = io.BytesIO()
    # img2.save(rawBytes, "JPEG")
    # rawBytes.seek(0)
    # img_64 = base64.b64encode(rawBytes.read()).decode('utf-8')
    # request_url = request.remote_addr
    # return {"image64": img_64, "points": count}


if __name__ == '__main__':
    app.run(debug=True)
