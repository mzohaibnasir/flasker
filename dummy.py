from flask import Flask, render_template, flash

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired

app = Flask(__name__)


app.config[
    "SECRET_KEY"
] = "secretKey"  # WE ARE CREATING AN ENV VARIABLE AND STORE IT IN APP CONFIG


class fForm(FlaskForm):
    name = StringField("Name?")
    submit = SubmitField("Submit?")


@app.route("/")
def index():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vowels = ["a", "e", "i", "o", "u"]
    string = " i am an <strong>idiot</strong>, "

    return render_template("dummy.html", number=number, vowels=vowels, string=string)


@app.route("/form", methods=["GET", "POST"])
def form():
    name = None
    form = fForm()
    if form.validate_on_submit() is True:
        name = form.name.data
        form.name.data = ""
        flash(", form submitted!")
    return render_template("dummyForm.html", name=name, form=form)
