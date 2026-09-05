import os 
import sqlite3
import re

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'databases')
os.makedirs(DB_DIR , exist_ok = True)
DB_PATH = os.path.join(DB_DIR, 'wrong_notes.db')

def parse_wrong_notes(md_path):
    notes = []
    category = ""
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("## "):
                # 分类：去掉前缀 + 括号说明
                category = re.sub(r"^## \d+\.\s*", "", line).split("（")[0]
            elif line.startswith("- "):
                # 检测重点标记
                priority = ""
                for mark in ("🔴", "⚠️", "🚫"):
                    if mark in line:
                        priority = mark
                        break
                # 提取加粗标题（只在有 **...** 时才进笔记）
                m = re.match(r"-\s*(?:🔴|⚠️|🚫)?\s*(?:\*\*(.+?)\*\*)?\s*[：:]?\s*(.*)", line)
                if not m:
                    continue
                title = m.group(1) or ""
                content = m.group(2).lstrip(' ；;,，。')
                if not title and content:
                    title = content
                    content = ""
                if not title:  # 整行只有 emoji/空白
                    continue
                notes.append((category, title, content, priority))
    return notes

def import_data():
    md_path = os.path.join(BASE_DIR, '..', 'archive', 'wrong_notes.md')
    notes = parse_wrong_notes(md_path)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('DELETE FROM wrong_notes')  # 清空表

    for category, title, content, priority in notes:
        cur.execute('''
        INSERT INTO wrong_notes (category, title, content, priority)
        VALUES (?, ?, ?, ?)
        ''', (category, title, content, priority))

    conn.commit()
    conn.close()
    print(f"导入了 {len(notes)} 条")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS wrong_notes (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,           -- 分类（如"文件操作"）
    title    TEXT,           -- **加粗**的标题
    content  TEXT,           -- 完整内容（去掉 - **title**： 后面的）
    priority TEXT            -- 🔴/⚠️/🚫/空字符串
    )
    ''')

    conn.commit()
    conn.close()
    print(f'数据库已创建:{DB_PATH}')

if __name__ == '__main__':
    init_db()
    import_data()