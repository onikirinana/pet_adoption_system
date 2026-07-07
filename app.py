from flask import Flask, render_template, request, abort, g, session, redirect, url_for, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "pet_adoption_secret_key"

# =========================
# DB CONFIG
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "pet_adoption.db")


def api_response(success=True, msg="", data=None, status=200):
    return jsonify({
        "success": success,
        "msg": msg,
        "data": data or {}
    }), status
    
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
# HOME
# =========================
@app.route("/")
def index():
    db = get_db()
    pets = db.execute("SELECT * FROM pets").fetchall()
    return render_template("index.html", pets=pets)


# =========================
# NAVBAR
# =========================
@app.route("/knowledge")
def knowledge():
    return render_template("knowledge.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/register")
def register():
    return render_template("register.html")


# =========================
# LOGIN SYSTEM
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    # ✅ GET：打开页面（原来你缺这个）
    if request.method == "GET":
        return render_template("login.html")

    # POST：登录逻辑（保留你的原逻辑）
    username = request.form.get("username")
    password = request.form.get("password")

    db = get_db()

    user = db.execute("""
        SELECT * FROM users 
        WHERE username=? AND password=?
    """, (username, password)).fetchone()

    if user:
        session["user_id"] = user["id"]
        session["username"] = user["username"]

        return jsonify(success=True, msg="Login success")

    return jsonify(success=False, msg="Invalid credentials")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/check_login")
def check_login():
    return jsonify(logged_in="user_id" in session)

# =========================
# REGISTER SYSTEM
# =========================
@app.route("/register", methods=["POST"])
def register_user():

    data = request.form

    username = data.get("username")
    password = data.get("password")
    sex = data.get("sex")
    age = data.get("age")
    telephone = data.get("telephone")
    email = data.get("email")
    address = data.get("address")
    pic = data.get("pic")

    db = get_db()

    exist = db.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    ).fetchone()

    if exist:
        return jsonify(success=False, msg="Username already exists")

    db.execute("""
        INSERT INTO users
        (username, password, sex, age, telephone, email, address, pic, state)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
    """, (username, password, sex, age, telephone, email, address, pic))

    db.commit()

    return jsonify(success=True, msg="Register success")

# =========================
# ADOPTION APPLY PAGES
# =========================
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

    return render_template(
        "adoption.html",
        pets=pets,
        page=page,
        total_pages=(total + per_page - 1) // per_page
    )

@app.route("/adoption/<int:pet_id>")
def pet_detail(pet_id):
    db = get_db()

    pet = db.execute("SELECT * FROM pets WHERE id=?", (pet_id,)).fetchone()

    if not pet:
        abort(404)

    return render_template("pet_detail.html", pet=pet)


# =========================
# ADOPTION APPLY
# =========================
@app.route("/adoption/apply", methods=["POST"])
def apply_adoption():

    user_id = session.get("user_id")
    if not user_id:
        return jsonify(success=False, msg="Please login first")

    db = get_db()

    pet_id = request.form.get("pet_id")
    message = request.form.get("message")

    db.execute("""
        INSERT INTO applications (user_id, pet_id, message, state)
        VALUES (?, ?, ?, 0)
    """, (user_id, pet_id, message))

    db.commit()

    return jsonify(success=True, msg="Application submitted")


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

    return "Login Failed ❌"


@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/")

    return render_template("admin/dashboard.html")


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect("/")


# =========================
# ADMIN ADOPTION REVIEW
# =========================
@app.route("/admin/adopt")
def admin_adopt_list():

    page = request.args.get("page", 1, type=int)
    apply_time = request.args.get("apply_time", "")

    per_page = 10
    offset = (page - 1) * per_page

    db = get_db()

    # =========================
    # SEARCH FILTER
    # =========================
    params = []
    where_sql = ""

    if apply_time:
        where_sql = "WHERE date(a.apply_time) = ?"
        params.append(apply_time)

    # =========================
    # PAGEEGATION
    # =========================
    total = db.execute(f"""
        SELECT COUNT(*)
        FROM applications a
        {where_sql}
    """, params).fetchone()[0]

    total_pages = (total + per_page - 1) // per_page

    rows = db.execute(f"""
        SELECT 
            a.id,
            u.username,
            p.pet_name,
            a.message,
            a.apply_time,
            a.state
        FROM applications a
        JOIN users u ON a.user_id = u.id
        JOIN pets p ON a.pet_id = p.id
        {where_sql}
        ORDER BY a.apply_time DESC
        LIMIT ? OFFSET ?
    """, params + [per_page, offset]).fetchall()

    return render_template(
        "admin/adopt.html",
        rows=rows,
        page=page,
        total_pages=total_pages,
        apply_time=apply_time
    )

