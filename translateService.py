import requests
import json


class TranslateService:
    url = "http://localhost:5000/translate"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "format": "text",
        "api_key": ""
    }

    def __init__(self, source, target):
        self.payload["source"] = source
        self.payload["target"] = target

    def translate(self, phrase):
        self.payload["q"] = phrase
        return self.__request_libre_translate_api()

    def __request_libre_translate_api(self):
        response = requests.post(url=self.url, data=json.dumps(self.payload), headers=self.headers)
        if response.status_code != 200:
            print("Error:", response.status_code)
        data = response.json()
        return data["translatedText"]
