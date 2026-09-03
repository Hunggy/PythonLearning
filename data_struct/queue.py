# 任务：自制队列（Step 3/6）
# 目标：
#   1. 用类实现队列 Queue，内部用列表存数据
#   2. 实现 enqueue（入队）、dequeue（出队）、front（看队头）、is_empty
#   3. 理解 FIFO：先进先出——排队的，先来的先走
#
# 和栈的对比：
#   栈：append 进末尾，pop 从末尾出   → 后进先出
#   队列：append 进末尾，从开头出     → 先进先出
#
# 提示：
#   - 入队：self.items.append(x)（和栈一样放末尾）
#   - 出队：列表方法 pop(0) 可以弹出第 0 个（开头）元素
#   - 看队头：items[0]
#   - 判空：return not self.items
#
# 写完验证（对照期待输出）：
#   q = Queue()
#   q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
#   print(q.dequeue())  # 应该输出 A（先进先出！）
#   print(q.dequeue())  # 应该输出 B

class Queue:
    """队列：先进先出（FIFO）"""
    def __init__(self):
        self.items = []

    # TODO: enqueue(x) —— 入队，放到末尾（和栈 push 一样）
    def enqueue(self, item):
        self.items.append(item)
    # TODO: dequeue() —— 出队，拿走并返回第 0 个元素
    def dequeue(self):
        return self.items.pop(0)
    # TODO: front() —— 只看队头不拿走
    def front(self):
        return self.items[0]
    # TODO: is_empty() —— 判断是否为空
    def is_empty(self):
        return not self.items

# ===== 验证区 =====
if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("队头（不取出）:", q.front())   # 期待 A
    print("出队:", q.dequeue())           # 期待 A
    print("出队:", q.dequeue())           # 期待 B
    print("是否为空:", q.is_empty())      # 期待 False
    print("出队:", q.dequeue())           # 期待 C
    print("是否为空:", q.is_empty())      # 期待 True