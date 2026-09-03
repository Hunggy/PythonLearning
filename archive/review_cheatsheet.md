# 六级考前 1 小时速记卡

> 配合 `wrong_notes.md`（详细分类）和 `mini_mock.md`（自测）使用。本卡只放最高频、最易混的必背点。

## 一、必背三张表

### 文件模式
| 模式 | 行为 |
|---|---|
| r | 只读 |
| w | 覆盖（不存在则新建） |
| a | 追加（**无缝拼接，中间无空格**） |
| a+ | 读写（**指针初始在末尾**） |
| x | 新建（已存在则报错） |

⚠️ `f.write()` 后指针移到末尾，`f.read()` 读到空串 → 读前先 `f.seek(0)`

### SQLite 规则
- PRIMARY KEY **非必须**（默认 rowid）
- 执行 SQL **不必须** `conn.execute()`（可 `cur.execute()`）
- 关闭：**先 cur.close() 再 conn.close()**
- DML(增删改) 后 `conn.commit()`；DDL 自动提交
- `fetchmany(n)` 从**当前游标位置**取 n 行
- `scroll()` 是 DB-API 2.0 规范方法（移动结果集指针），**sqlite3 未实现** → 报错 AttributeError（MySQLdb/pymysql 有实现）

### numpy
- dtype：`'i1'=int8` `'i2'=int16` `'i4'=int32` `'i8'=int64`；float 打印带小数点 `[1. 2. 3.]`
- `linspace(起,止,个数)` **含两端**；`arange(起,止,步长)` **不含终点**
- `reshape` 只改形状不旋转；`np.empty` 是**垃圾值**（非全 0）
- `arr[:, ::-1]` 每行左右翻转

## 二、必记单行
- 类里 `def = 方法`（非函数）；构造函数**缺 self 报错**
- `json.load(文件对象)` / `json.loads(字符串)`；**非全类型可转**（set/datetime/bytes/自定义对象 → TypeError）
- tkinter pack：剩余空间不够 → **换行到下方**；`command=函数名`（不带括号）
- **全角字符程序不认**（写代码/SQL 用半角）
- `csv.DictReader(f)` 首行当键名读字典
- `True == 1`；`input()` 永远返回字符串
- 私有 `__x` 用 `_类名__x` 访问

## 三、平台坑（非知识错，遇歧义按平台口径记）
- ACGO 卷面 bug（选项残缺/`__init__`显成`init`）→ 以 A/B/C/D 前缀判边界
- CODE STUDY 歧义题（两选项都错）→ 记平台答案；编程题无作答框自动判错（**本地做对即不计真错**）
- 平台答案键 bug：JSON 所有类型可转 判 A 实际 B

## 四、考前动作清单
- [ ] 过一遍 `wrong_notes.md`（11 类考点）
- [ ] 刷一遍 `mini_mock.md`（17 题自测，错哪类回哪类）
- [ ] 确认输入法半角习惯
- [ ] 睡好，9 月见 🎯
