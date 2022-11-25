from flask import Flask

app = Flask(
    __name__)  # __name__ is "magic" variable that we can always call and it refers to a file we are curently working with


@app.route("/")
def hello_world():
    return "<p>Hello gracious people!</p>"


@app.route("/about/<username>")
def about_page(username):
    return f'<h1>This is a about page for {username}</h1>'
