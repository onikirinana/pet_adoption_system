from flask import Flask, render_template, request, abort

app = Flask(__name__)


pets = [
    {
        "id": 1,
        "name": "Soju",
        "species": "Dog",
        "breed": "Old English Sheepdog",
        "gender": "Male",
        "birthday": "2021-04-12",
        "image": "images/pets/soju.webp",
        "short_description": "Soju is friendly, energetic, and loves people.",
        "lost_location": "Found near Kings Park, Perth.",
        "personality": "Playful, smart, gentle, and very social.",
        "health_status": "Healthy. No major medical issues found.",
        "vaccinated": "Yes",
        "description": "Soju is a friendly and active dog who enjoys outdoor walks and human company. He was found near Kings Park and has been well cared for since arriving at the rescue center. He is suitable for a family that can provide enough space, exercise, and attention."
    },
    {
        "id": 2,
        "name": "Minnie",
        "species": "Cat",
        "breed": "British Shorthair",
        "gender": "Female",
        "birthday": "2022-09-03",
        "image": "images/pets/minnie.jpeg",
        "short_description": "Minnie is quiet, sweet, and a little shy.",
        "lost_location": "Found near Victoria Park.",
        "personality": "Gentle, calm, shy at first, but very affectionate after trust is built.",
        "health_status": "Healthy. Slightly underweight but recovering well.",
        "vaccinated": "Yes",
        "description": "Minnie is a sweet cat who needs a patient adopter. She may hide when she first arrives at a new home, but she becomes very loving once she feels safe. She is suitable for a quiet home and an adopter who can give her time to adjust."
    },
    {
        "id": 3,
        "name": "Kena",
        "species": "Cat",
        "breed": "Domestic Shorthair",
        "gender": "Male",
        "birthday": "2020-11-18",
        "image": "images/pets/kena.webp",
        "short_description": "Kena is warm, friendly, and curious.",
        "lost_location": "Found near Cannington Station.",
        "personality": "Curious, confident, friendly, and enjoys being around people.",
        "health_status": "Healthy and active.",
        "vaccinated": "No",
        "description": "Kena is a confident and curious cat who enjoys exploring his surroundings. He likes attention and adapts quickly to new environments. He would be a good match for adopters who want an interactive and friendly companion."
    },
    {
        "id": 4,
        "name": "Luna",
        "species": "Dog",
        "breed": "Golden Retriever",
        "gender": "Female",
        "birthday": "2021-06-25",
        "image": "images/pets/luna.jpg",
        "short_description": "Luna is loving, calm, and family-friendly.",
        "lost_location": "Found near Scarborough Beach.",
        "personality": "Loyal, gentle, patient, and good with children.",
        "health_status": "Healthy. Regular check-up completed.",
        "vaccinated": "Yes",
        "description": "Luna is a gentle dog with a calm personality. She enjoys walks, people, and quiet family time. She would be suitable for a family or an adopter looking for a loyal and affectionate pet."
    },
    {
        "id": 5,
        "name": "Oreo",
        "species": "Cat",
        "breed": "Tuxedo Cat",
        "gender": "Male",
        "birthday": "2023-01-10",
        "image": "images/pets/oreo.jpeg",
        "short_description": "Oreo is playful and full of energy.",
        "lost_location": "Found near Northbridge.",
        "personality": "Active, playful, curious, and funny.",
        "health_status": "Healthy. Needs routine vaccination update.",
        "vaccinated": "No",
        "description": "Oreo is a young and playful cat who loves toys and climbing. He has a lot of energy and would enjoy a home with enough space and interaction. He is best suited for someone who enjoys playful pets."
    },
    {
        "id": 6,
        "name": "Coco",
        "species": "Rabbit",
        "breed": "Holland Lop",
        "gender": "Female",
        "birthday": "2022-03-08",
        "image": "images/pets/coco.webp",
        "short_description": "Coco is soft, quiet, and easy to care for.",
        "lost_location": "Surrendered by previous owner.",
        "personality": "Quiet, gentle, relaxed, and likes clean spaces.",
        "health_status": "Healthy.",
        "vaccinated": "Yes",
        "description": "Coco is a gentle rabbit who enjoys a quiet environment. She needs a clean living area, fresh vegetables, and gentle handling. She is suitable for adopters who understand rabbit care."
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
    page = request.args.get("page", 1, type=int)
    per_page = 3

    total_pets = len(pets)
    total_pages = (total_pets + per_page - 1) // per_page

    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page
    current_pets = pets[start:end]

    return render_template(
        "adoption.html",
        pets=current_pets,
        page=page,
        total_pages=total_pages
    )

@app.route("/adoption/<int:pet_id>")
def pet_detail(pet_id):
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)

    if pet is None:
        abort(404)

    page = request.args.get("page", 1, type=int)

    return render_template("pet_detail.html", pet=pet, page=page)


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