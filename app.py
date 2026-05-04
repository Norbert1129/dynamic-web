
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

journeys = []

@app.route("/app/journeys")
def list_journeys():
    return render_template("journeys.html", journeys=journeys)

@app.route("/app/add", methods=["GET", "POST"])
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
        return redirect("/app/journeys")
    return render_template("add.html")
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
