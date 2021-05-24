import flask
from flask import Flask, render_template, request, redirect
import json
import daten

app = Flask("Wishender")

def sachen_laden():
    with open("data/eingaben.json") as open_file:
        sachen = json.load(open_file)
    return sachen

@app.route("/home", methods=['GET', 'POST'])

def liste_erstellen():
    if request.method == 'POST':
        key = request.form["liste"]
        wunsch01 = request.form["wunsch01"]
        wunsch02 = request.form["wunsch02"]
        eintrag = daten.save_list(key, wunsch01, wunsch02)
        print(eintrag)
        return flask.redirect("/lists")
    return render_template("start.html")


@app.route("/lists", methods=['GET', 'POST'])
def output():
    sachen = sachen_laden()
    return render_template("hello.html", listen=sachen)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



