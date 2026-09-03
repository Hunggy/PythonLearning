# 拼音学习工具：第一步 = 韵母学习卡 + 第二步 = 辨识测试（占位）
# 结构：菜单页 / 学习卡页 / 测试页（Frame 切换）

import tkinter as tk
import random
import sqlite3
import datetime
import matplotlib.pyplot as plt 
from pinyin_data import pin_list

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

conn = sqlite3.connect("wrong_notes.db")    # 自动创建文件
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS wrong_notes (
    yunmu TEXT,
    char TEXT,
    wrong_count INTEGER DEFAULT 1,
    PRIMARY KEY (yunmu, char)
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS rounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    score INTEGER
)""")
conn.commit()

# ── 韵母数据（24 个）──────────────────────────────────────────
yunmu_list = [
    {"yunmu": "a",  "type": "单韵母",   "examples": [("阿", "ā")]},
    {"yunmu": "o",  "type": "单韵母",   "examples": [("哦", "ó")]},
    {"yunmu": "e",  "type": "单韵母",   "examples": [("鹅", "é")]},
    {"yunmu": "i",  "type": "单韵母",   "examples": [("衣", "yī")]},
    {"yunmu": "u",  "type": "单韵母",   "examples": [("乌", "wū")]},
    {"yunmu": "ü",  "type": "单韵母",   "examples": [("鱼", "yú"), ("女", "nǚ")]},
    {"yunmu": "ai", "type": "复韵母",   "examples": [("爱", "ài"), ("开", "kāi")]},
    {"yunmu": "ei", "type": "复韵母",   "examples": [("杯", "bēi"), ("飞", "fēi")]},
    {"yunmu": "ui", "type": "复韵母",   "examples": [("水", "shuǐ"), ("对", "duì")]},
    {"yunmu": "ao", "type": "复韵母",   "examples": [("包", "bāo"), ("高", "gāo")]},
    {"yunmu": "ou", "type": "复韵母",   "examples": [("狗", "gǒu"), ("头", "tóu")]},
    {"yunmu": "iu", "type": "复韵母",   "examples": [("球", "qiú"), ("六", "liù")]},
    {"yunmu": "ie", "type": "复韵母",   "examples": [("叶", "yè"), ("姐", "jiě")]},
    {"yunmu": "üe", "type": "复韵母",   "examples": [("月", "yuè"), ("学", "xué")]},
    {"yunmu": "er", "type": "卷舌韵母", "examples": [("耳", "ěr"), ("二", "èr")]},
    {"yunmu": "an", "type": "前鼻韵母", "examples": [("安", "ān"), ("半", "bàn")]},
    {"yunmu": "en", "type": "前鼻韵母", "examples": [("门", "mén"), ("人", "rén")]},
    {"yunmu": "in", "type": "前鼻韵母", "examples": [("心", "xīn"), ("音", "yīn")]},
    {"yunmu": "un", "type": "前鼻韵母", "examples": [("村", "cūn"), ("春", "chūn")]},
    {"yunmu": "ün", "type": "前鼻韵母", "examples": [("云", "yún"), ("军", "jūn")]},
    {"yunmu": "ang", "type": "后鼻韵母", "examples": [("昂", "áng"), ("帮", "bāng")]},
    {"yunmu": "eng", "type": "后鼻韵母", "examples": [("灯", "dēng"), ("风", "fēng")]},
    {"yunmu": "ing", "type": "后鼻韵母", "examples": [("星", "xīng"), ("听", "tīng")]},
    {"yunmu": "ong", "type": "后鼻韵母", "examples": [("龙", "lóng"), ("红", "hóng")]},
]

# ── 主窗口 ────────────────────────────────────────────────────
root = tk.Tk()
root.title("拼音学习工具")
screen_w = root.winfo_screenwidth()    # 屏幕宽度
screen_h = root.winfo_screenheight()   # 屏幕高度
win_w, win_h = 720, 920
x = (screen_w - win_w) // 2
y = (screen_h - win_h) // 2

root.geometry(f"{win_w}x{win_h}+{x}+{y}")
# ── 三个页面容器（Frame）───────────────────────────────────────
menu_frame = tk.Frame(root)
card_frame = tk.Frame(root)
test_frame = tk.Frame(root)
wrong_frame = tk.Frame(root)
pin_frame = tk.Frame(root)

def show_wrong():
    cur.execute("SELECT yunmu, char, wrong_count FROM wrong_notes ORDER BY wrong_count DESC LIMIT 5")
    rows = cur.fetchall()
    text = "\n".join(f"{y}  {c}  ❌{n}次" for y, c, n in rows) or "暂无错题 🎉"
    wrong_list.config(text=text)
    show(wrong_frame)


def show(frame):
    """显示指定页面，隐藏其他页面"""
    menu_frame.pack_forget()
    card_frame.pack_forget()
    test_frame.pack_forget()
    wrong_frame.pack_forget()
    pin_frame.pack_forget()
    frame.pack()

def plot_score():
    plt.close()
    cur.execute("SELECT date , score FROM rounds ORDER BY id")
    rows = cur.fetchall()
    if not rows:
        return
    dates = [r[0] for r in rows]
    scores = [r[1] for r in rows]
    plt.plot(dates , scores ,marker = "o")
    plt.ylim(0,10)
    plt.title('测试得分曲线')
    plt.xlabel("日期")
    plt.ylabel("得分")
    plt.show()

def plot_wrong():
    plt.close()
    cur.execute("SELECT yunmu , wrong_count FROM wrong_notes ORDER BY wrong_count DESC LIMIT 8")
    rows = cur.fetchall()
    if not rows:
        return  
    name = [r[0] for r  in rows]
    num = [r[1] for r in rows]
    plt.bar(name , num , color = "red", edgecolor="black", hatch="//")
    plt.title("最容易错的韵母")
    plt.show()

# ── 菜单页 ─────────────────────────────────────────────────────
tk.Label(menu_frame, text="拼音学习工具", font=("Microsoft YaHei", 36)).pack(pady=100)
tk.Button(menu_frame, text="韵母学习卡", font=("Microsoft YaHei", 24),
          command=lambda: show(card_frame)).pack(pady=10)
tk.Button(menu_frame, text="韵母辨识测试", font=("Microsoft YaHei", 24),
          command=lambda: show(test_frame)).pack(pady=10)
# 菜单页加按钮
tk.Button(menu_frame, text="错题本", font=("Microsoft YaHei", 24),
          command=show_wrong).pack(pady=10)
tk.Button(menu_frame, text = "成绩曲线", font=("Microsoft YaHei", 24),
          command=plot_score).pack(pady=10)
tk.Button(menu_frame, text = "错题排行图", font=("Microsoft YaHei", 24),
          command=plot_wrong).pack(pady=10)
tk.Button(menu_frame, text="拼音打字练习", font=("Microsoft YaHei", 24),
          command=lambda: show(pin_frame)).pack(pady=10)
# ── 学习卡页（原逻辑搬入，父容器 root → card_frame）──────────────
tk.Label(card_frame, text="韵母学习卡", font=("Microsoft YaHei", 48)).pack()
tk.Label(card_frame, text=" ", font=("Microsoft YaHei", 48)).pack()
yun_mu = tk.Label(card_frame, text="None", font=("Microsoft YaHei", 48))
yun_mu.pack()
type_label = tk.Label(card_frame, text="None", font=("Microsoft YaHei", 48))
type_label.pack()
example = tk.Label(card_frame, text="None None", font=("Microsoft YaHei", 48))
example.pack()
tk.Label(card_frame, text=" ", font=("Microsoft YaHei", 48)).pack()

count = 1
def prev():
    global count
    if count != 1:
        count -= 1
    else:
        count = 24
    new()

def next_card():
    global count
    if count != 24:
        count += 1
    else:
        count = 1
    new()

btn_frame = tk.Frame(card_frame)
btn_frame.pack()    # Frame 自己居中（pack 默认居中！）
tk.Button(btn_frame, text="上一个", command=prev, font=("Microsoft YaHei", 24)).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="下一个", command=next_card, font=("Microsoft YaHei", 24)).pack(side=tk.LEFT, padx=5)

number = tk.Label(card_frame, text=f"第{count}/24个", font=("Microsoft YaHei", 24))
number.pack()

def new():
    yun_mu.config(text=yunmu_list[count-1]["yunmu"])
    type_label.config(text=yunmu_list[count-1]["type"])
    text = "  ".join(f"{字} {拼音}" for 字, 拼音 in yunmu_list[count-1]["examples"])
    example.config(text=text)
    number.config(text=f"第{count}/24个")

new()
tk.Button(card_frame, text="← 返回菜单", font=("Microsoft YaHei", 16),
          command=lambda: show(menu_frame)).pack()

# ── 测试页（占位，第二步填逻辑）─────────────────────────────────
topic = random.sample(yunmu_list, 10)
score = 0
answered = False

def restart():
    global topic, count1, score, answered
    topic = random.sample(yunmu_list, 10)   # 重新抽 10 题
    count1 = 1
    score = 0
    answered = False
    score_label.config(text=f"得分：{score}")
    new1()


def new1():
    global count1, answered,字
    answered = False        # ← 换新题：解锁
    item = topic[count1 - 1]                 # 当前题
    字, 拼音 = random.choice(item["examples"])  # 随机例子字
    chinese.config(text=字)
    number1.config(text=f"第{count1}/10题")

    options = [item["yunmu"]]                # 正确答案
    others = [x["yunmu"] for x in yunmu_list if x != item]
    options += random.sample(others, 3)      # 3 个干扰
    random.shuffle(options)                  # 打乱

    for btn, opt in zip([anser1, anser2, anser3, anser4], options):
        btn.config(text=opt, command=lambda y=opt: check(y))  # lambda 固定参数！

    response.config(text= "快点给我答😡😡😡",fg="black")
    score_label.config(text=f"得分：{score}")


def check(chosen):
    global score, answered
    if answered:
        return
    answered = True
    item = topic[count1 - 1]
    if chosen == item["yunmu"]:
        score += 1
        response.config(text="✓ 答对了！", fg="green")
    else:
        response.config(text=f"✗ 错了，答案是 {item['yunmu']}", fg="red")
        # ← 新增：记错题（参数化 ? 防注入）
        cur.execute("""INSERT INTO wrong_notes (yunmu, char, wrong_count)
                       VALUES (?, ?, 1)
                       ON CONFLICT(yunmu, char)
                       DO UPDATE SET wrong_count = wrong_count + 1""",
                    (item["yunmu"], 字))
        conn.commit()
    score_label.config(text=f"得分：{score}")

count1 = 1
def next_topic():
    global count1
    if count1 != 10:
        count1 += 1
        new1()
    else:
        response.config(text=f"本轮完成！得分：{score}/10")
        cur.execute("INSERT INTO rounds (date , score) VALUES (?,?)",(str(datetime.date.today()),score))
        conn.commit()


tk.Label(test_frame, text="韵母辨识测试", font=("Microsoft YaHei", 48)).pack(pady=30)
chinese = tk.Label(test_frame, text="None", font=("Microsoft YaHei", 48))
chinese.pack()
number1 = tk.Label(test_frame, text=f"第{count1}/10题", font=("Microsoft YaHei", 24))
number1.pack()
btn_frame1 = tk.Frame(test_frame)
btn_frame1.pack(pady=30)    # Frame 自己居中（pack 默认居中！）
anser1 = tk.Button(btn_frame1 , text="None" , font=("Microsoft YaHei", 24))
anser1.pack(side=tk.LEFT, padx=50)
anser2 = tk.Button(btn_frame1 , text="None" , font=("Microsoft YaHei", 24))
anser2.pack(side=tk.LEFT, padx=50)
btn_frame2 = tk.Frame(test_frame)
btn_frame2.pack()    # Frame 自己居中（pack 默认居中！）
anser3 = tk.Button(btn_frame2 , text="None" , font=("Microsoft YaHei", 24))
anser3.pack(side=tk.LEFT, padx=50)
anser4 = tk.Button(btn_frame2 , text="None" , font=("Microsoft YaHei", 24))
anser4.pack(side=tk.LEFT, padx=50)

response = tk.Label(test_frame ,text = '快点给我答😡😡😡' , font=("Microsoft YaHei", 24))
response.pack()
score_label = tk.Label(test_frame ,text=f"得分：{score}" , font=("Microsoft YaHei", 24))
score_label.pack()
btn_frame3 = tk.Frame(test_frame)
btn_frame3.pack()  
tk.Button(btn_frame3, text="下一题", command=next_topic, font=("Microsoft YaHei", 24)).pack(side="left")
tk.Button(btn_frame3, text="刷新", command=restart, font=("Microsoft YaHei", 24)).pack(side="left",padx= 30)
new1()
tk.Button(test_frame, text="← 返回菜单", font=("Microsoft YaHei", 16),
          command=lambda: show(menu_frame)).pack()
# ── 错题页─────────────────────────────────
tk.Label(wrong_frame, text="错题排行", font=("Microsoft YaHei", 36)).pack(pady=20)
wrong_list = tk.Label(wrong_frame, text="test", font=("Microsoft YaHei", 24))
wrong_list.pack(pady=30)
tk.Button(wrong_frame, text="← 返回菜单", font=("Microsoft YaHei", 16),
          command=lambda: show(menu_frame)).pack()
# ── 打字页 ───────────────────────────────────────────────────────
topic1 = random.sample(pin_list, 10)
score1 = 0
answered1 = False
count2 = 1

def check1_enter(event):
    check1(pin.get().strip().lower())    # 复用你写好的判定！

def new2():
    global answered1
    answered1 = False 
    Zhi.config(text=topic1[count2 - 1]['char'])
    respon.config(text="快点给我答😡😡😡",fg="black")
    score_label1.config(text=f"得分：{score1}")
    number2.config(text=f"第{count2}/10题")
    pin.delete(0, tk.END)
    pin.focus()

def next_topic1(event=None):
    global count2
    if count2 != 10:
        count2 += 1
        new2()
    else:
        respon.config(text=f"本轮完成！得分：{score1}/10")
        # 记录本轮成绩（画曲线用，与辨识测试共用 rounds 表）
        cur.execute("INSERT INTO rounds (date , score) VALUES (?,?)",(str(datetime.date.today()),score1))
        conn.commit()

def check1(written):
    global score1, answered1
    if answered1:
        return
    answered1 = True
    item = topic1[count2 - 1]
    if written == item["input"]:
        score1 += 1
        respon.config(text=f"✓ 对了！ {item['py']} = {item['sm']} + {item['ym']}", fg="green")
    else:
        respon.config(text=f"✗ 错了！ {item['py']} = {item['sm']} + {item['ym']}", fg="red")
        # 答错也记入错题本（复用 wrong_notes 表）
        cur.execute("""INSERT INTO wrong_notes (yunmu, char, wrong_count)
                       VALUES (?, ?, 1)
                       ON CONFLICT(yunmu, char)
                       DO UPDATE SET wrong_count = wrong_count + 1""",
                    (item["ym"], item["char"]))
        conn.commit()
    score_label1.config(text=f"得分：{score1}")

def restart1(event=None):
    global topic1, count2, score1, answered1
    topic1 = random.sample(pin_list, 10)  # 重新抽 10 题
    count2 = 1
    score1 = 0
    answered1 = False
    score_label1.config(text=f"得分：{score1}")
    new2()


tk.Label(pin_frame, text="拼音打字练习", font=("Microsoft YaHei", 48)).pack(pady=30)
Zhi = tk.Label(pin_frame, text="None", font=("Microsoft YaHei", 48))
Zhi.pack(pady = 15)
tk.Label(pin_frame, text="请输入它的拼音:", font=("Microsoft YaHei", 24)).pack()
pin = tk.Entry(pin_frame , width="15" , font=("Microsoft YaHei", 24))
pin.pack(pady=5)
tk.Button(pin_frame , text = "提交" , font=("Microsoft YaHei", 24),command=lambda:check1(pin.get().strip().lower())).pack(pady=5)
respon = tk.Label(pin_frame , text= 'None' , font=("Microsoft YaHei", 24))
respon.pack(pady= 10)
btn_frame4 = tk.Frame(pin_frame)
btn_frame4.pack(pady=5)
score_label1 = tk.Label(btn_frame4 ,text=f"得分：{score1}" , font=("Microsoft YaHei", 24))
score_label1.pack(side="left")
number2 = tk.Label(btn_frame4 ,text=f"第{count2}/10题" , font=("Microsoft YaHei", 24))
number2.pack(side ="left" , padx = "30")
btn_frame5 = tk.Frame(pin_frame)
btn_frame5.pack(pady=15)
tk.Button(btn_frame5, text="下一题", command=next_topic1, font=("Microsoft YaHei", 24)).pack(side="left")
tk.Button(btn_frame5, text="刷新", command=restart1, font=("Microsoft YaHei", 24)).pack(side="left",padx= 30)
pin.bind("<Return>", check1_enter)
pin.bind("<Left>", restart1)
pin.bind("<Right>", next_topic1)
tk.Button(pin_frame, text="← 返回菜单", font=("Microsoft YaHei", 24),
          command=lambda: show(menu_frame)).pack()
new2()
# ── 启动 ───────────────────────────────────────────────────────
show(menu_frame)
root.mainloop()