@app.route("/admin/adopt/approve/<int:id>", methods=["POST"])
def approve(id):

    db = get_db()

    db.execute("""
        UPDATE applications
        SET state = 1
        WHERE id = ?
    """, (id,))

    db.commit()

    return api_response(True, "Approved successfully")

@app.route("/admin/adopt/reject/<int:id>", methods=["POST"])
def reject(id):

    db = get_db()

    db.execute("""
        UPDATE applications
        SET state = 2
        WHERE id = ?
    """, (id,))

    db.commit()

    return api_response(True, "Rejected successfully")


@app.route("/admin/adopt/delete/<int:id>", methods=["POST"])
def delete(id):

    db = get_db()

    db.execute("""
        UPDATE applications
        SET state = -1
        WHERE id = ?
    """, (id,))

    db.commit()

    return api_response(True, "Deleted successfully")

# =========================
# APPROVED ADOPTION LIST
# =========================
@app.route("/admin/adopt/approved")
def approved_adopt():

    db = get_db()

    rows = db.execute("""
        SELECT 
            a.id,
            u.username,
            p.pet_name,
            a.message,
            a.apply_time,
            a.state
        FROM applications a
        JOIN users u ON a.user_id = u.id
        JOIN pets p ON a.pet_id = p.id
        WHERE a.state = 1
        ORDER BY a.apply_time DESC
    """).fetchall()

    return render_template(
        "admin/approved.html",
        rows=rows
    )

# =========================
# REJECTED ADOPTION LIST
# =========================
@app.route("/admin/adopt/rejected")
def rejected_adopt():

    db = get_db()

    rows = db.execute("""
        SELECT 
            a.id,
            u.username,
            p.pet_name,
            a.message,
            a.apply_time,
            a.state
        FROM applications a
        JOIN users u ON a.user_id = u.id
        JOIN pets p ON a.pet_id = p.id
        WHERE a.state = 2
        ORDER BY a.apply_time DESC
    """).fetchall()

    return render_template(
        "admin/rejected.html",
        rows=rows
    )

# =========================
# ADMINS CRUD
# =========================

@app.route("/admin/admins")
def admins():
    db = get_db()
    
    admin_id = request.args.get("id")
    admin_name = request.args.get("admin_name")
    gender = request.args.get("gender")
    email = request.args.get("email")
    telephone = request.args.get("telephone")
    real_name = request.args.get("real_name")
    
    sql = """
        SELECT *
        FROM admins
        WHERE 1=1
    """
    params = []
    if admin_id:
        sql += " AND id=?"
        params.append(admin_id)
    if admin_name:
        sql += " AND admin_name LIKE ?"
        params.append("%"+admin_name+"%")
    if gender:
        sql += " AND gender=?"
        params.append(gender)
    if email:
        sql += " AND email LIKE ?"
        params.append("%"+email+"%")
    if telephone:
        sql += " AND telephone LIKE ?"
        params.append("%"+telephone+"%")
    if real_name:
        sql += " AND real_name LIKE ?"
        params.append("%"+real_name+"%")
    admins = db.execute(
        sql,
        params
    ).fetchall()

    return render_template(
        "admin/admins.html",
        admins=admins
    )

@app.route("/admin/admins/add", methods=["POST"])
def add_admin():
    data = request.form
    db = get_db()
    try:
        db.execute("""
            INSERT INTO admins
            (admin_name, admin_password, real_name, telephone, birthday, gender, email, profile_image, remark)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

        """, (
            data.get("admin_name"),
            data.get("admin_password"),
            data.get("real_name"),
            data.get("telephone"),
            data.get("birthday"),
            data.get("gender"),
            data.get("email"),
            data.get("profile_image"),
            data.get("remark")
        ))
        db.commit()
        return api_response(
            True, "Admin created successfully")
    except Exception as e:
        return api_response(
            False,
            str(e),
            status=500
        )
        
