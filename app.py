from flask import Flask, render_template, request, abort, g, session, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "pet_adoption_secret_key"

# =========================
# DB CONFIG
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "pet_adoption.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


# =========================
# PUBLIC ROUTES
# =========================
@app.route("/")
def index():
    db = get_db()
    pets = db.execute("SELECT * FROM pets").fetchall()
    return render_template("index.html", pets=pets)


@app.route("/knowledge")
def knowledge():
    return render_template("knowledge.html")


@app.route("/adoption")
def adoption():
    page = request.args.get("page", 1, type=int)
    per_page = 3
    offset = (page - 1) * per_page

    db = get_db()

    total = db.execute("SELECT COUNT(*) FROM pets").fetchone()[0]

    pets = db.execute("""
        SELECT * FROM pets
        LIMIT ? OFFSET ?
    """, (per_page, offset)).fetchall()

    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "adoption.html",
        pets=pets,
        page=page,
        total_pages=total_pages
    )


@app.route("/adoption/<int:pet_id>")
def pet_detail(pet_id):
    db = get_db()

    pet = db.execute(
        "SELECT * FROM pets WHERE id=?",
        (pet_id,)
    ).fetchone()

    if pet is None:
        abort(404)

    return render_template("pet_detail.html", pet=pet)


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/login")
def login():
    return render_template("login.html")


# =========================
# REGISTER
# =========================
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form
        db = get_db()

        db.execute("""
            INSERT INTO users
            (username, password, sex, age, telephone, email, address, pic, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
        """, (
            data["username"],
            data["password"],
            data["sex"],
            data["age"],
            data["telephone"],
            data["email"],
            data["address"],
            data["pic"]
        ))

        db.commit()
        return "Register Success 🎉"

    return render_template("register.html")


# =========================
# ADMIN LOGIN
# =========================
@app.route("/admin/login", methods=["POST"])
def admin_login():
    username = request.form.get("username")
    password = request.form.get("password")

    db = get_db()

    admin = db.execute("""
        SELECT * FROM admins 
        WHERE admin_name=? AND admin_password=?
    """, (username, password)).fetchone()

    if admin:
        session["admin"] = True
        session["admin_name"] = username
        return redirect(url_for("admin_dashboard"))
    else:
        return "Login Failed ❌"


@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/login")

    return render_template("admin/dashboard.html")


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect("/login")


# =========================
# ADMIN - ADMINS CRUD
# =========================
@app.route("/admin/admins")
def admin_list():
    db = get_db()
    admins = db.execute("SELECT * FROM admins").fetchall()
    return render_template("admin/admins.html", admins=admins)


@app.route("/admin/admins/add", methods=["POST"])
def add_admin():
    data = request.form
    db = get_db()

    db.execute("""
        INSERT INTO admins
        (admin_name, admin_password, real_name, telephone, email, birthday, gender, profile_image, remark)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["admin_name"],
        data["admin_password"],
        data["real_name"],
        data["telephone"],
        data["email"],
        data["birthday"],
        data["gender"],
        data["profile_image"],
        data["remark"]
    ))

    db.commit()
    return "success"


@app.route("/admin/admins/delete/<int:id>")
def delete_admin(id):
    db = get_db()
    db.execute("DELETE FROM admins WHERE id=?", (id,))
    db.commit()
    return "deleted"


@app.route("/admin/admins/update/<int:id>", methods=["POST"])
def update_admin(id):
    data = request.form
    db = get_db()

    db.execute("""
        UPDATE admins SET
        admin_name=?, admin_password=?, real_name=?, telephone=?, email=?, birthday=?, gender=?, profile_image=?, remark=?
        WHERE id=?
    """, (
        data["admin_name"],
        data["admin_password"],
        data["real_name"],
        data["telephone"],
        data["email"],
        data["birthday"],
        data["gender"],
        data["profile_image"],
        data["remark"],
        id
    ))

    db.commit()
    return "updated"


# =========================
# USERS CRUD
# =========================
@app.route("/admin/users")
def users():
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    return render_template("admin/users.html", users=users)


@app.route("/admin/users/add", methods=["POST"])
def add_user():
    data = request.form
    db = get_db()

    db.execute("""
        INSERT INTO users
        (username, password, sex, age, telephone, email, address, pic, state)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["username"],
        data["password"],
        data["sex"],
        data["age"],
        data["telephone"],
        data["email"],
        data["address"],
        data["pic"],
        0
    ))

    db.commit()
    return "success"


@app.route("/admin/users/delete/<int:id>")
def delete_user(id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id=?", (id,))
    db.commit()
    return "deleted"


@app.route("/admin/users/update/<int:id>", methods=["POST"])
def update_user(id):
    data = request.form
    db = get_db()

    db.execute("""
        UPDATE users SET
        username=?, password=?, sex=?, age=?, telephone=?, email=?, address=?, pic=?
        WHERE id=?
    """, (
        data["username"],
        data["password"],
        data["sex"],
        data["age"],
        data["telephone"],
        data["email"],
        data["address"],
        data["pic"],
        id
    ))

    db.commit()
    return "updated"


# =========================
# PETS CRUD
# =========================
@app.route("/admin/pets")
def pets_list():
    db = get_db()
    pets = db.execute("SELECT * FROM pets").fetchall()
    return render_template("admin/pets.html", pets=pets)


@app.route("/admin/pets/add", methods=["POST"])
def add_pet():
    data = request.form
    file = request.files.get("pic")

    filename = None

    # 保存上传文件
    if file and file.filename != "":
        upload_folder = os.path.join("static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)

        filename = "uploads/" + file.filename
        file.save(os.path.join("static", filename))

    db = get_db()

    db.execute("""
        INSERT INTO pets
        (pet_name, pet_type, sex, birthday, pic, state, remark)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["pet_name"],
        data["pet_type"],
        data["sex"],
        data["birthday"],
        filename,
        data.get("state", 0),
        data.get("remark", "")
    ))

    db.commit()
    return redirect("/admin/pets")


@app.route("/admin/pets/delete/<int:id>")
def delete_pet(id):
    db = get_db()
    db.execute("DELETE FROM pets WHERE id=?", (id,))
    db.commit()
    return "deleted"


@app.route("/admin/pets/update/<int:id>", methods=["POST"])
def update_pet(id):
    data = request.form
    file = request.files.get("pic")

    db = get_db()

    if file and file.filename != "":
        upload_folder = os.path.join("static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)

        filename = "uploads/" + file.filename
        file.save(os.path.join("static", filename))
    else:
        filename = data["old_pic"]

    db.execute("""
        UPDATE pets SET
        pet_name=?, pet_type=?, sex=?, birthday=?, pic=?, state=?, remark=?
        WHERE id=?
    """, (
        data["pet_name"],
        data["pet_type"],
        data["sex"],
        data["birthday"],
        filename,
        data["state"],
        data.get("remark", ""),
        id
    ))

    db.commit()
    return redirect("/admin/pets")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True, port=5001)