import random
import time

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

random.shuffle(names)

for x in names:
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    print("轮到:",x)
    time.sleep(1)
    if x == names[-1]:
        print("一轮完毕")
    user_input = input("按回车继续 / 输入 q 退出: ")
    if user_input.lower() == 'q':
        print("退出程序")
        break



