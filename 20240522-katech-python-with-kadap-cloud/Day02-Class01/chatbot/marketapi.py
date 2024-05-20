import requests
import json

class Mychatbot :
    def __init__(self, apikey) :
        self.url = "https://api-gateway.bigdata-car.kr/chatbot/v1/chatbot"
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": apikey
        }

    def chatbot(self, prompt, user_id) :
        payload = json.dumps({
            "user_id": user_id,
            "prompt": prompt
        })

        # print(f"user_id: {user_id}, prompt: {prompt}")

        res = requests.post(url=self.url, headers=self.headers, data=payload)
        return res.json()