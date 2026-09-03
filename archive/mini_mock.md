# 六级迷你模拟考（歧义题 + 真漏题专练）

> 17 题，全部来自八张卷里你真实踩过 / 易混的坑。先做，答案在最后自对。
> 建议：闭卷，每题 30 秒内出答案；错了回 `wrong_notes.md` 对应类再背一遍。

## 单选题

1. 关于文件打开模式，错误的是？
   A. 'a' 模式追加写入，原内容不会被清空
   B. 'a+' 模式打开后文件指针位于文件开头
   C. 'w' 模式打开不存在的文件会新建
   D. 'x' 模式打开已存在的文件会报错

2. 执行 `f.write('hello')` 后立刻 `f.read()`，得到？
   A. 'hello'  B. ''（空串）  C. 报错  D. None

3. 下列方法中，属于文件写操作的是？
   A. writeline  B. writetext  C. writelines  D. readline

4. 关闭 SQLite 连接，正确顺序是？
   A. 先 conn.close() 再 cur.close()
   B. 先 cur.close() 再 conn.close()
   C. 无所谓先后
   D. 只关 cursor 即可

5. `cur.fetchmany(2)` 取的是？
   A. 前两行  B. 后两行  C. 从当前游标位置取 2 行  D. 随机 2 行

6. sqlite3 中 `cur.scroll()` 会？
   A. 移动指针  B. 报 AttributeError  C. 提交事务  D. 滚动结果集

7. `np.dtype('i1')` 对应的类型是？
   A. int16  B. int8  C. int32  D. int64

8. `np.linspace(0, 10, 11)` 生成？
   A. 11 个数，含 0 和 10
   B. 10 个数，含 0 不含 10
   C. 11 个数，不含 10
   D. 10 个数，含 10

9. 以下能直接 `json.dumps()` 的是？
   A. {'a': 1}
   B. {'a': {1, 2}}
   C. {'a': datetime.now()}
   D. {'a': open('x.txt')}

10. 从文件对象 f 读取 JSON，正确写法是？
    A. json.load(f)  B. f.load(json)  C. json.loads(f)  D. json.load(json)

11. 类里写 `def foo(self):`，foo 是？
    A. 函数  B. 方法  C. 变量  D. 属性

12. `class A: def __init__(x, y): self.x = x` 这样定义构造函数会？
    A. 正确  B. 缺 self 报错  C. 缺 return 报错  D. 运行正常但无效

13. tkinter 用 pack 布局，剩余空间不够时控件会？
    A. 重叠  B. 换行到下方  C. 报错  D. 被忽略

14. 代码 `SELECT * FROＭ t` 报错的原因是？
    A. 语法错误  B. Ｍ 是全角字符  C. FROM 拼写错  D. 表不存在

15. `csv.DictReader(f)` 把？
    A. 全部读成列表  B. 首行当键名读成字典  C. 末行当键名  D. 直接报错

16. `np.empty((2, 2))` 的初始值是？
    A. 全 0  B. 全 1  C. 未初始化的垃圾值  D. 全 None

17. `arr = [[0,1,2],[3,4,5]]`，`arr[:, ::-1]` 结果是？
    A. [[2,1,0],[5,4,3]]  B. [[0,1,2],[3,4,5]]  C. [[2,1],[5,4]]  D. 报错

## 答案
1.B  2.B  3.C  4.B  5.C  6.B  7.B  8.A  9.A  10.A
11.B  12.B  13.B  14.B  15.B  16.C  17.A

## 错因速查（对应 wrong_notes.md 类）
- 1/2/3 → 文件操作（a+指针末尾、write后read空、writeline不存在）
- 4/5/6 → SQLite（关闭顺序、fetchmany当前指针、scroll是DB-API 2.0规范方法但sqlite3未实现→报错）
- 7/8/16/17 → numpy（dtype、linspace含两端、empty垃圾值、::-1翻转）
- 9/10 → json（非全类型可转、load读文件）
- 11/12 → 类对象（def=方法、缺self）
- 13/14/15 → tkinter/字符/csv（pack换行、全角、DictReader）
