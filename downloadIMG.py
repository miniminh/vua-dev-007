import os
import json
import requests

jsonfile = 'output.json'
finalfile = 'finalll.json'

def download_images(image_urls, output_folder, item_name):
    successful_downloads = []
    temp = []
    for image in image_urls:
        try:
            response = requests.get(image)
            if response.status_code == 200:
                temp.append({
                    'image_url': image,
                    'content': response.content
                })
        except Exception as e:
            print(f"Error downloading {image}: {e}")

    for idx, image_url in enumerate(temp, start=1):
        try:
            file_extension = image_url['image_url'].split('.')[-1]  # Get file extension from URL
            file_name = f"{item_name}_{idx}.{file_extension}"
            file_path = os.path.join(output_folder, file_name)
            os.makedirs(output_folder, exist_ok=True)  # Ensure the directory exists
            with open(file_path, 'wb') as file:
                file.write(image_url['content'])  # Fixed content download
            #print(f"Downloaded: {file_name}")
            successful_downloads.append(image_url['image_url'])
        except Exception as e:
            print(f"Error downloading {image_url['image_url']}: {e}")

    return successful_downloads

current_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_directory, jsonfile)
output_folder = os.path.join(current_directory, 'downloaded_images')

with open(json_file_path, 'r') as file:
    data = json.load(file)

for index, item in enumerate(data, start=1):
    image_urls = []

    if '|' in item['images']:
        image_urls = item['images'].split(' | ')
    elif '~' in item['images']:
        image_urls = item['images'].split('~')
    else:
        image_urls = [item['images']]

    item_name = item['ID']

    if image_urls:
        successful_downloads = download_images(image_urls, output_folder, item_name)
        item['images'] = successful_downloads

final_json_path = os.path.join(current_directory, finalfile)
with open(final_json_path, 'w') as file:
    json.dump(data, file, indent=2)
