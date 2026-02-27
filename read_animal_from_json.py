import json


JSON_FILE = r"animals_data.json"
HTLM_TEMPLATE_FILE = r"animals_template.html"
HTML_OUT_FILE = r"animals.html"
REPLACE_TEXT = "__REPLACE_ANIMALS_INFO__"

 
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
    
    
def animal_to_string(animal: dict)->str:
  '''
  Prints the information of one animal
  :param animal: dict --> element of the list of animals, means one animal
  :return: str --> containig all information of the animal in one string'''
  animal_name: str = animal.get('name', None)
  animal_diet: str = animal['characteristics'].get('diet', None)
  animal_locations: str = animal.get('locations', None)
  animal_type: str = animal['characteristics'].get('type', None)
  
  outstr: str = ""
  if animal_name !=  None:
    outstr += f"Name: {animal_name}\n"
  if animal_diet !=  None:
    outstr += f"Diet: {animal_diet}\n"
  if animal_locations!=  None:
    outstr += f"Location: {animal_locations[0]}\n"
  if animal_type!=  None:
    outstr += f"Type: {animal_type}\n"
  return outstr

  
def animals_to_string(animals: dict)-> str:
  outstr = ""
  for animal in animals:
    outstr += animal_to_string(animal)
    outstr += "\n"
  return outstr


def animal_to_html(animal: dict)->str:
  '''
  Converts the information of one animal into a form : Name:...<br/>...Typa:...<br/> 
  :param animal: dict --> element of the list of animals, means one animal
  :return: str --> containig all information of the animal in one string'''
  animal_name: str = animal.get('name', None)
  animal_diet: str = animal['characteristics'].get('diet', None)
  animal_locations: str = animal.get('locations', None)
  animal_type: str = animal['characteristics'].get('type', None)
  
  outstr: str = ""
  if animal_name !=  None:
    outstr += f"Name: {animal_name}<br/>"
  if animal_diet !=  None:
    outstr += f"Diet: {animal_diet}<br/>"
  if animal_locations!=  None:
    outstr += f"Location: {animal_locations[0]}<br/>"
  if animal_type!=  None:
    outstr += f"Type: {animal_type}<br/>"
  return outstr

  
def animals_to_html(animals: dict)-> str:
  outstr: str = ""
  for animal in animals:
    outstr += "<li class=\"cards__item\">"
    outstr += animal_to_html(animal)
    outstr += "</li>"
  return outstr
    

animals_data = load_data('animals_data.json')
#print(animals_data)
#for animal in animals_data:
#  print_animal(animal)

replacestr_new = animals_to_html(animals_data)
with open(HTLM_TEMPLATE_FILE, "r") as html_reader:
  html_text = html_reader.read()
html_text = html_text.replace(REPLACE_TEXT, replacestr_new)
with open(HTML_OUT_FILE, "w") as html_writer:
  html_writer.write(html_text)
   
  
    