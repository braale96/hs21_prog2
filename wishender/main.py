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
        key = request.form["liste"]  # hier wird der listenname als key abgefangen und gespeichert
        wunsch01 = request.form["wunsch01"]  # ab hier werden die wünsche einzeln abgespeichert
        wunsch02 = request.form["wunsch02"]
        wunsch03 = request.form["wunsch03"]
        wunsch04 = request.form["wunsch04"]
        eintrag = daten.save_list(key, wunsch01, wunsch02, wunsch03, wunsch04)  # hier wird die funktion "save_list" ausgeführt und in eintrag gespeichert
        print(eintrag)
        return flask.redirect("/lists")  # hier wird, nach durchlaufen der if-schlaufe auf eine neue url (/lists) weitergeleitet

    else:
        sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt und der return in "sachen" gespeichert
        return render_template("start.html", listen=sachen)


@app.route("/lists", methods=['GET', 'POST'])
def output():
    sachen = sachen_laden()  # hier wird die funktion "sachen_laden" ausgeführt und der return in "sachen" gespeichert
    return render_template("hello.html", listen=sachen)  # "sachen" wird hier für jinja in "listen" gespeichert


if __name__ == '__main__':
    app.run(debug=True, port=5000)
