# Python 学习进阶项目

## 开发者背景
- 已通过中国电子学会青少年软件编程（Python）二级考试
- 熟练掌握变量、条件判断、循环、函数、列表、字典、文件读写等核心基础语法
- 当前目标：从语法应试转向实战项目开发，掌握常用库与工程化思维
- 备考：2026年9月 Python 六级考试

## 协作原则
1. 结果优先：先给思路和提示，用户自己写代码，需要时给参考代码
2. 分步拆解：复杂项目按模块拆分，每步都能独立运行
3. 适度注释：核心逻辑加中文注释，新库方法简单说明用途
4. 报错友好：优先给修复思路，附带简短错误原因
5. 不重复基础：默认掌握 if/for/函数等入门语法
6. 用户说"ok"时，自己读文件查看进展，不要等用户贴代码
7. 新建项目时：创建英文小写文件夹 + learn.py 骨架（仅任务提示，不写答案）
8. 图片识别约定：用户可直接在对话里贴图（无需先存文件）。助手流程：
   用提取脚本（D:\Temp\Temp\opencode\extract_latest_image.py）从 opencode.db
   的 part 表提取 base64 图片 → 存到 images/pasted_*.png → 用 look_at 工具
   或 multimodal-looker 子代理识别后传回描述，再由主模型思考。
   识别完由助手自行决定图片去留（删或留），不用问用户
9. 图片标记约定：识别过的图片重命名加 _done 后缀（如 xxx_done.png），
   主模型看到 _done 就知道已处理过，避免重复识别
10. 代写边界（2026-08-22 教训）：界面/逻辑**代码必须用户自己写**——只给任务清单 +
    提示级线索（函数名/思路），不给完整代码块；用户说"你写完了我还练什么"= 抱怨代写，
    不是让我写。资料性工作（题库/韵母表/数据）可由助手补全

## 代码规范
- 文件命名：英文小写+下划线，如 learn.py
- 变量函数：蛇形命名法，见名知意
- 单行注释中文

## 工具环境（2026-08-11 更新）
- 全局工具链（opencode 插件/子代理模型/CLI/skills/图片识别流程）见全局文件：
  C:\Users\Hunggy\.config\opencode\AGENTS.md（所有项目通用）
- 本项目特定：图片提取脚本 D:\Temp\Temp\opencode\extract_latest_image.py（用法见协作原则第8条）

## 浏览器操控（2026-08-12 打通 ✅）
- **通用方案**（连接 Chrome、命令、授权、注意事项）见全局文件：
  C:\Users\Hunggy\.config\opencode\AGENTS.md「浏览器操控」章节
- **ACGO 验证结果**：列表页可直读；试卷页需登录（用户浏览器已登录 ✅）。
  2026年3月六级真题 = https://www.acgo.cn/exam/85689?attendNo=5124339762869567601&practiceMatchPaperId=519
  （attendNo/practiceMatchPaperId 每次生成，过期需重新点「开始练习」）

## 学习偏好
- 排斥纯理论，动手实操
- 边做边查库
- 先跑通再优化

## 项目进度

### 考试目标 🎯（2026年9月，Python 六级）
- ⚠️ **考纲版本**：2026年9月考试适用 **2020 修订版考纲**（2019-10-30 发布，qceit.org.cn）。
  2026 修订版（新增数据结构）2027 年才实施，**本次考试不考**。
- 六级考纲考点进度（2020 版 = 5 大块）：
  1. 类与对象（封装/继承/多态）✅ 已完成（oop2/）＋ super()/类变量查漏（2026-08-16 进行中）
  2. 文件操作与数据格式化（CSV、json库）✅ 已完成（data_io/）
  3. 数据可视化（numpy、matplotlib）✅ 已完成（viz/）
  4. SQLite 数据库基础（创建/查询/游标）✅ 已完成（sqlite_db/）
  5. tkinter GUI 设计（控件/布局/事件绑定）✅ 已完成（gui/ 点名器、calc/ 计算器、gui_adv/ 高级控件）
  - 📌 数据结构（data_struct/ 栈/队列/二叉树）为 **2026 新考纲内容，9月不考**，已学完不复习（实战有价值，未来考纲会用）
