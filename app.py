\
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

journeys = []

@app.route("/journeys")
def list_journeys():
    return render_template("journeys.html", journeys=journeys)

@app.route("/add", methods=["GET", "POST"])
def add_journey():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        journey = {
            "id": len(journeys) + 1,
            "title": title,
            "content": content
        }
        journeys.append(journey)
        return redirect("/journeys")
    return render_template("add.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/first")
def first():
     return render_template("journey1.html")

@app.route("/second")
def second():
     return render_template("journey2.html")

@app.route("/third")
def third():
    return render_template("journey3.html")

@app.route("/fourth")
def fourth():
    return render_template("journey4.html")

@app.route("/fifth")
def fifth():
    return render_template("journey5.html")

@app.route("/sixth")
def sixth():
    return render_template("journey6.html")

@app.route("/seventh")
def seventh():
    return render_template("journey7.html")

@app.route("/about")
def about():
    return "About page"

@app.route("/test")
def test():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
