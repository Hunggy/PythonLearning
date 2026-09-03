# 任务：银行叫号系统（Step 4/6）
# 目标：
#   1. 用 Step 3 的队列模拟银行排队叫号
#   2. 理解队列的真实场景：先来的先服务（FIFO）
#
# 场景：
#   银行只有一个柜台，顾客取号排队。柜台处理完一个，
#   就叫下一个号——永远是最早排队的先被叫到。
#
# 实现（控制台版即可，界面加分）：
#   1. 建一个 Queue
#   2. 模拟几个操作，输出每次操作后的状态：
#      - 新顾客取号："顾客 X 取号，前面还有 N 人"
#      - 柜台叫号："请 A01 号到 1 号窗口"（出队）
#      - 显示当前等待人数
#
# 提示：
#   - 从 queue.py 导入：from queue import Queue  （别忘了它也有 if __name__ 保护）
#   - 顾客编号：A01, A02, A03... 可以用字符串格式化
#       f"A{num:02d}"  → num=1 时输出 "A01"
#   - 加个"操作菜单"，用 input() 让用户选择：
#       1 = 新顾客取号
#       2 = 柜台叫号（出队）
#       3 = 查看等待人数
#       0 = 下班
#     用 while True 循环包起来
#   - 出队前先判断队空不空，空就提示"没有顾客在等"
#
# 真实感加分：柜台处理速度用 time.sleep(1) 模拟 1 秒办一笔

from queue import Queue  # 复用 Step 3 的队列
import time  # 用 time.sleep 模拟处理速度

# ===== TODO: 主程序 =====
# 提示框架：
# 1. q = Queue() 建队
# 2. 取号计数器 num = 1
# 3. while True 菜单循环：
#      choice = input("1取号 2叫号 3查看人数 0下班 > ")
#      if choice == "1": 取号，入队，打印号
#      elif choice == "2": 队空提示，否则出队打印"请 Axx 到 1 号窗口"
#      elif choice == "3": 打印 q.is_empty() / len 等待人数
#      elif choice == "0": break
# 4. 打印"今日营业结束，共服务 X 位顾客"
q = Queue()  # 建队
num = 1  # 取号计数器
served_count = 0  # 服务顾客计数器
while True:
    choice = input("1取号 2叫号 3查看人数 0下班 > ")
    if choice == "1":
        q.enqueue(f"A{num:02d}")  # 入队
        print(f"顾客 A{num:02d} 取号，前面还有 {len(q.items)-1} 人")
        num += 1
    elif choice == "2":
        if q.is_empty():
            print("没有顾客在等")
        else:
            next_customer = q.dequeue()  # 出队
            print(f"请 {next_customer} 到 1 号窗口")
            served_count += 1
            time.sleep(1)  # 模拟处理速度
    elif choice == "3":
        print(f"当前等待人数: {len(q.items)}")
    elif choice == "0":
        break
print(f"今日营业结束，共服务 {served_count} 位顾客")