- 刷题资源（2026-08-13 更新）：
  - 🥇 ACGO 题库（主刷平台，登录稳定）：https://www.acgo.cn/practice/pastQuestion?matchSourceId=4&subjectType=2
    电子学会考级真题 2023-12 至 2026-3（一至六级全有）+ GESP/CSP 真题 + 算法专题（BFS/DFS/二分/贪心）
  - 🆕 **官方测试卷**（2026-08-17 发现）：电子学会官网 qceit.org.cn 的考试页（网址带 exam_uid/d 参数，
    每次进入生成，过期需从官网考评中心重新进入）。**带标准答案 + 逐题解析（官方口径）**，
    比 ACGO 强（ACGO 解析全是"--"）。仅此一份（2022 年卷），用户已刷完：非编程 70 分拿 66 分（94%），
    编程题基本全对 → 正卷通过稳（60 分及格）
  - ⚠️ CODE STUDY（2026-08-13 弃用：登录麻烦）：六级真题 2022-12 至 2025-12 https://gcjkstar.cn/problems/python/
  - GESP 真题仓库（CCF 系，题型相近）：https://github.com/jonaslgtm/gesp-exam-questions

### 第一周：核心常用库实战 ✅ 已完成
- [x] 桌面文件自动分类器（os, shutil）→ folder_clear/
- [x] 课堂随机点名器（random, time）→ random/
- [x] 每日名言查询工具（requests）→ request/
- [x] Excel 成绩自动生成工具（openpyxl）→ excel/
- [x] 批量文件重命名工具（os+字符串）→ rename/

### 第二周：代码模块化与 GUI 入门 ✅ 已完成
- [x] 函数封装：把工具拆成单一职责函数
- [x] 模块导入：多文件架构拆分（rename_utils.py + main.py）
- [x] 面向对象：类重构工具（class RenameTool）
- [x] 继承与多态（Animal/Dog/Cat/Pig）→ oop2/
- [x] tkinter GUI：点名器（gui/）+ 计算器（calc/）

### 六级备考剩余任务
- [x] 数据结构：数组/字符串/队列/栈 ✅ 已完成（data_struct/：learn.py 栈 → parentheses.py 括号匹配 → queue.py 队列 → bank.py 叫号系统 ✅ 全通）
- [x] 二叉树：概念/性质/遍历（前序/中序/后序）✅ 已完成（tree.py 三种遍历全部跑通）
- [x] 历年真题练习（data_struct/practice.py 5 道真题考点全部跑通：is_valid 出栈序列判断 / 前中序求后序验证 / 二叉树节点数公式 / BFS 层序遍历 / 递归深度爆栈实景）
- ⚠️ 以上数据+二叉树属 2026 新考纲（2027 实施），2026-9 考试不考；已学完，考前不用复习

### 2026年3月六级真题（ACGO 实战）✅ 完成
- [x] 单选 25 题 ✅ 已交卷：22/25 = 44 分（满分 50）
- [x] 错题复盘（3 题）：
  1. arr[:, ::-1] 输出题——正确选项 A=[[2 1 0] [5 4 3]]（知识点会，选项字母没对上）
  2. 主窗口创建——正确 tk.Tk()（讨论过但卷面没改，教训：讨论完回卷面改答案）
  3. CSV 描述题——正确 B（每行元素数量必须相同，数据一致性口径；扩展名随意修改❌）。
     ⚠️ 电子学会官方口径与技术事实相反，以考纲口径为准记 B
- [x] 判断题 10 题 ✅ 全对：1错(r原始字符串) 2错(w覆盖→应a) 3对 4对 5对 6错 7错(write不能写列表) 8错(dict用["price"]不能.price) 9对(command绑定) 10对(executemany)
- [x] 填空题 3 题 ✅ 对 2 错 1：1. 长方体灯笼(self.w*self.h*2/self.h*4/d.chang()/d.a4%) 2. 学生信息(w/r/readlines/student/.2f) 3. 数据库(SELECT * FROM member WHERE days<30/cur.fetchall()/row[2])
- [x] 二刷交卷（2026-08-14）✅ **96 分（97%）**：单选+判断+填空全对，仅错 1 空
  - 错因：填空3 SQL 写成 `SELECT * FROＭ...`，FROM 的 M 是**全角字符**（输入法全角模式）
  - 教训：写代码/SQL 用半角输入；全角字母肉眼难辨但程序不认；选中可看出全角更宽
