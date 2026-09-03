import sqlite3
conn = sqlite3.connect("demo.db")
cur = conn.cursor()

# ── 1. CREATE 建表（DDL：自动提交，不用 commit）──
cur.execute("CREATE TABLE IF NOT EXISTS stu(id INTEGER, name TEXT, score REAL)")

# ── 2. INSERT 插入（DML：要 commit 才落盘）──
cur.execute("INSERT INTO stu VALUES(1, '张三', 85)")          # 全列
cur.execute("INSERT INTO stu(id, name) VALUES(2, '李四')")    # 指定列（score 空）
cur.executemany("INSERT INTO stu VALUES(?,?,?)",
                [(3,'王五',78),(4,'赵六',88),(5,'孙七',95)])   # 批量
conn.commit()                                                  # ← 别忘！

# ── 3. SELECT 查询（不用 commit）──
cur.execute("SELECT * FROM stu")                 # 全查
print(cur.fetchall())

cur.execute("SELECT name, score FROM stu WHERE score >= 80")   # 条件
cur.execute("SELECT * FROM stu ORDER BY score DESC")           # 降序排序
cur.execute("SELECT * FROM stu ORDER BY score DESC LIMIT 2")   # 前 2 名
cur.execute("SELECT COUNT(*), AVG(score), MAX(score) FROM stu")  # 聚合

# ── 4. UPDATE 更新（DML：要 commit）──
cur.execute("UPDATE stu SET score = 90 WHERE name = '张三'")  # 改指定行
cur.execute("UPDATE stu SET score = score + 5")               # 所有人加分
conn.commit()

# ── 5. DELETE 删除（DML：要 commit）──
cur.execute("DELETE FROM stu WHERE id = 2")      # 删指定行
cur.execute("DELETE FROM stu")                   # 清空数据（表还在）
conn.commit()

# ── ⭐ 6. 参数化 ? 占位（防注入，考试必考）──
# 永不拼字符串！值用 ? 占位，第二个参数传元组
cur.execute("SELECT * FROM stu WHERE score >= ?", (80,))
cur.execute("UPDATE stu SET score = ? WHERE id = ?", (100, 1))
cur.execute("INSERT INTO stu VALUES(?,?,?)", (6, '测试', 60))
conn.commit()
conn.close()