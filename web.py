from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about_page():
    return "<p>Wow this is easy!</p><h1>Hmm?</h1>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
