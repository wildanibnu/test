from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Fungsi ambil data
def get_data_from_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchone()[0]
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    headers = [col[0] for col in cursor.description]
    conn.close()
    return headers, data, table

# Route utama
@app.route('/')
def index():
    return render_template("index.html", db_name=None)

@app.route('/show_data', methods=['POST'])
def show_data():
    db_name = request.form['db']
    headers, data, table = get_data_from_db(db_name)
    return render_template("index.html", headers=headers, data=data, db_name=db_name, table_name=table)

@app.route('/add_data', methods=['POST'])
def add_data():
    db_name = request.form['db_name']
    if db_name == 'db1.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part1 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))
    elif db_name == 'db2.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part2 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))
    elif db_name == 'db3.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part3 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))
    elif db_name == 'db4.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part4 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))
    elif db_name == 'db5.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part5 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))  
    elif db_name == 'db6.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part6 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))  
    elif db_name == 'db7.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part7 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah)) 
    elif db_name == 'db8.db':
        name = request.form['name']
        email = request.form['email']
        jumlah = request.form['jumlah']
        conn = sqlite3.connect(db_name)
        conn.execute("INSERT INTO part8 (name, email, jumlah) VALUES (?, ?, ?)", (name, email, jumlah))  

    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='192.168.1.8',port=5000)
 