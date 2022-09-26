from flask import Flask,render_template,request,redirect
import youtube_dl
import requests

app = Flask(__name__)
@app.route("/")
def index():
	return "Index page"

app.run(debug=True)