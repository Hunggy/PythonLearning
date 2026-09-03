import random
import time

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
random.shuffle(names)

for i, name in enumerate(names):
    for n in range(3, 0, -1):
        print(n)
        time.sleep(1)
    print("轮到:", name)
    time.sleep(1)
    if i == len(names) - 1:
        print("一轮完毕")
        break
    if input("按回车继续 / 输入 q 退出: ").lower() == "q":
        print("退出程序")
        break
