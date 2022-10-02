from flask import Flask, make_response,render_template,request,redirect,send_from_directory
import requests
from cryptography.fernet import Fernet
from tool import Downloader
app= Flask(__name__)

key = b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
fernet = Fernet(key)
app.config['UPLOAD_FOLDER'] = "static"

def encrypt(text):
	encodedtext = fernet.encrypt(text.encode())
	return encodedtext.decode()


def decrypt(text):
	encodedtext = fernet.decrypt(text.encode())
	return encodedtext.decode()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    q= request.args.get("q")
    out = Downloader.downloadvideo(q)
    response = make_response({"done":True,"out":out.split("static/")[1]})
    response.set_cookie("file",str(encrypt(str(out.split("static/")[1]))))
    return response
@app.route("/complete")
def completedownload():
    filename = request.cookies.get("file")
    if filename != None:
        filename = decrypt(filename)
        return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=filename,as_attachment=True)
app.run(debug=True)