from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json():
    with open("products.json", "r") as j:
        return json.load(j)

def load_csv():
    data = []
    with open("products.csv", "r") as c:
        reader = csv.DictReader(c)
        for row in reader:
            data.append(row)
    return data

def load_sqlite():
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    data = []
    for row in rows:
        data.append(dict(row))
    return data

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    loaders = {
        "json": load_json,
        "csv": load_csv,
        "sql": load_sqlite
    }

    if source not in loaders:
        return render_template("product_display.html",
                               products=[],
                               error="Wrong source")

    products = loaders[source]()

    if product_id:
        filtered = []
        pid = int(product_id)

        for p in products:
            if int(p["id"]) == pid:
                filtered.append(p)

        if not filtered:
            return render_template("product_display.html",
                                   products=[],
                                   error="Product not found")

        products = filtered

    return render_template("product_display.html",
                           products=products,
                           error=None)

app.run(host="127.0.0.1", port=5000)