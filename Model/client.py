import requests

url = "http://localhost:14024/api/upload"

payload = {}
files=[
  ('input',('test1.jpg',open('test1.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
