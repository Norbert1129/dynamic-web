
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/app/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "About page"

@app.route("/app/test")
def test():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
