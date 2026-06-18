from flask import Flask, render_template

app = Flask(__name__)


pets = [
    {
        "id": 1,
        "name": "Milo",
        "species": "Cat",
        "breed": "British Shorthair",
        "age": 2,
        "gender": "Male",
        "status": "Available"
    },
    {
        "id": 2,
        "name": "Bella",
        "species": "Dog",
        "breed": "Golden Retriever",
        "age": 3,
        "gender": "Female",
        "status": "Available"
    },
    {
        "id": 3,
        "name": "Luna",
        "species": "Rabbit",
        "breed": "Holland Lop",
        "age": 1,
        "gender": "Female",
        "status": "Adopted"
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/knowledge")
def knowledge():
    return render_template("knowledge.html")


@app.route("/adoption")
def adoption():
    return render_template("adoption.html", pets=pets)


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)