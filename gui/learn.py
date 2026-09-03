import tkinter as tk
import random
# 任务1：显示一个空白窗口
# 1. tk.Tk() 创建主窗口
# 2. window.mainloop() 让窗口保持显示（程序阻塞在这里等事件）

window = tk.Tk()

label = tk.Label(window, text="你好, Python GUI!")
label.pack()

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

def 抽人():
    global countdown
    countdown = 3
    tick()

def tick():
    global countdown
    if countdown > 0:
        label.config(text=countdown)
        countdown -= 1
        window.after(1000, tick)      # 循环调度自己
    else:
        label.config(text=random.choice(names))

countdown = 0

button = tk.Button(window, text="点名", command=抽人)  # command= 绑定点击事件
button.pack()






window.mainloop()