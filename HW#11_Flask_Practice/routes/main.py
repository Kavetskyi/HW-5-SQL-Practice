from app import app
from helpers.file import get_users, write_users
from flask import render_template, request, redirect


@app.route("/")
def main():
    users = get_users()
    return render_template("index.html", users=users)


@app.route("/user_add")
def user_add():
    return render_template("user_add.html")


@app.route("/users", methods=["POST"])
def save_user():
    users = get_users()
    val_id = 1
    if len(users) > 0:
        val_id = len(users) + 1
    user = {
        "id": val_id,
        "email": request.form.get("email"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "work_area": request.form.get("work_area")
    }
    users.append(user)
    write_users(users)
    return redirect("/")


@app.route("/user_edit/<int:val_id>")
def edit_user(val_id):
    users = get_users()
    for user in users:
        if user["id"] == val_id:
            return render_template("user_add.html", user=user)
    return redirect("/")


@app.route("/users/<int:val_id>", methods=["POST"])
def update(val_id):
    users = get_users()
    for user in users:
        if user["id"] == val_id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("work_area")

    write_users(users)
    return redirect("/")


@app.route("/users/delete/<int:val_id>")
def delete_user(val_id):
    users = get_users()
    users_new = []
    id_new = 0
    for user in users:
        if user["id"] != val_id:
            id_new = id_new + 1
            user_new = {
                "id": id_new,
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "work_area": user["work_area"]
            }
            users_new.append(user_new)
    users = users_new
    write_users(users)
    return redirect("/")


@app.route("/user_search")
def user_search():
    return render_template("user_search.html")


@app.route("/users/search", methods=["GET"])
def search():
    users = get_users()
    users_new = []
    for user in users:
        if user["email"] == request.args.get("email"):
            user_new = {
                "id": 1,
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "work_area": user["work_area"]
            }
            users_new.append(user_new)

    users = users_new
    return render_template("index.html", users=users)