- 交卷地址：https://www.acgo.cn/practice/report/519（一刷 44 分 → 二刷 96 分）

### 2025年12月六级真题（ACGO 实战）✅ 已交卷 94 分（95%）
- [x] 单选 25 + 判断 10 + 填空 3 作答完成（2026-08-15），**交卷 94 分，用时 1h28m**（提交 2026-08-15 20:02）
- 单选答案：1C 2A 3D 4A 5B 6C 7B 8D 9B 10C 11D 12D 13C 14B 15C 16C 17B 18B 19D 20A 21C 22B 23B 24B 25B
- 判断答案：1正确 2正确 3错误 4正确 5正确 6正确 7正确 8正确 9正确 10错误（全对）
- 填空 3（图书借阅）全对；错题复盘 2 处（-6 分）：
  1. 单选 11：ACGO 卷面 `print(count)`（按卷面应选 D 报错），但后台标准答案按 `print(a.count)` 判 B（1）
     → **ACGO 卷面 bug：卷面错、后台对，被冤枉扣 2 分**（与 2024-6 卷排版 bug 相反方向翻车）
  2. 填空 1 ②③：② 填 conn.commit() 错（应填 executemany 的**数据定义** `employees = [(1,'张一',6000),...]`）；
     ③ 填了数据本身（应填**变量名** employees）
- ⚠️ 本卷新考点：tk.Scale/OptionMenu/Entry(show=)/cur.scroll()/super()/类变量/reshape/legend(loc=)
- ⚠️ 本卷踩坑：ACGO 第 11 题题面是 print(count)（非网上流传的 print(a.count)）→ 答案 D 报错！
  **网上解析版本与 ACGO 卷面有出入，做题以卷面为准**
- ⚠️ 用户发现：CREATE TABLE 是 DDL 自动提交，无需 commit()（填空1的②应为定义数据而非 commit）
- 报告地址：https://www.acgo.cn/practice/report/520
- 完整答案解析来源：技术栈 jishuzhan.net/article/2009894034316771330（含标准答案，但判断题/填空题部分缺失）

### 2024年6月六级真题（ACGO 实战）✅ 已交卷 66 分（87%）
- [x] 单选 25 + 判断 10 作答完成并交卷（2026-08-16，用时 1h16m）；**编程题 3 题（30 分）全部放弃**
- 成绩结构：单选+判断 70 分只丢 4 分（2 题），其余 30 分是编程题放弃（环境税）
- 错题复盘（2 题）：
  1. 单选 1（追加拼接）：'a' 模式追加是**无缝拼接**，`"This is an example."+"l see you."` =
     `"This is an example.l see you."`（**中间无空格**）——C 选项带空格是陷阱，正确答案 A（无空格版）
     → 教训：追加 = 原样拼接，**字符级对比选项**（句号、空格都算数）
  2. 单选 21（说法不正确）：`def jd(self)` 在**类里面**定义的是**方法（method）**不是**函数（function）**
     → D"定义 jd 函数"不正确；C"Peter 已成年。"被判正确（ACGO 不纠结句号差异）
     → 教训：类里的 def = 方法！方法 ≠ 函数
- ⚠️ ACGO 编程题环境（本卷暴露的坑）：编辑器缩进显示错乱、代码自动变形、运行错误无 traceback 详情、
  判题环境把 `import csv` 未使用当"编译错误"、运行时 csv.reader 也报"运行错误"（原因未知）
  → **结论：ACGO 编程题体验差，后续编程题在本地 Python 跑通后只填答案**
- ⚠️ 本卷排版 bug：第 4 题题干提示 "Hello World!" 被渲染进选项区下方；`__init__` 显示成 `init`、
  `add()` 显示成 `ddd()`、`Parents` 显示成 `Parent` → **选项里没有"报错"→ 按正常逻辑走；以 A/B/C/D 前缀判断选项边界**
