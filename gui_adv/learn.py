# tkinter 高级控件学习（六级新考点：Scale / OptionMenu / Entry(show=) / Radiobutton / Checkbutton）
# 任务：做一个"个人信息设置"窗口，把 5 个控件都用上

# 界面布局（从上到下）：
# ① Scale 滑块：调节"音量"（0~100），旁边标签实时显示当前值（拖动时 command 回调）
# ② OptionMenu 下拉菜单：选择"城市"（用 StringVar 存选中值）
# ③ Entry 输入框：密码输入（show="*" 隐藏显示）
# ④ Radiobutton 单选：性别（男/女，两个按钮共享同一个 IntVar/StringVar，互斥）
# ⑤ Checkbutton 多选：爱好（跑步/读书/游戏，可以同时勾多个）

# 最后放一个"提交"按钮，点击后把 5 项内容打印到控制台：
# 例如：音量=60 城市=北京 密码=abc123 性别=男 爱好=['跑步', '游戏']

# 提示（记不住再看）：
# Scale(root, from_=0, to=100, orient=HORIZONTAL, command=回调函数)
#    - from_/to 范围（注意 from 是关键字，要加下划线）
#    - orient=HORIZONTAL 水平 / VERTICAL 垂直
#    - command 回调会收到当前值（字符串）
# OptionMenu(root, 变量, *选项列表)      ← 变量 = StringVar()，选项展开传
# Entry(root, show="*")                  ← show 参数隐藏真实输入
# Radiobutton(root, text="男", variable=变量, value=1)
#    - 一组单选共享同一个 variable，靠 value 区分
# Checkbutton(root, text="跑步", variable=变量)
#    - 勾选 = 变量变 1，取消 = 0（IntVar 默认）

# 第一步：先搭窗口骨架 + ① Scale（窗口 + 滑块 + 实时数值标签）
import tkinter as tk 
root = tk.Tk()
root.title("个人信息设置")

# 音量标签（实时显示滑块值）
vol_label = tk.Label(root, text="音量：0")
vol_label.pack()

# Scale 滑块：范围 0~100，水平方向，拖动时触发回调
def show_vol(value):          # value = 回调收到的当前值（字符串！）
    vol_label.config(text="音量：" + value)

def submit():
    vol = scale.get()                    # ① 滑块：get()
    city = city_var.get()                # ② 下拉：StringVar.get()
    pwd = pw_entry.get()                 # ③ 密码框：Entry.get()
    gender = "男" if gender_var.get() == 1 else "女"   # ④ 单选：IntVar.get()
    hobbies = []
    if run_var.get() == 1:
        hobbies.append("跑步")
    if read_var.get() == 1:
        hobbies.append("读书")
    if game_var.get() == 1:
        hobbies.append("游戏")
    print(f"音量={vol} 城市={city} 密码={pwd} 性别={gender} 爱好={hobbies}")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,
                 command=show_vol)
scale.pack()



city_var = tk.StringVar()
city_var.set("北京")                     # 预设默认值（下拉框初始显示）

cities = ["北京", "上海", "广州", "深圳"]
city_menu = tk.OptionMenu(root, city_var, *cities)   # ← * 展开列表
city_menu.pack()

pw_entry = tk.Entry(root,show='*')
pw_entry.pack()

gender_var = tk.IntVar()
gender_var.set(1) 

tk.Radiobutton(root, text="男", variable=gender_var, value=1).pack()
tk.Radiobutton(root, text="女", variable=gender_var, value=2).pack()

# 爱好多选：每个勾选框【各用各的变量】→ 可以同时勾多个
run_var = tk.IntVar()      # 跑步
read_var = tk.IntVar()     # 读书
game_var = tk.IntVar()     # 游戏

tk.Checkbutton(root, text="跑步", variable=run_var).pack()
tk.Checkbutton(root, text="读书", variable=read_var).pack()
tk.Checkbutton(root, text="游戏", variable=game_var).pack()

tk.Button(root, text="提交", command=submit).pack()
root.mainloop()