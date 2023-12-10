from flask import Blueprint, jsonify, request, send_file
import json
from io import BytesIO
import random
import base64
import os
from matplotlib.figure import Figure
import pandas as pd
from lib.db import db

api = Blueprint("api", __name__)


@api.route("/dashboard", methods=["POST"])
def dashboard():
    files = request.files.get("file")
    df = pd.read_csv(files)

    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.lower()

    sum_total_per_tanggal = []
    tanggal_pembelian = df['tanggal_pembelian'].unique()

    for tanggal in tanggal_pembelian:
        sum_total = int(df[df['tanggal_pembelian'] == tanggal]['total'].sum())
        sum_total_per_tanggal.append({
            'tanggal_pembelian': str(tanggal),
            'sum_total': sum_total
        })

    new_df = df[:5]
    data = new_df.to_json(orient="records")
    new_json = json.loads(data)

    return jsonify({"data": new_json, "row": df.shape[0], "column": df.shape[1], "total_per_tanggal": sum_total_per_tanggal})


@api.route("/new-table-transaction", methods=["POST"])
def new_table_transaction():
    date = request.form.get("date")
    print(date)

    return jsonify({"date": date})

    # cursor = db.cursor()
    # cursor.close()


@api.route("/figure", methods=["GET"])
def figure():
    files = request.files.get("file")
    df = pd.read_csv(files)

    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.lower()

    df = df.drop(['tanggal_pembelian', 'nama_barang',
                 'kuantitas', 'user_id'], axis=1)

    fig = Figure()
    ax = fig.subplots()
    ax.bar(df.columns, df.mean())
    ax.legend()

    buf = BytesIO()
    img_path = os.path.join('static', 'img')
    img_name = random.randint(1000000000, 9999999999)
    fig.savefig(os.path.join(img_path, str(f"{img_name}.png")), format="png")
    # data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return send_file(img_name, mimetype='image/png')
    # return f"<img src=\"data:image/png;base64,{data}\" alt=\"plt\" />"