- 单选答案（25 题）：1A 2D 3A 4B 5C 6D 7A 8D 9C 10C 11C 12C 13A 14A 15A 16B 17B 18A 19C 20C 21D 22A 23B 24D 25A
- 判断答案（10 题）：1正确 2错误 3正确 4正确 5正确 6正确 7正确 8错误 9正确 10正确
- 报告地址：https://www.acgo.cn/practice/report/116
- 试卷地址：https://www.acgo.cn/exam/45702?attendNo=5125196232534261873&practiceMatchPaperId=116

### ACGO 六级卷刷题总结（2026-08-16）
- ACGO 六级卷共 5 张：2026-3 ✅ 96 分、2025-12 ✅ 94 分、2024-6 ✅ 66 分、**2024-3 与 2023-12 放弃**（题型更旧更基础，边际价值低）
- 知识性错题共 8 分（2026-3 的 3 题 + 2025-12 的 2 题 + 2024-6 的 2 题），细节题为主，考前过一遍错题清单即可
- 待办：可把三卷错题汇总成考前错题清单

### 考前错题清单 ✅ 已完成（v2 终极版 2026-08-29）
- [x] wrong_notes.md：**覆盖全部 8 张卷**（ACGO 2026-3/2025-12/2024-6 + 官方2022 + CODE STUDY 2025-09/06/03/2024-12/09）
  按 11 大类考点归类（文件/类对象/SQLite/numpy/matplotlib/json/tkinter/CSV口径/字符陷阱/平台bug/细节），每条约注明出处卷
  - 配套自测：`mini_mock.md`（17 题歧义/真漏专练 + 答案）｜`review_cheatsheet.md`（考前 1 小时速记卡 + 动作清单）｜`tomorrow_plan.md`（下次学习安排）
- 高频丢分区：文件模式(a/a+/w+/seek) / SQLite(PRIMARY KEY非必须+关闭顺序+commit) / numpy(linspace vs arange) / json(非全类型可转)
- 2024-6 单选 1 复盘：ACGO 选项数据残缺 bug（A 只显示 "This is an example ."，后台按完整无空格版判 A 对）→ 用户是被 ACGO 坑的，非知识点错

### 新考点查漏补缺（2026-08-16 开始）
- [x] tkinter 高级控件组 ✅ 已完成（gui_adv/learn.py："个人信息设置"窗口全跑通）：
  Scale 滑块(from_/orient/command回调) + OptionMenu 下拉(StringVar+*展开) + Entry(show="*") +
  Radiobutton 单选(共享变量互斥) + Checkbutton 多选(各自变量) + 提交按钮 5 项取值打印
  → 2025-12 卷新考点已消灭 3/8（Scale/OptionMenu/Entry(show=)）
- [x] 数据+继承组 ✅ 已完成（data_adv/learn.py + sql_demo.py）：
  super()(子类复用父类__init__) + 类变量(Employee.count 实例计数) + reshape(2x3/3x2/-1自动算) +
  legend(loc=)("upper right"等) → 8/8 全部消灭
- ⚠️ **cur.scroll() 是假考点**：Python 实测 sqlite3.Cursor **没有 scroll() 方法**（DB-API 2.0 规范
  有定义但 sqlite3 没实现；scroll 属于 MySQLdb/pymysql）。2025-12 卷考它 = 虚晃一枪，
  考试遇到 sqlite3 的 cur.scroll() 正确结果是**报错**（AttributeError）
- [x] SQL 语句速查（sql_demo.py）：CREATE/INSERT/SELECT(WHERE/ORDER BY/聚合 COUNT/AVG/MAX)/
  UPDATE/DELETE + ? 参数化占位 + commit 规则（DDL 自动、DML 手动）

### CODE STUDY 平台重启使用（2026-08-23 注册成功）
- 地址 https://gcjkstar.cn/problems/python/ （当年弃用理由"登录麻烦"已解决）
- 📋 六级卷资源（比 ACGO 多）：2025-12/09/06/03、2024-12/09/06/03、2023-12/09/05、2022-12 + GESP 系列
- ⚠️ 平台特性：①编程题**没有作答框**，空着自动判错（本地做完对解析即可）②计分 38×2=76 制，
  与真实口径（单选50+判断20+编程30=100）不同 → 只当客观题训练场 ③解析带文字（比 ACGO 的"--"强）
  ④限时 60 分钟（ACGO 是 90）⑤浏览器经 playwright-cli attach 可操控（登录态保留）
