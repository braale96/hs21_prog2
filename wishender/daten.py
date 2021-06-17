import json


def save_list(key, wunsch01, wunsch02, wunsch03, wunsch04):
    file = "data/eingaben.json"
    try:
        with open(file) as open_file:
            content = json.loads(open_file.read())
    except FileNotFoundError:  # sollte das File nicht gefunden werden
        content = {}  # wird ein neues, leeres File erstellt

    content[str(key)] = {"1. Wunsch": wunsch01,  # hier wird die speicherstruktur festgelegt
                         "2. Wunsch": wunsch02,
                         "3. Wunsch": wunsch03,
                         "4. Wunsch": wunsch04}

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4)  # hier werden die gespeicherten daten im file "eingaben.json" abgelegt


def save_checkbox(auswahl):
    file = "data/checked.json"
    with open(file, "r") as open_file:
        content = json.loads(open_file.read())  # hier wird der Inhalt vom checked.json in content gespeichert
        content.clear()  # das ganze wird direkt gelöscht
        for i in auswahl:
            if i not in content:
                content[str(i)] = "abgehakt"  # und mit dem neuen Inhalt überschrieben
                # dies geht nur weil auch die bestehenden haken jedes Mal erneut übermittelt werden

    with open(file, "w") as open_file:
        json.dump(content, open_file, indent=4)  # der neue content wird ins File abgelegt


def listen_filter(liste):
    file = "data/eingaben.json"

    with open(file, "r") as open_file:
        content = json.loads(open_file.read())  # hier wird der Inhalt vom eingaben.json in content gespeichert

        for key, value in content.items():
            if key in liste:  # sofern der key (aus dem Dropdown Formular) vorhanden ist
                return key  # wird er zurückgegeben

# Funktion ist nicht zwingend notwendig, aber eine Sicherheitsstufe. Der Key sollte aber in jedem Fall vorhanden sein
