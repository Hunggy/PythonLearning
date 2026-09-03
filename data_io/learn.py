import json
import csv
# 任务1：json 写入文件
# 目标：把下面的成绩字典保存到 scores.json 文件
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 88}

# 提示：
#   json.dump(字典, 文件对象)  # 写入
#   with open("scores.json", "w", encoding="utf-8") as f:
#       json.dump(scores, f, ensure_ascii=False)
# 注意 encoding="utf-8" 和 ensure_ascii=False 保住中文

# 任务2：读取 json 文件
# 目标：从 scores.json 读回数据并打印
# 提示：json.load(文件对象) 返回原字典

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False)

with open("scores.json", "r", encoding="utf-8") as f:
    loaded_scores = json.load(f)
print(loaded_scores)

with open("scores.csv", "w", newline="", encoding="gbk") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "成绩"])  # 写入表头
    for name, score in scores.items():
        writer.writerow([name, score])  # 写入每一行数据

with open("scores.csv", "r", encoding="gbk") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # 打印每一行数据