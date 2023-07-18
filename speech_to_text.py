import os
import requests

headers = {
    'Authorization': 'Bearer ' + os.getenv('IAM_TOKEN', ''),
    'Content-Type': 'application/x-www-form-urlencoded',
}

params = {
    'folderId': os.getenv('FOLDER_ID', ''),
    'lang': 'ru-RU',
}

with open('speech.ogg', 'rb') as f:
    data = f.read()

response = requests.post('https://stt.api.cloud.yandex.net/speech/v1/stt:recognize', params=params, headers=headers, data=data)