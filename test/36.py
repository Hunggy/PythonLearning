import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# 任务1：修改成绩（示例：将1班张三数学成绩改为135）
update_sql = "UPDATE scores SET math = ? WHERE class = ? AND name = ?"
cursor.execute(update_sql, (135, '1班', '张三'))
conn.commit()

# 任务2：统计各班数学>120分人数
cursor.execute("SELECT class FROM scores WHERE math > 120")
results = cursor.fetchall()               # 拿到全部查询结果
class_counts = {}
for row in results:
    class_name = row[0]
    if class_name in class_counts:
        class_counts[class_name] += 1                 # 这个班已经出现过 → 计数+1
    else:
        class_counts[class_name] = 1

# 任务3：格式化输出结果
print("各班数学高分统计：")
for class_name, count in class_counts:        # 遍历字典的键值对
    print(f"{class_name.ljust(6)}: {'★'*count}")

cursor.close()
conn.close()