- 刷题顺序建议：2025-09 ✅ → 2025-06 ✅ → 2025-03 ✅ → 2024-12 ✅ → 2024-09 ✅（最后一张，2023 及更早跳过）

### 2025年9月六级真题（CODE STUDY）✅ 已交卷 58/76（客观题 30/35 = 86%）
- [x] 全卷完成并交卷（2026-08-23），错题 9 = 客观 5 + 编程 4（编程是平台没作答框，非真实错误）
- [x] 编程 3 题本地全做：36 CSV 合并补全 ✅ 全对；37 BankAccount 类逻辑全对（__init__ 双下划线笔误被抓）；
      38 SQLite 改成绩 4/5（漏 .items()——字典遍历键值对必须 items()，直接遍历只有键）
- 错题复盘（5 道客观）：
  1. 题3 文件追加：'a+' 指针初始在**末尾**；'w'/'a' 不存在都新建 → 🔴 **文件模式连续两卷丢分**
     （2024-6 'a' 无缝拼接 + 本次 'a+'），考前必背 r/w/a/a+/x 表
  2. 题8 matplotlib：set_aspect('equal') 锁 XY 1:1 缩放窗口不变形；yticks 接 list/tuple 等效
  3. 题17 🆕 csv.DictReader(f)：首行当键名读成字典——csv 新考点已补
  4. 题21 类基础：self.name 是**属性**不是实例；类名大写只是惯例非语法；④处是创建实例
  5. 题27 arange(10) vs range(10)："序列相类似"判对（宽松口径）；30 JSON load 后就是 dict 可直接改
     （官方口径与直觉相反，以解析为准）

### 2025年6月六级真题（CODE STUDY）✅ 已交卷 56/76（客观题 28/35 = 80%）
- [x] 全卷完成并交卷（2026-08-24），错题 10 = 客观 7 + 编程 3（编程是平台没作答框，非真实错误）
- 错题复盘（客观 7 道，题3 为平台卷面 bug）：
  1. 题2 类定义错误：D `def __init__(l, w, h)` **缺 self**——构造函数细节（上卷考双下划线、这卷考 self）
  2. 题3 平台 bug：正确答案 `Mi(a, b)` 被抓题丢失、D 显示与 C 重复 → 用户被坑，非知识性错误
  3. 题4 json.load 调用方向：是 `json.load(文件对象)` 不是 `文件对象.load(json)`——load 是 json 模块方法
  4. 题11 tkinter pack：考试口径"剩余空间不够→换行到下方"→ D（用户实测偏 C，按官方口径记 D）
  5. 题23 SQLite 关闭顺序：先 `cur.close()` 后 `conn.close()`（cursor 从 connection 生出，先关小的）
  6. 题29 json.loads：带 s=处理字符串→转 dict，正确答案 A（刚讲过还错，送分题）
  7. 题35 fetchmany(size=2)：从**当前游标位置**开始取 2 行，非"前两行"（抠字眼口径）
- 编程 3 题（36/37/38）：平台无作答框判错，本地未做（按上卷流程应本地做对）

### 2025年3月六级真题（CODE STUDY）✅ 已交卷 68/76（客观题 34/35 ≈ 97%）
- [x] 全卷完成并交卷（2026-08-27），错题 4 = 客观 1（题6）+ 编程 3（36/37/38 平台无作答框自动判错）
- 客观只错 1 道（题6），编程 36/37 用户代码经助手核对全对、38 二进制换算已学会
- 错题复盘（客观 1 道）：
  - 题6 numpy.linspace：`np.linspace(0,10,11)` 生成 **11 个**等间距数、**含两端** → `[0. 1. 2. ... 10.]`
    （正确答案 A，无逗号空格分隔）；用户选 D `[0., 0.9, 1.8...9.]` 是 `linspace(0,9,11)` 类误判
    → 🔴 **linspace vs arange 新考点**：linspace 按"个数"含两端；arange 按"步长"不含终点
- 编程 38 二进制换算：用户当时不会，已讲透 `s = s*2 + int(位)` 累加法（每 8 位一组清零重算）

