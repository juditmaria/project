# Simple Hello World
""" from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" """

#Modul Hello World
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('helloworld.html')
#