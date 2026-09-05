from flask import Flask
import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'databases')
os.makedirs(DB_DIR , exist_ok = True)
DB_PATH = os.path.join(DB_DIR, 'wrong_notes.db')

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello 错题本"

@app.route('/list')
def get_wrong_notes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT * FROM wrong_notes')
    rows = cur.fetchall()
    conn.close()
    html = "<ul>"
    for row in rows:
        cat, title, content, priority = row[1], row[2], row[3], row[4]
        pri = f"[{priority}] " if priority else ""
        html += f"<li>{pri}<b>[{cat}]</b> {title}"
        if content:
            html += f"：{content}"
        html += "</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    app.run(debug = True)