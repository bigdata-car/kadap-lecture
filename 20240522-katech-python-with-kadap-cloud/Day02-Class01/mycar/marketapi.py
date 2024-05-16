import requests
import json

class Mycar :
    def __init__(self, apikey) :
        self.url = "https://api-gateway.bigdata-car.kr/carinfo/v1"
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": apikey
        }

    def carinfo(self, ownername, reginumber) :
        url = self.url + "/car_info"
        payload = json.dumps({
            "OWNERNAME": ownername,
            "REGINUMBER": reginumber
        })

        res = requests.post(url=url, headers=self.headers, data=payload)
        print(res)

    def owner_verify(self, ownername, reginumber) :
        url = self.url + "/owner_verify"
        payload = json.dumps({
            "OWNERNAME": ownername,
            "REGINUMBER": reginumber
        })

        res = requests.post(url=url, headers=self.headers, data=payload)
