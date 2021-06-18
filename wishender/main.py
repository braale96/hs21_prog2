import flask
from flask import Flask, render_template, request
import json
import daten

app = Flask("Wishender")


def sachen_laden():
    with open("data/eingaben.json") as open_file:
        sachen = json.load(open_file)  # hier wird der Inhalt des "eingabe.json" in "sachen" gespeichert
    return sachen


def wuensche_laden():
    with open("data/checked.json") as open_file:
        checked_wishes = json.load(open_file)  # hier wird der Inhalt des "checked.json" in "checked_wishes" gespeichert
    return checked_wishes


@app.route("/home", methods=['GET', 'POST'])
def liste_erstellen():
    if request.method == 'POST':  # wenn das Formular abgesendet wurde
        listen = request.form["liste_auswahl"]  # hier wird der Input vom Dropdown (mit allen Keys) entgegengenommen
        key = request.form["liste"]  # hier wird der listenname als key abgefangen und gespeichert
        if daten.listen_filter(listen) == listen:
            listen_auswahl = daten.listen_filter(listen)  # better double-check that ^^
            sachen = sachen_laden()
            return render_template("start.html", liste_auswahl=listen_auswahl, listen=sachen)  # speichern für jinja
        elif key != "":
            wunsch01 = request.form["wunsch01"]  # ab hier werden die wünsche einzeln abgespeichert
            wunsch02 = request.form["wunsch02"]
            wunsch03 = request.form["wunsch03"]
            wunsch04 = request.form["wunsch04"]
            # hier wird die funktion "save_list" ausgeführt und in eintrag gespeichert
            eintrag = daten.save_list(key, wunsch01, wunsch02, wunsch03, wunsch04)
            print(eintrag)
            return flask.redirect("/lists")  # hier wird auf die neue url weitergeleitet
        elif request.form["action"] == "Zu allen Listen":  # der Button mit value “Zu allen Listen"
            return flask.redirect("/lists")
        else:
            warnung = "Bitte einen Listennamen und einen Wunsch definieren!"  # Kein Input gibt eine Warnung
            sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt in "sachen" gespeichert
            return render_template("start.html", listen=sachen, warnung=warnung)

    else:
        sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt in "sachen" gespeichert
        return render_template("start.html", listen=sachen)


@app.route("/lists", methods=['GET', 'POST'])
def liste_abhaken():
    if request.method == 'POST':
        checkbox = request.form.getlist("haken")  # alle abgehakten Wünsche werden als Liste gespeichert
        daten.save_checkbox(checkbox)  # um sie permanent zu speicher werden sie in dies Funktion gegeben
        if request.form["action"] == "Zur Startseite":
            return flask.redirect("/home")
        elif checkbox:  # sofern eine Checkbox angewählt ist
            erfuellt = wuensche_laden()  # alle gespeicherten Haken
            sachen = sachen_laden()  # alle gespeicherten Listen inklusive Wünsche
            return render_template("lists.html", checkbox=checkbox, listen=sachen, erfuellt=erfuellt)
        else:
            erfuellt = wuensche_laden()
            sachen = sachen_laden()
            return render_template("lists.html", checkbox=checkbox, listen=sachen, erfuellt=erfuellt)
    else:
        erfuellt = wuensche_laden()
        sachen = sachen_laden()
        return render_template("lists.html", listen=sachen, erfuellt=erfuellt)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

# QUELLEN
# https://pwp.stevecassidy.net/bottle/forms-processing.html
# https://stackabuse.com/building-a-todo-app-with-flask-in-python
# https://pythonbasics.org/flask-template-data/
# https://www.w3schools.com/python/python_json.asp
# https://tutorialdeep.com/knowhow/delete-multiple-items-dictionary-python/
