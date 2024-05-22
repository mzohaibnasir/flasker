from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from datetime import datetime

# create a flask instance
app = Flask(__name__)

# addd db

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

# initailize db
db = SQLAlchemy(app)

# define model,,what do you want to ave in db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

    data_added = db.Column(db.DateTime, default=datetime.utcnow)

    # create a string

    def __repr__(self):
        return "<Name %r>" % self.name


""" 

The __name__ variable is a special Python variable that represents the current module's name. When __name__ is set to "__main__", it means this file is 
the main module, and the application is being run directly. If the file is being imported as a module in another script, __name__ will be set to the name 
of that module.
"""


"""
Filters:
     Variables can be modified by filters. Filters are separated from the variable by a pipe symbol (|) 
    and may have optional arguments in parentheses. Multiple filters can be chained. The output of one filter is applied to the next.

    -safe  # to render html i.e. stuff variable
    -capitalize
    -lower
    -upper
    -title
    -trim
    -striptags # remove html tags

"""


""" {{}} for variables {% %} for blocks/logic, specify at both start and end """


"""
with forms there is a CSRF(Cross-Site Request Forgery) token. The process of preventing CSRF attacks with CSRF tokens typically involves the following steps:
Token Generation: When a user visits a web application, the server generates a CSRF token. This token is typically a random and unique value that is associated with the user's current session.
Token Inclusion: The CSRF token is then included in the HTML forms that the user interacts with. This is usually achieved by adding the token as a hidden field in the form or embedding it in a 
JavaScript variable.
User Interaction: The user interacts with the web application and submits a form, such as submitting a login form, updating a profile, making a purchase, or performing any other action that 
requires authentication.
Token Submission: When the user submits the form, the CSRF token is automatically sent along with the request, either as a form parameter or as an HTTP header.
Server Validation: Upon receiving the request, the server checks the CSRF token's validity. It verifies that the submitted token matches the expected value for the user's current session and request. 
If the token is missing or does not match, the server can reject the request as a potential CSRF attack.
Action Processing: If the CSRF token is valid, the server processes the user's requested action as usual.
By including a CSRF token with each form submission, the web application ensures that the request originated from the same site and user session, making it difficult for attackers to forge 
malicious requests and execute unauthorized actions on behalf of the user.
"""


app.config[
    "SECRET_KEY"
] = "secretKey"  # WE ARE CREATING AN ENV VARIABLE AND STORE IT IN APP CONFIG

#  Create a form class


class UserForm(FlaskForm):
    name = StringField("Name?", validators=[DataRequired()])
    email = StringField("Email?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create a route decorator// website's endpoint


@app.route("/")
# def index():
#     #  return "<h1>hello World</h1>"
#     return render_template("index.html")


def index():
    first_name = "john"
    stuff = "This is <strong> bold </strong>text"

    favourite_pizza = ["Peperroni", "Cheese", "Mushrooms", 1]

    return render_template(
        "index.html",
        first_name=first_name,
        stuff=stuff,
        favourite_pizza=favourite_pizza,
    )


# we can pass in variables, lists, dicts, objects


# flask already knows its in template directory


#  http://127.0.0.1:5000/user/john
@app.route("/user/<name>")
# <name> tis will allow us to pass a name
def user(name):
    # return "<h1>Hello {}!*</h1>".format(name)
    return render_template("user.html", user_name=name)


# instead of writing code line by line, we create templates.


# custom error pages

# - Invalid URL

print("\n\n\n\n\n\n\n", __name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# - internal server error


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    return render_template("add_user.html")


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = namerForm()
    if form.validate_on_submit() is True:
        """
        if form.validate_on_submit():: This condition checks if the submitted form data is valid. If the request is a POST request and the data
        in the form passes validation rules (if any), the block of code inside the if statement will be executed.
        """
        name = form.name.data
        form.name.data = None
        flash("Form submitted successfully!")
    return render_template("name.html", name=name, form=form)


# flask run to run this

# to eliminate hassle of restarting  server with flask run again and again
#   export FLASK_ENV=development
#   export FLASK_APP=hello.py
#   export FLASK_DEBUG=1

# then flask run
# if __name__ == __main__:
#     app.run(debug=True)
