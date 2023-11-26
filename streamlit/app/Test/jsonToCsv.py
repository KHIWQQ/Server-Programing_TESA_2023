import csv
import json

# Assuming you have a JSON string or a file path to a JSON file
json_data = '{"w_date":"2007-08-17T00:00:00.000Z","w_height":110.44,"w_cubic":133.4}'

# If you have a file, you can load the JSON data like this:
# with open('path/to/your/file.json') as json_file:
#     json_data = json.load(json_file)

# Parse JSON
data = json.loads(json_data)

# Specify the CSV file path
csv_file_path = 'output.csv'

# Write CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header
    csv_writer.writerow(data.keys())

    # Write data
    csv_writer.writerow(data.values())

print(f"Conversion complete. CSV file saved at: {csv_file_path}")
