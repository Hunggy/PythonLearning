# 任务：真题演练（Step 6/6，考前最后冲刺）
# 目标：用代码验证六级真题里的选择题结论，把概念变成直觉
#
# 下面这些是真题里反复出现的考点，每题写几行代码验证
# 不会的可以先猜，跑完代码看结果，再想想为什么

# ========== 考题 1：栈的进出顺序 ==========
# 一个栈初始为空，依次 push 了 a,b,c（栈底到栈顶 a,b,c）
# 元素 d 已经出栈，问 d 可能是第几个入栈的？
# 验证：
#   模拟一下：只能 push 或 pop 栈顶，能出栈 d 吗？
#   提示：d 在 a,b,c 之上才能出来。写个小模拟：push a,b,c 后
#   先 pop（出 c），d 还没入栈怎么出？
# 试试运行这个：
#   s = []
#   s.append("a"); s.append("b"); s.append("c")
#   print("只能弹出:", s.pop())   # 观察能弹出谁
#   # 结论：栈只能弹出栈顶，这就是为什么真题说 d 必须在最上面
from learn import Stack 

def is_valid(push_seq, pop_seq):
    s=Stack()
    for i in push_seq:
        s.push(i)
        while s.is_empty() == False and s.peek() == pop_seq[0]:
            s.pop()
            pop_seq.pop(0)
    return s.is_empty() and len(pop_seq) == 0

# ========== 考题 2：前序+中序求后序 ==========
# 真题：前序遍历 1 2 4 3 5 7 6，中序遍历 2 4 1 5 7 3 6，求后序遍历
# 手算技巧（写代码理解）：
#   前序第一个 = 根（1）
#   中序里找 1，左边 2 4 是左子树，右边 5 7 3 6 是右子树
#   递归套用……（这就是 Step 5 学的知识！）
# 根 1 左根2 左的右是4 ,右的根3 右左5 右左右7 右右6
# 用 tree.py 建树验证：
#   root = TreeNode(1)
#   root.left = TreeNode(2)          # 左子树只有 2（2 的右孩子是 4？不对，看中序）
#   # 实际结构：1 的左孩子 2，2 的右孩子 4
#   #           1 的右子树根 3，3 的左孩子 5，5 的右孩子 7，3 的右孩子 6
from tree import TreeNode , postorder
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(7)
root.right.right = TreeNode(6)


#postorder(root)  # 后序遍历，验证：4 2 7 5 6 3 1



# ========== 考题 3：完全二叉树性质 ==========
# 完全二叉树深度 h 的层数满节点数：2**h - 1
# 深度为 h 的二叉树最多 2**h - 1 个节点
# 验证代码：
#   h = 4
#   print("深度", h, "最多节点:", 2**h - 1)   # 15，对吗？
#   print("深度", h, "最后一层最多:", 2**(h-1))  # 8
# 真题：深度 4 的二叉树最少几个节点？（4 个——每条路都只有一个孩子）
# 最多？（15 个——满二叉树）
import math
h=4
#print("深度", h, "最多节点:", 2**h - 1)
#print("深度 4 完全二叉树最少:", 2**(h-1))
#print("13 个节点的深度:", math.floor(math.log2(13)) + 1)


# ========== 考题 4：队列和 BFS ==========
# 广度优先搜索（BFS）为什么要用队列？
# 验证：把树按层从上到下、每层从左到右输出 = 队列操作
#   1. 根入队
#   2. 循环：出队一个 → 打印 → 它的左孩子右孩子入队
#   用 tree.py 的树跑一遍，应该输出 1 2 3 4 5 6（层序！）
# 这就是著名的"层序遍历"，BFS 的核心就是队列
from tree import root            # tree.py 里现成的树（1 2 3 / 4 5 6）
from collections import deque    # 队列：先进先出

def bfs(node):
    """层序遍历：一层一层、从左到右打印"""
    q = deque([node])            # 1. 根节点先入队
    while q:                     # 2. 队列不空就一直处理
        cur = q.popleft()        # 3. 队头出队（谁先来谁先走）
        print(cur.value, end=" ")  # 4. 打印出队的节点
        if cur.left:             # 5. 左孩子排到队尾
            q.append(cur.left)
        if cur.right:            # 6. 右孩子排到队尾
            q.append(cur.right)
    print()

#print("层序遍历:", end=" ")
#bfs(root)

# ========== 考题 5：递归与栈 ==========
# 递归太深为什么程序会崩？（栈空间溢出）
# 先不跑这个，容易卡死——理解即可：
#   每次递归调用都往"调用栈"压一层，太深就爆了
#   Python 默认递归深度约 1000
# 验证（安全版）：
import sys
print("Python 递归上限:", sys.getrecursionlimit())

def errortest(n):
    if n >= 5000:        # ✅ 出口：到 5000 就回头
        return
    errortest(n + 1)     # 参数朝出口收敛，每层只调一次

errortest(0)            



