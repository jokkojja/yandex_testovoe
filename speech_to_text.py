import requests
import config

class SpeechToText:
    def __init__(self):
        self.__PARAMS = config.PARAMS
        self.__HEADERS = config.HEADERS
    
    def voice_to_text(self, voice_data):
        response = requests.post('https://stt.api.cloud.yandex.net/speech/v1/stt:recognize', params=self.__PARAMS, headers=self.__HEADERS, data=voice_data)
        text = response.json()['result']
        return text
