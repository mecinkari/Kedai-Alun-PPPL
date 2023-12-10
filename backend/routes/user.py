from flask import Blueprint, jsonify, request
from lib.db import db

user = Blueprint("user", __name__)


@user.route("/get-all", methods=["GET"])
def get_all():
    data = []
    cursor = db.cursor()
    sql = f"select * from user"
    cursor.execute(sql)

    res = cursor.fetchall()

    for i in res:
        data.append({"id": i[0], "nama": i[1],
                    "email": i[2], "password": i[3], "role": i[4]})

    cursor.close()
    return jsonify({"user": data})


@user.route("/get/<int:id>", methods=["GET"])
def get(id):
    cursor = db.cursor()
    sql = f"select * from user where id = {id}"
    cursor.execute(sql)
    res = cursor.fetchone()

    if res is None:
        return jsonify({"status": "error", "msg": f"Data not found"}), 404

    data = {"id": res[0], "nama": res[1],
            "email": res[2], "password": res[3], "role": res[4]}
    cursor.close()

    return jsonify({"user": data})


@user.route("/create", methods=["POST"])
def create():
    nama = request.form.get("nama")
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role") or 2

    cursor = db.cursor()
    check_email_sql = f"select * from user where email = '{email}'"
    cursor.execute(check_email_sql)
    res = cursor.fetchone()

    if (res):
        return {"status": "error", "msg": f"Email already exist"}, 402

    sql = f"insert into user (nama, email, password, role) VALUES ('{nama}', '{email}', '{password}', {role})"
    cursor.execute(sql)
    db.commit()

    cursor.close()
    return jsonify({"status": "success", "msg": f"{cursor.rowcount} row inserted"})


@user.route("/update/<int:id>", methods=["POST"])
def update(id):
    nama = request.form.get("nama")
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role") or 2

    cursor = db.cursor()
    sql = f"update user set nama = '{nama}', email = '{email}', password = '{password}', role = {role} where id = {id}"
    cursor.execute(sql)
    db.commit()

    cursor.close()
    return jsonify({"status": "success", "msg": f"{cursor.rowcount} row(s) affected"})


@user.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    cursor = db.cursor()
    sql = f"delete from user where id = {id}"
    cursor.execute(sql)
    db.commit()

    cursor.close()
    return jsonify({"status": "success", "msg": f"{cursor.rowcount} row(s) deleted"})
