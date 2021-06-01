import json


def save_list(key, wunsch01, wunsch02, wunsch03, wunsch04):
    file = "data/eingaben.json"
    try:
        with open(file) as open_file:
            content = json.loads(open_file.read())
    except FileNotFoundError:
        content = {}

    content[str(key)] = {"1. Wunsch": wunsch01,  # hier wird die speicherstruktur festgelegt
                         "2. Wunsch": wunsch02,
                         "3. Wunsch": wunsch03,
                         "4. Wunsch": wunsch04}

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4)  # hier werden die gespeicherten daten im file "eingaben.json" abgelegt


def daten_filter(wuensche):
    file = "data/eingaben.json"
    with open(file) as open_file:
        content = json.loads(open_file.read())

        for key, value in content.items():
            for key2, value2 in value.items():
                for wunsch in wuensche:
                    if wunsch in value2:
                        print(value2)

