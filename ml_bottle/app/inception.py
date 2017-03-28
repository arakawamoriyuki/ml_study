# coding: utf-8
from json import dumps
import datetime, os

import requests
from bottle import Bottle, request, response
from PIL import Image, ImageFile

from inception_v3 import run_inference_on_image

# TRUNCATED画像も読み込む
ImageFile.LOAD_TRUNCATED_IMAGES = True

# 複数のPOSTを受けるのでtmpファイルに日付を入れる
TMP_IMAGE = '/tmp/inception_tmp_{}.jpg'

inception_app = Bottle()


# GETで画像urlを渡して分類を判定する。ContentType:multipart/form-data
@inception_app.get('/inception')
def get_inception():
    # request image url
    response = requests.get(request.params.image, stream=True)

    path = image_path()

    # save image
    with open(path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    # scan
    result = inception_scan(path)

    response.content_type = 'application/json'
    return dumps(result)


# POSTで画像binaryを渡して分類を判定する。ContentType:multipart/form-data
@inception_app.post('/inception')
def post_inception():
    # request image binary
    image = request.files.get('image')

    path = image_path()

    # save image
    image.save(path, overwrite=True, chunk_size=1024)

    # scan
    result = inception_scan(path)

    response.content_type = 'application/json'
    return dumps(result)


# apiテスト用View
@inception_app.get('/inception/test')
def get_inception_test():
    return '''
<form action="/inception" method="post" enctype="multipart/form-data">
    <input type="submit">
    <input type="file" name="image">
</form>
'''


def image_path():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H:%M:%S.%f")
    return TMP_IMAGE.format(now)

def convert(path, format='jpeg'):
    image = Image.open(path)
    image.save(path, format)

def inception_scan(path):
    # convert jpeg
    convert(path, 'jpeg')
    # classify image
    result = run_inference_on_image(path)
    # delete tmp image
    os.remove(path)

    return result
