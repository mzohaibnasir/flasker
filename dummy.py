from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def index(name):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vowels = ["a", "e", "i", "o", "u"]
    string = " i am an <strong>idiot</strong>, "

    return render_template(
        "dummy.html", name=name, number=number, vowels=vowels, string=string
    )
