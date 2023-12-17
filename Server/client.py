import requests
import re

def getSuggest(filename):
    url = "http://localhost:14024/api/upload"

    payload = {}
    files=[
    ('input',('kk.png',open(filename,'rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return (response.json())

def extract_image_id(file_path):
    img_name = file_path[file_path.rfind('\\') + 1: file_path.find('.')]
    return img_name.split('_')[0]

def getRecord(id):
    url = "http://localhost:9200/vuadev/_search"
    query = {
        "query": {
            "match": {
                "ID": id
            }
        }
    }
    response = requests.get(url, json=query, headers={'Content-Type': 'application/json'})

    # Check the response
    # if response.status_code == 200:
    #     print("POST request successful!")
    #     print("Response:", response.json())
    # else:
    #     print("POST request failed. Status code:", response.status_code)
    #     print("Response:", response.text)
    return response.json()