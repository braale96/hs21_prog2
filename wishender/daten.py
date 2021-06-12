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


def wunsch_filter(wuensche):
    file = "data/eingaben.json"

    with open(file, "r") as open_file:
        content = json.loads(open_file.read())

        for key, value in content.items():
            print("Liste:" + key)
            for key2, value2 in value.items():
                if value2 in wuensche:
                    print("Wunsch: " + value2 + " erfüllt")
                    #content.pop(value2)
                    #return content

    #with open(file, "w") as open_file:
        #json.dump(content, open_file, indent=4)


def listen_filter(liste):
    file = "data/eingaben.json"

    with open(file, "r") as open_file:
        content = json.loads(open_file.read())

        for key, value in content.items():
            if key in liste:
                return key
