from flask import Flask, render_template, request
import json
import daten


app = Flask("Wishender")


@app.route("/home", methods=['GET', 'POST'])

def liste_erstellen():
    if request.method == 'POST':
        key = request.form["liste"]
        eintrag = request.form["liste"]
        eintrag = daten.save_list(key, eintrag)
        print(eintrag)
        return "test erfolgreich"
    return render_template("start.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

