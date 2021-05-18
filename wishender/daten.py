import json

def save_list(key, eintrag):
    file = "data/eingaben.json"
    try:
        with open(file) as open_file:
           content = json.loads(open_file.read())
    except FileNotFoundError:
        content = {}

    content[str(key)] = {"liste": eintrag}

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4)


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value
