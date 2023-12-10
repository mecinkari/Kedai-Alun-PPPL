from flask import Blueprint, jsonify, request
from lib.db import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    cursor = db.cursor()
    sql = f"select * from user where email = '{email}'"
    cursor.execute(sql)
    res = cursor.fetchone()

    cursor.close()
    if res is None:
        return jsonify({"status": "Unauthorized", "msg": f"Data not found"}), 401

    if res[3] != password:
        return jsonify({"status": "Unauthorized Access", "msg": f"Wrong Password"}), 401

    data = {"id": res[0], "nama": res[1],
            "email": res[2], "password": res[3], "role": res[4]}

    return jsonify({"user": data})
