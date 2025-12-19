from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5000/api/message"

@app.route("/")
def index():
    response = requests.get(BACKEND_URL).json()
    return render_template("index.html", message=response["message"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)