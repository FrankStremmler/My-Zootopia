import json


JSON_FILE = r"animals_data.json"

 
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as json_reader:
    return json.load(json_reader)
  
  
def print_animal(animal: dict)->None:
  '''
  Prints the information of one animal
  :param animal: dict --> element of the list of animals
  '''
  animal_name: str = animal.get('name', None)
  animal_diet: str = animal['characteristics'].get('diet', None)
  animal_locations: str = animal.get('locations', None)
  animal_type: str = animal['characteristics'].get('type', None)
  
  if animal_name !=  None:
    print(f"Name: {animal_name}")
  if animal_diet !=  None:
    print(f"Diet: {animal_diet}")
  if animal_locations!=  None:
    print(f"Location: {animal_locations[0]}")
  if animal_type!=  None:
    print(f"Type: {animal_type}")
  print()
    
    
print(JSON_FILE)
animals_data = load_data('animals_data.json')
#print(animals_data)
for animal in animals_data:
  print_animal(animal)

  
    