from flask import Flask
from flask import render_template
from flask import request


app = Flask("Hello")


@app.route("/hello/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Liste 01 " + ziel_person + "!"
        return rueckgabe_string
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
