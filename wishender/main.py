import flask
from flask import Flask, render_template, request
import json
import daten

app = Flask("Wishender")


def sachen_laden():
    with open("data/eingaben.json") as open_file:
        sachen = json.load(open_file)  # hier wird der Inhalt des "eingabe.json" in "sachen" gespeichert
    return sachen


@app.route("/home", methods=['GET', 'POST'])
def liste_erstellen():
    if request.method == 'POST':
        listen = request.form["liste_auswahl"]
        if daten.listen_filter(listen) == listen:
            listen_auswahl = daten.listen_filter(listen)
            sachen = sachen_laden()
            return render_template("start.html", liste_auswahl=listen_auswahl, listen=sachen)
        key = request.form["liste"]  # hier wird der listenname als key abgefangen und gespeichert
        if key != "":
            wunsch01 = request.form["wunsch01"]  # ab hier werden die wünsche einzeln abgespeichert
            wunsch02 = request.form["wunsch02"]
            wunsch03 = request.form["wunsch03"]
            wunsch04 = request.form["wunsch04"]
            # hier wird die funktion "save_list" ausgeführt und in eintrag gespeichert
            eintrag = daten.save_list(key, wunsch01, wunsch02, wunsch03, wunsch04)
            print(eintrag)
            return flask.redirect("/lists")  # hier wird auf die neue url weitergeleitet
        else:
            warnung = "Bitte einen Listennamen und einen Wunsch definieren!"
            sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt in "sachen" gespeichert
            return render_template("start.html", listen=sachen, warnung=warnung)

    else:
        sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt in "sachen" gespeichert
        return render_template("start.html", listen=sachen)


@app.route("/lists", methods=['GET', 'POST'])
def liste_abhaken():
    if request.method == 'POST':
        checkbox = request.form.getlist("haken")
        test = daten.wunsch_filter(checkbox)
        sachen = sachen_laden()
        return render_template("hello.html", checkbox=checkbox, listen=sachen, test=test)
    else:
        sachen = sachen_laden()  # der return von sachen_laden wird in "sachen" gespeichert
        return render_template("hello.html",
                               listen=sachen)  # "sachen" wird hier für die jinja-logik in "listen" gespeichert


if __name__ == '__main__':
    app.run(debug=True, port=5000)
