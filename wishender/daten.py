import json


def save_list(key, wunsch01, wunsch02,wunsch03, wunsch04):
    file = "data/eingaben.json"
    try:
        with open(file) as open_file:
            content = json.loads(open_file.read())
    except FileNotFoundError:
        content = {}

    content[str(key)] = {"1. Wunsch": wunsch01,# hier wird die speicherstruktur festgelegt / es entsteht ein dict im dict
                         "2. Wunsch": wunsch02,
                         "3. Wunsch": wunsch03,
                         "4. Wunsch": wunsch04}

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4) #hier werden die gespeicherten daten im file "eingaben.json" abgelegt