### 2024年12月六级真题（CODE STUDY）✅ 已做（客观逐题过 + 编程 36/37/38 自对答案）
- [x] 客观题逐题做过（json/int→JSON/tkinter pack/StringVar/file模式/继承/matplotlib subplots+savefig/控件/null/默认文本模式/plot参数/Button/scatter s/全类型转JSON 等），编程 36/37/38 本地写完并对照参考答案自验
- 编程 3 题（登陆校验 / 学生数据库 / 图书管理类）全部自对通过：
  - 36：①`input('用户名：')+'\n'` ②`input('密码：')+'\n'` ③`c==a and d==b`（readline 带 `\n` 必须 +'\n' 对齐）
  - 37：①`conn.cursor()` ②`students` ③`conn.commit()` ④`cursor`
  - 38：①`author` ②`self.books` ③`self.books` ④`display_info`
- ⚠️ **平台答案键 bug**：判断题"Python所有数据类型都可以转换为JSON类型"平台判 A（正确），实际应为 **B（错误）**——set/datetime/bytes/自定义对象转 JSON 会 TypeError。以知识点为准，别被平台带偏

### 2024年09月六级真题（CODE STUDY）✅ 已交卷 64/76（客观题 32/35 = 91%）
- [x] 全卷完成并交卷（2026-08-29），错题 6 = 客观 3（Q5/Q10/Q11）+ 编程 3（平台无作答框自动判错，非真实错误）
- [x] 编程 3 题本地全做并核对（助手读页拉题干+参考，用户自写）：
  - 36 士兵瑞恩（OOP）：①`__init__` ②`self` ③`-=` ④`self.model` ⑤`self.gun.shoot()` —— 全对
  - 37 成绩统计（sqlite）：①`sqlite3.connect("D:/Cjdata.db")` ②`学号 TEXT PRIMARY KEY`（参考`学号 TEXT(10) PRIMARY KEY NOT NULL`等效）③`INSERT INTO cj VALUES(...)` ④`SELECT * FROM cj WHERE 成绩<100` ⑤`cursor.fetchall()` —— 初稿漏 D: 路径+用 INTEGER，经助手点出改 TEXT 后满分
  - 38 家庭记录（文件）：①`"a"` ②`"ledger.txt"` ③`readlines()` ④`read_records()` —— 全对
- 客观错题复盘（3 道，2 歧义 + 1 真漏）：
  1. **Q5** SQLite 说法错误：用户选 B（conn.execute 必须），参考 A（PRIMARY KEY 必须）。⚠️ **歧义题：A、B 两句都是假话，平台按 A 判**。助手当时误导用户选 B，记一笔（背锅）
  2. **Q10** 不是文件写方法：用户选 B(writeline)，参考 C(writetext)。⚠️ 歧义：writeline(单数不存在)/writetext(框架) 都不是方法，平台选 C
  3. **Q11** `open('A.txt','w+')` 写'hello'后`print(f.read())`：用户选 C(写并输出hello)，参考 B(只写不输出)。🔴 **真知识点**：`f.write()` 后指针移到末尾，`f.read()` 从末尾读→空串；要读需先 `f.seek(0)`
- 总分 64/76（38×2 制），客观 91%，与前面几张卷（94/56/68）相当
- 📌 六卷 CODE STUDY 全部刷完（2025-09/06/03/2024-12/09），六级真题热身收工

### 拼音学习工具（pinyin_tool/）🔨 进行中（2026-08-22 开工，提前于六级考试）
- 背景：用户口语正常（会读字），但拼音方案不熟：**声母全会，韵母只认识 a o e i u
  （缺 ü、复韵母、鼻韵母共 19 个）**。用户用仓颉输入法（字形拆字）→ 学拼音打字是实用目标。
  技术栈 = 六级全家桶（tkinter + sqlite3 + random + matplotlib + 文件操作）