@app.route("/admin/admins/update/<int:id>", methods=["POST"])
def update_admin(id):
    data = request.form
    db = get_db()
    try:

        db.execute("""
            UPDATE admins SET
            admin_name=?,
            admin_password=?,
            real_name=?,
            telephone=?,
            birthday=?,
            gender=?,
            email=?,
            profile_image=?,
            remark=?

            WHERE id=?

        """, (
            data.get("admin_name"),
            data.get("admin_password"),
            data.get("real_name"),
            data.get("telephone"),
            data.get("birthday"),
            data.get("gender"),
            data.get("email"),
            data.get("profile_image"),
            data.get("remark"),
            id

        ))

        db.commit()
        return api_response(
            True,
            "Admin updated"
        )
    except Exception as e:

        return api_response(
            False,
            str(e),
            status=500
        )
        
@app.route("/admin/admins/delete/<int:id>")
def delete_admin(id):
    db = get_db()
    try:
        db.execute("""
            DELETE FROM admins
            WHERE id=?
        """, (id,))
        db.commit()
        return api_response(
            True,
            "Admin deleted"
        )
    except Exception as e:
        return api_response(
            False,
            str(e),
            status=500
        )
# =========================
# USERS CRUD
# =========================
@app.route("/admin/users")
def users():
    db = get_db()

    user_id = request.args.get("id")
    username = request.args.get("username")
    sex = request.args.get("sex")
    age = request.args.get("age")
    telephone = request.args.get("telephone")
    email = request.args.get("email")
    address = request.args.get("address")
    state = request.args.get("state")

    sql = """
        SELECT *
        FROM users
        WHERE 1=1
    """
    params = []
    if user_id:
        sql += " AND id=?"
        params.append(user_id)
    if username:
        sql += " AND username LIKE ?"
        params.append("%" + username + "%")
    if sex:
        sql += " AND sex=?"
        params.append(sex)
    if age:
        sql += " AND age=?"
        params.append(age)
    if telephone:
        sql += " AND telephone LIKE ?"
        params.append("%" + telephone + "%")
    if email:
        sql += " AND email LIKE ?"
        params.append("%" + email + "%")
    if address:
        sql += " AND address LIKE ?"
        params.append("%" + address + "%")
    if state:
        sql += " AND state=?"
        params.append(state)
    users = db.execute(
        sql,
        params
    ).fetchall()
    return render_template(
        "admin/users.html",
        users=users
    )
    
@app.route("/admin/users/add", methods=["POST"])
def add_user():
    data = request.form
    db = get_db()

    try:
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
        return jsonify(success=True, msg="User created")

    except Exception as e:
        return jsonify(success=False, msg=str(e))


@app.route("/admin/users/delete/<int:id>")
def delete_user(id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id=?", (id,))
    db.commit()
    return jsonify(success=True, msg="Deleted")


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
    return jsonify(success=True, msg="Updated")


# =========================
# PETS CRUD
# =========================
@app.route("/admin/pets")
def pets_list():

    db = get_db()
    
    pet_id = request.args.get("id")
    pet_name = request.args.get("pet_name")
    pet_type = request.args.get("pet_type")
    sex = request.args.get("sex")
    state = request.args.get("state")

    sql = """
        SELECT *
        FROM pets
        WHERE 1=1
    """
    params = []

    if pet_id:
        sql += " AND id=?"
        params.append(pet_id)

    if pet_name:
        sql += " AND pet_name LIKE ?"
        params.append("%"+pet_name+"%")

    if pet_type:
        sql += " AND pet_type=?"
        params.append(pet_type)

    if sex:
        sql += " AND sex=?"
        params.append(sex)

    if state:
        sql += " AND state=?"
        params.append(state)

    pets = db.execute(
        sql,
        params
    ).fetchall()

    return render_template(
        "admin/pets.html",
        pets=pets
    )

@app.route("/admin/pets/add", methods=["POST"])
def add_pet():
    data = request.form
    file = request.files.get("pic")

    filename = None

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
    return jsonify(success=True, msg="Pet added")


@app.route("/admin/pets/delete/<int:id>")
def delete_pet(id):
    db = get_db()
    db.execute("DELETE FROM pets WHERE id=?", (id,))
    db.commit()
    return jsonify(success=True, msg="Deleted")


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
        filename = data.get("old_pic")

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
    return jsonify(success=True, msg="Updated")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True, port=5001)