from flask import Flask, render_template, request
import os
import sqlite3
import random

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'databases')
os.makedirs(DB_DIR , exist_ok = True)
DB_PATH = os.path.join(DB_DIR, 'wrong_notes.db')

def dict_factory(cursor, row):
    """让 sqlite3 的 fetchall() 返回字典而不是元组"""
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello 错题本"

@app.route('/list')
def get_wrong_notes():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT * FROM wrong_notes')
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', notes=rows)

@app.route('/search')
def search():
    keyword = request.args.get('q', '').strip()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    if keyword:
        cur.execute('SELECT * FROM wrong_notes WHERE title LIKE ? OR content LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
    else:
        cur.execute('SELECT * FROM wrong_notes ORDER BY category, id')
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', notes=rows, keyword=keyword)

@app.route('/category/<path:name>')
def get_notes_by_category(name):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT * FROM wrong_notes WHERE category = ? ORDER BY id', (name,))
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', notes=rows, category=name)

@app.route('/practice')
def practice():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT * FROM wrong_notes')
    all_notes = cur.fetchall()
    conn.close()
    sample = random.sample(all_notes, min(10, len(all_notes)))
    return render_template('practice.html', notes=sample)


if __name__ == '__main__':
    app.run(debug = True)