import json

# Replace with the correct filename you see in your data folder
file_path = "data/annotation_20250712_090623.json"

# Open and load the JSON file
with open(file_path, "r") as file:
    form_data = json.load(file)

# Display the loaded data
print("Loaded Form Data:")
print(json.dumps(form_data, indent=2))