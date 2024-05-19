from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index,.html')

@app.route("/players")
def players():
    return render_template("players.html")

@app.route("/coaches")
def coaches():
    return render_template("coaches.html")
