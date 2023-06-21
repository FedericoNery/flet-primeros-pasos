import http.client
import json
import requests

class HttpClient:
    def __init__(self):
        self.url_base = "http://127.0.0.1:8000"

    def get(self, url):
        response = requests.get(self.url_base + url)
        return response.json()

    def post(self, url , data): #data es un diccionario
        json_data = json.dumps(data)# conversion de diccionario a json, serializa un objeto a json
        response = requests.post(self.url_base + url, data=json_data)

        if response.status_code == 200:
            print("Data created successfully")
            return response.json()
        else:
            print("Error:", response.status_code)

    def put(self, url, data):
        json_data = json.dumps(data)
        print(json_data)
        print(self.url_base + url)
        response = requests.put(self.url_base + url, data=json_data)
        if response.status_code == 200:
            print("Data updated successfully")
            return response.json()
        else:
            print("Error:", response.status_code)

    def delete(self, url):
        response = requests.delete(self.url_base + url)
        if response.status_code == 204:
            print("Data deleted successfully")
            return response.json()
        else:
            print("Error:", response.status_code)
