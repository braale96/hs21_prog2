import json


def save_list(key, wunsch01, wunsch02):
    file = "data/eingaben.json"
    try:
        with open(file) as open_file:
            content = json.loads(open_file.read())
    except FileNotFoundError:
        content = {}

    content[str(key)] = {"1. Wunsch": wunsch01, "2. Wunsch": wunsch02}

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4)
