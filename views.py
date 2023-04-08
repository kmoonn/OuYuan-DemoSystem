from flask import Flask, render_template


@main.route("/")
def index():
	return render_template("index.html")