- 功能进度：
  - [x] ①韵母学习卡（24 卡翻页循环；Frame 多页架构：菜单/学习卡/测试/错题本四页 show() 切换）
  - [x] ②韵母辨识测试（random.sample 抽 10 题 + 4 选 1 按钮 + 计分 + 刷新重开 +
        answered 锁标记防重复刷分）
  - [x] ③sqlite 错题本（wrong_notes.db：答错 UPSERT 记录 ON CONFLICT DO UPDATE 次数+1；
        错题排行页 Top5；⚠️ 菜单按钮要绑 show_wrong() 而非直接 show(frame)，否则不查询）
  - [x] ④matplotlib 曲线（rounds 表记每轮成绩 date/score → plot_score 折线 ylim(0,10)；
        plot_wrong 弱项柱状图 bar(hatch="//") 取前8 = ORDER BY DESC LIMIT 8）
  - [x] ⑤拼音打字练习 ✅ 完成（2026-08-23）：主动输出式——出汉字、Entry 输入完整拼音判定
    （用户否决了"选声母+选韵母"方案：声母全会没训练价值，且与测试页实现雷同）。
    题库 pinyin_data.py（66 字标准结构，覆盖 24 韵母+易混声母组 zh/z ch/c sh/s n/l f/h；
    刻意避开整体认读音节和零声母字）。界面用户自己写 + 助手修 3 bug：
    bind/command 函数签名冲突（event=None 默认参数双兼容）、刷新按钮绑错成测试页 restart、
    打字错题没进 wrong_notes/rounds 表。交互：←重开 →下一题 回车提交（绑 pin 不绑 root，
    focus 常驻输入框；短拼音全删重打比移光标快）
  - 📌 可选升级（未做）：题库加介音字（uo/ia/ua 类，2026-08-23 用户发现 kuo 的 uo 在 24 韵母表
    找不到 → 介音概念：u/i/ü 垫在声母和韵母之间，uo=k+介音u+韵母o，不算独立韵母）；
    简繁体字库支持
- 📌 ü 打字规则（做进题库 input 字段）：n/l 后打 v（女=nv 绿=lv）；j/q/x 后省点打 u（军=jun 学=xue）
- 本项目新学知识点（2026-08-22）：
  - Frame 多页切换：pack_forget() 只撤下不销毁，状态保留；show() 统一隐藏+显示
  - 函数内改全局变量必须 global 声明，否则 UnboundLocalError（赋值=认定局部变量）
  - lambda 循环绑定陷阱：command=lambda y=opt: check(y) 默认参数固定当前值
  - 防重复操作锁标记模式：answered 标志位 if answered: return
  - list.index(值) 按值找下标（找不到报 ValueError）；字典 d[key]=新值 直接改
  - SQL UPSERT：INSERT ... ON CONFLICT(主键) DO UPDATE SET 字段=字段+1（sqlite3 ≥3.24）
  - matplotlib plt.show() 脚本模式下关窗即销毁 figure 不叠图；Jupyter/Spyder 交互模式才叠（需 clf/close）
  - Label 只认字符串：列表/元组上屏前要 join 格式化
  - bind 和 command 共用函数：def f(event=None) 默认参数双兼容（bind 塞 event、command 不传）
  - bind 绑控件不绑 root = 只在该控件聚焦时生效（打字页绑 Entry，focus 常驻）

## 已掌握的库
- os：listdir / path.join / path.splitext / makedirs / rename
- shutil：move
- random：choice / shuffle
- time：sleep
- requests：get / json / status_code / 异常处理
- openpyxl：Workbook / cell / Font / Alignment / column_dimensions
- tkinter：Tk / Label / Button / Entry(get/delete/focus/show) / pack(side) / pack_forget多页切换 /
  Frame页面容器 / command / lambda固定参数绑定 / after / config / Radiobutton / Checkbutton /
  Scale / OptionMenu
- json：dump / load / ensure_ascii
- csv：writer / reader / 编码（utf-8 / gbk）
- sqlite3：connect / cursor / execute / commit / close / fetchall / fetchone / 参数占位 /
  ON CONFLICT UPSERT（次数累加）/ CREATE TABLE IF NOT EXISTS
- matplotlib：plot(marker) / bar(hatch/color/edgecolor) / pie / subplot / title / xlabel / ylabel /
  ylim / show / rcParams字体 / legend(loc=)
- numpy：array / 数组运算（arr+常数）/ mean / sum / max / arange / linspace / reshape / 切片
- 类与对象：class / __init__ / self / 继承 / 多态 / 重写