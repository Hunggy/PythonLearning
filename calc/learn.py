import tkinter as tk


win = tk.Tk()
win.title("计算器")
display = tk.Label(win, text="", bg="white", anchor="e")
display.grid(row=0, column=0, columnspan=4)

def click(value):
    global first_num, operator
    if value.isdigit():              # 数字
        current = display["text"] + value
        display.config(text=current)
    elif value in "+-*/":
        first_num = float(display["text"])   # 记住当前数字
        operator = value
        display.config(text="")
    elif value == "=":
        second = float(display["text"])
        if operator == "+":
            result = first_num + second
        elif operator == "-":
            result = first_num - second
        elif operator == "*":
            result = first_num * second
        elif operator == "/":
            result = first_num / second
        display.config(text=str(result))
    elif value == "C":
        display.config(text="")


tk.Button(win, text="7", command=lambda: click("7")).grid(row=1, column=0)
tk.Button(win, text="8", command=lambda: click("8")).grid(row=1, column=1)
tk.Button(win, text="9", command=lambda: click("9")).grid(row=1, column=2)
tk.Button(win, text="/", command=lambda: click("/")).grid(row=1, column=3)
tk.Button(win, text="4", command=lambda: click("4")).grid(row=2, column=0)
tk.Button(win, text="5", command=lambda: click("5")).grid(row=2, column=1)
tk.Button(win, text="6", command=lambda: click("6")).grid(row=2, column=2)
tk.Button(win, text="*", command=lambda: click("*")).grid(row=2, column=3)
tk.Button(win, text="1", command=lambda: click("1")).grid(row=3, column=0)
tk.Button(win, text="2", command=lambda: click("2")).grid(row=3, column=1)
tk.Button(win, text="3", command=lambda: click("3")).grid(row=3, column=2)
tk.Button(win, text="-", command=lambda: click("-")).grid(row=3, column=3)
tk.Button(win, text="0", command=lambda: click("0")).grid(row=4, column=0)
tk.Button(win, text="C", command=lambda: click("C")).grid(row=4, column=1)
tk.Button(win, text="+", command=lambda: click("+")).grid(row=4, column=2)
tk.Button(win, text="=", command=lambda: click("=")).grid(row=4, column=3)








win.mainloop()