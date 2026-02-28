import json


JSON_FILE = r"animals_data.json"
HTLM_TEMPLATE_FILE = r"animals_template.html"
HTML_OUT_FILE = r"animals.html"
REPLACE_TEXT = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as json_reader:
        return json.load(json_reader)


def animal_to_html(animal: dict)->str:
    '''
    Converts the information of one animal into a form for Cards is needed
    :param animal: dict --> element of the list of animals, means one animal
    :return: str --> containig all information of the animal in one string'''
    animal_name: str = animal['name'] # a name can't be optional
    animal_diet: str|None = animal['characteristics'].get('diet', None)
    animal_locations: list|None = animal.get('locations', None)
    animal_type: str|None = animal['characteristics'].get('type', None)

    # <li> is added at the calling function
    # Title is of class card__title displaying the Name inside a <div>-Tag
    # Information of the animal is placed inside a <p>-Tag and from class card__item
    outstr: str = f'<div class="card__title">{animal_name}</div>\n'
    outstr += '<p class="card__text">\n'
    if animal_diet is not None:
       outstr += f"<strong>Diet:</strong> {animal_diet}<br/>\n"
    if animal_locations is not  None:
        outstr += f"<strong>Location:</strong> {animal_locations[0]}<br/>\n"
    if animal_type is not  None:
        outstr += f"<strong>Type:</strong> {animal_type}<br/>\n"
    outstr += '</p>'
    return outstr


def animals_to_html(animals: list)-> str:
    '''
    Formatting the whole list of animals for Card-elemnts in HTML
    :param animals: list --> list of animals read from .json-file
    '''
    outstr: str = ""
    for animal in animals:
        outstr += "<li class=\"cards__item\">\n"
        outstr += f"{animal_to_html(animal)}\n"
        outstr += "</li>\n"
    return outstr


def main():
    '''
    Standard-main, simple and straight
    '''
    # load animal-data from .json-file
    animals_data = load_data('animals_data.json')
    replacestr_new: str = animals_to_html(animals_data)

    # load index.html as Text.
    with open(HTLM_TEMPLATE_FILE, "r") as html_reader:
        html_text = html_reader.read()
    # replacing the text with HTML-Code created
    html_text = html_text.replace(REPLACE_TEXT, replacestr_new)
    # write updated HTML-Code to index.html
    with open(HTML_OUT_FILE, "w") as html_writer:
        html_writer.write(html_text)

if __name__ == "__main__":
    main()
