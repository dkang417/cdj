from flask import Flask, render_template, request,redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/ninja')
def ninja():
	return render_template("ninja.html")

@app.route('/ninja/<ninja_color>')
def ninjaReveal(ninja_color):
        return render_template("turtles.html",color=ninja_color)
	

app.run(debug=True)