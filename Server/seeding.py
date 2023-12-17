import json
import requests

json_file_path = "./Helper/finalll.json"
url = "http://localhost:9200/vuadev/_doc"

with open(json_file_path, 'r') as file:
    inp = json.load(file)

for data in inp:
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("POST request successful!")
        print("Response:", response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print("Response:", response.text)