# 任务：括号匹配检查器（Step 2/6）
# 目标：
#   1. 用 Step 1 的 Stack 检查一串括号是否匹配
#   2. 理解栈的真实用途：编译器/编辑器检查 ()[]{} 是否成对
#
# 什么是"匹配"：
#   "()" 匹配  |  "(())" 匹配  |  "([{}])" 匹配
#   "(" 不匹配（没关闭）  |  ")(" 不匹配（先关后开）
#   "([)]" 不匹配（交叉了：中括号没关就开小括号了）
#
# 思路（用栈）：
#   - 遇到左括号 ( [ { → 压入栈
#   - 遇到右括号 ) ] } → 弹出栈顶，检查是否和它配对
#       配对法则：弹出的是 ( 则必须遇到 )，[ 必须 ]，{ 必须 }
#   - 遍历完：栈空 = 全部匹配；栈不空 = 有没关上的括号
#
# 提示：
#   - 定义配对字典：{")": "(", "]": "[", "}": "{"}
#   - 写函数 check(s: str) -> bool
#   - 从 Step 1 导入：from learn import Stack
#     （learn.py 结尾的验证区用 if __name__ == "__main__" 保护了，
#      别删除那个 if，否则导入时会连验证代码一起跑）
#
# 写完验证：
#   check("()")      → True
#   check("(())")    → True
#   check("([{}])")  → True
#   check("(")       → False
#   check(")(")      → False
#   check("([)]")    → False

from learn import Stack  # 复用 Step 1 的栈

def check(x):
    """检查括号字符串 x 是否匹配，返回 True/False"""
    # 左括号的集合：'([{'
    left_brackets = '([{'
    # 配对字典：右括号 -> 左括号
    dict = {")": "(", "]": "[", "}": "{"}
    # 思路搬到代码：
    # 1. 建一个空栈
    # 2. for 循环每个字符 c：
    #      如果是左括号 → push(c)
    #      如果是右括号 → 先判断栈空不空（空了说明没配对的 = 不匹配）
    #                      再 pop 出栈顶，和配对字典比对，对不上 = 不匹配
    s = Stack()
    for c in x:
        if c in left_brackets:
            s.push(c)
            
        else:
            if s.is_empty():
                return False
            top = s.pop()
            if dict[c] != top:
                return False

    if s.is_empty():
        return True
    else:
        return False

    # 3. 循环结束，栈空返回 True，不空返回 False
      # TODO: 删掉 pass 写你的代码

# ===== 验证区 =====
if __name__ == "__main__":
    test_list = ["()", "(())", "([{}])", "(", ")", ")(", "([)]"]
    for t in test_list:
        print(f"{t:10} -> {check(t)}")
    # 期待依次输出：True True True False False False False