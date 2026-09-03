import sqlite3

# 任务1：连接数据库 + 创建表
# 目标：
#   1. sqlite3.connect("students.db") 连接（没有文件会自动创建）
#   2. 创建 students 表：id(编号) name(姓名) score(成绩)
# 提示：
#   conn = sqlite3.connect("students.db")
#   cur = conn.cursor()           # 游标：执行SQL命令的"手"
#   cur.execute("""CREATE TABLE IF NOT EXISTS students (
#       id INTEGER PRIMARY KEY,
#       name TEXT,
#       score INTEGER
#   )""")
#   conn.commit()                 # 提交事务（保存修改）
#   conn.close()                  # 关闭连接
#
# 跑完检查：文件夹里出现 students.db 文件
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}
conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score INTEGER
)""")
"""
for name, score in scores.items():
    cur.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
"""
cur.execute("SELECT name, score FROM students WHERE score > ?", (85,))
rows = cur.fetchall()
print("成绩大于85的学生：", rows)

cur.execute("SELECT name, score FROM students WHERE id = ?", (1,))
row = cur.fetchone()
print("第一条记录：", row)

cur.execute("UPDATE students SET score = ? WHERE name = ?", (90, "张三"))

cur.execute("DELETE FROM students WHERE name = ?", ("李四",))

conn.commit()
conn.close()

