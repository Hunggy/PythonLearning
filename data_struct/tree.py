# 任务：二叉树类 + 三种遍历（Step 5/6）
# 目标：
#   1. 用类实现二叉树节点 TreeNode（值 + 左孩子 + 右孩子）
#   2. 实现前序、中序、后序遍历
#   3. 理解递归：遍历一个树 = 处理根 + 递归遍历左子树 + 递归遍历右子树
#
# 二叉树长这样（每个节点最多两个"孩子"）：
#           1
#          / \
#         2   3
#        / \   \
#       4   5   6
#
# 三种遍历的区别（中间访问根的时机）：
#   前序（根左右）：1 2 4 5 3 6   —— 先访问根，再左，再右
#   中序（左根右）：4 2 5 1 3 6   —— 先左，再根，再右
#   后序（左右根）：4 5 2 6 3 1   —— 先左，再右，最后根
#
# 建议先手动按上面规则走一遍这棵树，再写代码对照
#
# 提示：
#   - 节点类：__init__(self, value) 里存 value + left + right（默认 None）
#   - 建树（对着上面的图）：
#       root = TreeNode(1)
#       root.left = TreeNode(2);  root.right = TreeNode(3)
#       root.left.left = TreeNode(4); root.left.right = TreeNode(5)
#       root.right.right = TreeNode(6)
#   - 遍历函数模板（递归）：
#       def 前序(node):
#           if node is None: return       # 递归出口：空节点直接返回
#           print(node.value)             # 1. 访问根
#           前序(node.left)                # 2. 递归左边
#           前序(node.right)               # 3. 递归右边
#       （中序 = 把 print 放中间，后序 = 放最后，就这么简单）
#
# 写完对照上面手算结果，三种顺序都要对上！

class TreeNode:
    """二叉树节点：一个值 + 指向左/右孩子的连接"""
    def __init__(self, value):
        self.value = value
        self.left = None    # 左孩子，默认没有
        self.right = None   # 右孩子，默认没有

# TODO: 建一棵树（按上面示意图）
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# TODO: 前序遍历函数
def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)

# TODO: 中序遍历函数    
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

# TODO: 后序遍历函数
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")

# ===== 验证区 =====
if __name__ == "__main__":
    # 预期输出：
    # 前序: 1 2 4 5 3 6
    # 中序: 4 2 5 1 3 6
    # 后序: 4 5 2 6 3 1
    print("前序遍历:")
    preorder(root)
    print("\n中序遍历:")
    inorder(root)
    print("\n后序遍历:")
    postorder(root)