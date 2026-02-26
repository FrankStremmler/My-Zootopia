import json


JSON_FILE = r"animals_data.json"

 
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as json_reader:
    return json.load(json_reader)

print(JSON_FILE)
animals_data = load_data('animals_data.json')
print(animals_data)
    