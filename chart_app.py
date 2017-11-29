"""A quick demo to show how to dynamically generate a webpage using the Google
Charts API with the Flask web framework.
Run charts.py and then connect to http://localhost:5000/charts/ in your
browser."""

from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
app = Flask(__name__)

@app.route('/chart/')
def chart():
	# The data can come from anywhere you can read it; for instance, a SQL
	# query or a file on the filesystem created by another script.
	# This example expects two values per row; for more complicated examples,
	# refer to the Google Charts gallery.
	data = [('Sunday', 48), ('Monday', 27), ('Tuesday', 32), ('Wednesday', 42),
			('Thursday', 38), ('Friday', 45), ('Saturday', 52)]
	return render_template('chart.html', data=data)

@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]

    return render_template('test.html', **locals())

if __name__ == '__main__':
	# Automatically detect changes to charts.py and reload the server as
	# necessary.
	app.run(debug=True)