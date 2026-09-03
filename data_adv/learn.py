# 新考点查漏（二）：super() / 类变量 / cur.scroll() / reshape / legend(loc=)
# 任务：分 3 步，每步独立跑通

# ── 第一步：super() + 类变量（继承与共享）──────────────────────
# 做一个"员工系统"：
# ① 类变量 count：记录一共创建了多少个实例（每创建一个 +1）
#    → 定义在 __init__ 外面、class 里面；访问用 类名.count（所有实例共享）
# ② 子类 Manager 继承 Employee：
#    → __init__ 里用 super().__init__(name, salary) 调用父类构造（不用重复写 self.name = ...）
#    → 再补一个经理专属属性 bonus（奖金）
# ③ 打印：创建 2 个普通员工 + 1 个经理后，Employee.count 应该是 3

# 提示（记不住再看）：
# class Employee:
#     count = 0                      # 类变量：所有实例共享
#     def __init__(self, name, salary):
#         self.name = name           # 实例变量：每个实例各有一份
#         self.salary = salary
#         Employee.count += 1        # 每创建一个实例就 +1
# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)   # 调用父类 __init__，父类代码复用
#         self.bonus = bonus
# 访问类变量：Employee.count（类名.count），实例名.count 也能读

# 第一步：写 Employee + Manager 类，创建 3 个实例，打印 count

class Employee:
    count = 0          # 类变量：写在 __init__ 外面，属于"整个类"，所有实例共享
    def __init__(self, name, salary):
        self.name = name      # 实例变量：挂在 self 上，每个实例各有一份
        Employee.count += 1   # 每 new 一个员工，共享的 count 就 +1

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus = bonus

import sqlite3
conn = sqlite3.connect("score.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS stu(id, name, score)")
data =  [(1,'张三',85),(2,'李四',92),(3,'王五',78),(4,'赵六',88),(5,'孙七',95)]
#cur.executemany("INSERT INTO stu VALUES(?,?,?)",data)
conn.commit()
conn.close()


import numpy as np

a = np.array([1,2,3,4,5,6])
b = a.reshape(2, 3)        # 6 个元素 → 2 行 3 列
print(b)                   # [[1 2 3] [4 5 6]]

c = a.reshape(3, 2)        # 3 行 2 列
print(c)                   # [[1 2] [3 4] [5 6]]

d = a.reshape(2, -1)       # -1 = 自动算！2 行 → 自动 3 列
print(d)                   # [[1 2 3] [4 5 6]]

# ── legend(loc=)：图例位置 ──
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), label="cos")
plt.legend(loc="upper right")    # 图例放右上角
plt.show()