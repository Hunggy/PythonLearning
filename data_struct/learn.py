# 任务：自制栈（Step 1/6）
# 目标：
#   1. 用类实现一个栈 Stack，内部用列表存数据
#   2. 实现 push（压入）、pop（弹出）、peek（看栈顶）、is_empty（判空）
#   3. 理解 LIFO：后进先出——最后放进去的最先拿出来
#
# 提示：
#   - 栈就像一摞盘子：只能从顶部放、从顶部拿
#   - 列表的 append() 就是"放到顶部"
#   - 列表的 pop()（不带参数）就是"从顶部拿走"
#   - __init__ 里 self.items = [] 做存储
#
# 写完验证：
#   s = Stack()
#   s.push("A"); s.push("B"); s.push("C")
#   print(s.pop())  # 应该输出 C（后进先出！）
#   print(s.pop())  # 应该输出 B
#
# 写完后不用删之前的文件，每步有自己的"验证区"

class Stack:
    """栈：后进先出（LIFO）"""
    def __init__(self):
        self.items = []  # 用列表存数据

    # TODO: 实现 push 方法——把元素放到栈顶
    # 提示：一行搞定，列表有个方法专门往末尾加
    def push(self, item):
        self.items.append(item)
    # TODO: 实现 pop 方法——把栈顶元素拿出来并返回
    # 提示：列表不带参数的 pop() 就是干这个的
    def pop(self):
        return self.items.pop()
    # TODO: 实现 peek 方法——只看栈顶但不拿走
    # 提示：列表最后一个元素用 items[-1]
    def peek(self):
        return self.items[-1]
    # TODO: 实现 is_empty 方法——判断栈是否为空
    # 提示：空列表的 bool 值是 False，直接 return not self.items
    def is_empty(self):
        return not self.items
# ===== 验证区：运行看结果 =====
if __name__ == "__main__":
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    print("栈顶（不取出）:", s.peek())   # 期待 C
    print("弹出:", s.pop())              # 期待 C
    print("弹出:", s.pop())              # 期待 B
    print("是否为空:", s.is_empty())     # 期待 False
    print("弹出:", s.pop())              # 期待 A
    print("是否为空:", s.is_empty())     # 期待 True