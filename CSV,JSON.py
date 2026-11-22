
import csv
import json

# Reading data from CSV file
with open("input.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Converting CSV data into JSON format
json_data = json.dumps(data, indent=4)

# Writing JSON data into output file
with open("output.json", "w") as json_file:
    json_file.write(json_data)

print("CSV data successfully converted into JSON!")
