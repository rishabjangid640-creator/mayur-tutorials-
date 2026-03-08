from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS enquiries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        course TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    course = request.form["course"]
    message = request.form["message"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO enquiries(name,phone,email,course,message) VALUES(?,?,?,?,?)",
        (name,phone,email,course,message)
    )

    conn.commit()
    conn.close()

    return "Enquiry Submitted Successfully!"

@app.route("/admin")
def admin():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM enquiries")
    data = cur.fetchall()

    conn.close()

    return render_template("admin.html", data=data)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)
