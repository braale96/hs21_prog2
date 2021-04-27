from flask import Flask
from flask import render_template
from flask import request

app = Flask("Wishender")

@app.route("/start/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['Liste']
        rueckgabe_string = ziel_person + ":"
        return rueckgabe_string
    return render_template("start.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
