# 六级考前错题清单（终极版 · 考前 10 分钟过一遍）

> 覆盖：ACGO 2026-3 / 2025-12 / 2024-6 + 官方 2022 卷 + CODE STUDY 2025-09 / 06 / 03 / 2024-12 / 09
> CODE STUDY 76 制（38×2），ACGO 100 制。全是细节/口径题，记住规律 = 满分。

## 1. 文件操作（最高频丢分区）
- **文件模式 r/w/a/a+/x**：r 只读｜w 覆盖(不存在新建)｜a 追加(无缝拼接无空格)｜a+ 读写(指针初始末尾)｜x 新建(已存在报错)
- **'a' 追加 = 原样拼接，中间无空格**：`"This is an example."+"l see you."` → `"This is an example.l see you."`（ACGO 2024-6 单选1：C 带空格是陷阱）
- **'a+' 指针初始在末尾；'w'/'a' 文件不存在都新建**（CODE 2025-09 题3）
- 🔴 **write 后指针移到末尾，read() 从末尾读→空串**；要读先 `f.seek(0)`（CODE 2024-09 Q11 真漏）
- **readline() 带换行 `\n`**，比对前 input 要 `+'\n'` 才能和文件内容对齐（CODE 2024-12 36）
- **csv.DictReader(f) 首行当键名读成字典**（CODE 2025-09 题17）
- **writelines() 才是真方法**；`writeline`(单数不存在)/`writetext`(框架) 都不是（CODE 2024-09 Q10 歧义）
- print(file)≠print(file.read())：file 是对象，内容要 read()
- with open() as f 自动关闭；csv.writer 需写权限(默认'r'会报错)

## 2. 类与对象
- **类里的 def = 方法(method)，不是函数(function)**（ACGO 2024-6 单选21）
- **__init__ 双下划线**；构造函数**缺 self 报错**（CODE 2025-06 题2）
- self.name 是**属性**不是实例；类名大写是惯例非语法；④处是创建实例（CODE 2025-09 题21）
- **没有真正私有成员**：`__x` 可用 `_类名__x` 访问（CODE 2024-09 判断）
- 封装 = 绑定属性+方法，getter/setter 控制访问（CODE 2024-09 判断）
- super() 复用父类 __init__（新考点）｜主窗口 `tk.Tk()`（T 大写）

## 3. SQLite
- ⚠️ **PRIMARY KEY 不必须指定**，默认 rowid（CODE 2024-09 Q5 歧义，平台按 A 判）
- ⚠️ 执行 SQL **不必须 conn.execute**，可 `cur=conn.cursor(); cur.execute()`（CODE 2024-12 Q5 歧义）
- **关闭顺序：先 cur.close() 后 conn.close()**（CODE 2025-06 题23）
- **DML(增删改)后必须 conn.commit()；DDL 自动提交**（ACGO 2025-12 填空）
- **fetchmany(size=2) 从当前游标位置取 2 行**（CODE 2025-06 题35）
- 🚫 **cur.scroll()**：DB-API 2.0 规范方法（移动结果集指针），**sqlite3 未实现** → 报错 AttributeError（MySQLdb/pymysql 有实现）
- **connect 路径用正斜杠 `D:/test.db`**；反斜杠 `\t` 变制表符（CODE 2024-12 Q8）
- 占位符 ? 参数化；executemany 第二参是**数据列表的变量名**（ACGO 2025-12 填空）
- INTEGER 存储 1/2/3/4/6/8 字节(无 16)｜行=记录 列=字段｜零配置无需服务器（官方卷）

## 4. numpy
- dtype **'i1'=int8, 'i2'=int16, 'i4'=int32, 'i8'=int64**（CODE 2024-09 Q2）
- dtype=float 打印带小数点 `[1. 2. 3.]`（CODE 2024-09 Q3）
- 结构化数组 **'S20'→bytes(`b'Alice')、'i2'→int、'f4'→float**；`S`带b `U`不带（CODE 2024-09 Q4）
- 🔴 **linspace(起,止,个数) 按个数含两端；arange(起,止,步长) 不含终点**（CODE 2025-03 题6）
- reshape 只改形状，**不旋转/缩放**（CODE 2024-09 判断）
- `arr[:, ::-1]` 每行左右翻转｜itemsize float64=8 float32/int32=4｜np.empty≠全0(垃圾值) 全0用 zeros
- axis=0 按列 axis=1 按行｜负步长 `x[8:4:-1]` 从右往左 stop 不包含

## 5. matplotlib
- **bar() 柱状图**（CODE 2024-09 Q1）
- **set_aspect('equal') 锁 1:1**；yticks 接 list/tuple 等效（CODE 2025-09 题8）
- subplots / savefig / legend(loc='upper right')（新考点）｜rcParams 字体

## 6. json
- **json.load(文件对象)** 不是 文件对象.load(json)（CODE 2025-06 题4）
- **json.loads(s) 带 s 处理字符串→dict**（CODE 2025-06 题29）
- load 后就是 dict 可直接改（CODE 2025-09 题27）
- 🚫 **不是所有类型能转 JSON！** set/datetime/bytes/自定义对象→TypeError（CODE 2024-12 平台误判 A，实际 B）

## 7. tkinter
- **pack 官方口径**：剩余空间不够→换行到下方（CODE 2025-06 题11）
- StringVar + textvariable 绑定｜Scale/OptionMenu/Entry(show='*')（新考点）
- **command=函数名(不带括号)**；带括号=立即执行｜不能显示文本的组件官方口径=Button（官方卷9）

## 8. CSV 描述题（官方口径）
- **每行元素数量必须相同**（数据一致性）｜扩展名可改❌（以考纲口径为准）
- csv.writer 需写权限

## 9. 输入法 / 字符陷阱
- 🔴 **全角字符程序不认**：`SELECT * FROＭ...` 的 Ｍ 全角→报错（ACGO 2026-3 二刷）。写代码/SQL 用**半角**！
- 追加拼接**字符级对比选项**（句号空格都算数）

## 10. 平台歧义 / 卷面 bug（非知识错但会丢分）
- ACGO 卷面 bug：选项残缺(`__init__`显成`init`、A 只显半句)/渲染错(题干提示进选项区)
- CODE STUDY 歧义题：**两选项都错，平台按一个判**（2024-09 Q5/Q10、2024-12 Q5）→ 以平台口径记
- CODE STUDY **编程题无作答框，自动判错**——不计真错，本地做对即可
- 平台答案键 bug：JSON 所有类型可转 判 A 实际 B（2024-12）
- 卷面与网上版本可能不一致，以卷面为准但后台按官方答案
- **讨论完答案记得回卷面改**（ACGO 2026-3 单选2 血泪）

## 11. 其他细节
- True==1｜input() 返回字符串要数字必 int()｜(30,) 元组要带逗号否则是 int
- a[-1]=最后一个；二维 a[行][列]，len(a[j])=行宽，先化简再代入
- place(x,y)：x 同=垂直线 y 同=水平线；width/height 像素覆盖构造参数
- 负索引从末尾数，i=0 时 a[i-1] 不越界
