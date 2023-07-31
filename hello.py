from flask import Flask, render_template


# create a flask instance
app = Flask(__name__)

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


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# - internal server error


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# flask run to run this

# to eliminate hassle of restarting  server with flask run again and again
#   export FLASK_ENV=development
#   export FLASK_APP=hello.py
#   export FLASK_DEBUG=1

# then flask run
