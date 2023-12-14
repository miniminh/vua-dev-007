import csv
import json

csv_file = 'preprocessed_data.csv'

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    keys = next(csv_reader)  # Get the first line as keys
    data = [dict(zip(keys, row)) for row in csv_reader]  # Create a list of dictionaries

json_data = json.dumps(data, indent=4)

print(json_data)

with open('output.json', 'w') as json_file:
  json_file.write(json_data)
