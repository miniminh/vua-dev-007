#Conver url -> array of url 
import json

# Read JSON data
with open('finalll.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to convert URL string to array
def convert_url_to_array(url):
    return url.split('~')

# Iterate through each item in the JSON data and modify the URLs
for item in data:
    if 'url' in item:  # Check if 'url' key exists in the item
        item['url'] = convert_url_to_array(item['url'])

# Write the modified data back to the JSON file
with open('final.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("URLs converted and saved to modified_data.json")
