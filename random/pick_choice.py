import random
import time

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
picked = []  # 已抽过的人

while len(picked) < len(names):
    # 在「没被抽过」的人里随机选
    available = [n for n in names if n not in picked]
    name = random.choice(available)

    for n in range(3, 0, -1):
        print(n)
        time.sleep(1)
    print("轮到:", name)
    picked.append(name)  # 记录已抽过

    if len(picked) == len(names):
        print("一轮完毕")
        break
    if input("按回车继续 / 输入 q 退出: ").lower() == "q":
        print("退出程序")
        break