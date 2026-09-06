# web_wrong_notes - Flask 错题本

> 基于六级备考错题清单的 Web 检索工具  
> 创建：2026-09-03 · 完成：2026-09-06

## 一、功能

| 路由 | 功能 |
|---|---|
| `/` | 首页 |
| `/list` | 全部 55 条错题（带 Bootstrap 卡片样式） |
| `/search?q=关键词` | 标题/内容模糊搜索 |
| `/category/<name>` | 按分类筛选（支持 `平台歧义 / 卷面 bug` 这类带 `/` 的分类） |
| `/practice` | 随机抽 10 题练习，点"显示答案"查看详解 |

## 二、技术栈

- **Python 3.14** + **Flask 3.1.3**
- **SQLite 3**（标准库 `sqlite3`）
- **Jinja2** 模板（Flask 自带）
- **Bootstrap 5.3**（CDN 引入，零本地依赖）

## 三、运行

```powershell
# 1. 安装 Flask（首次）
& "C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe" -m pip install flask

# 2. 初始化数据库 + 导入数据（首次或重新导入）
& "C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe" init_db.py

# 3. 启动 Flask
& "C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe" app.py

# 4. 浏览器访问
# http://127.0.0.1:5000/list
```

## 四、文件结构

```
web_wrong_notes/
├── README.md          # 本文件
├── app.py             # Flask 主程序：5 个路由
├── init_db.py         # 数据库初始化 + markdown 解析导入
├── templates/         # Jinja2 模板
│   ├── base.html      #   骨架（导航栏 + Bootstrap + 页脚）
│   ├── index.html     #   错题列表（被 /list /search /category 共用）
│   └── practice.html  #   随机练习页（带 JS 显示/隐藏答案）
└── databases/
    └── wrong_notes.db # SQLite 数据（55 条）
```

## 五、数据来源

`init_db.py` 解析 `../archive/wrong_notes.md`（六级备考错题清单）入库。
表结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| id | INTEGER PK AUTOINCREMENT | 自增 ID |
| category | TEXT | 分类（文件操作/类与对象/SQLite…） |
| title | TEXT | 要点标题（`xxx` 部分） |
| content | TEXT | 详细说明 |
| priority | TEXT | 重点标记（🔴/⚠️/🚫/空）|

## 六、核心代码片段

### 数据库路径（避免污染根目录）
```python
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, 'databases')
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, 'wrong_notes.db')
```

### 让 fetchall() 返回字典（Jinja2 才能用 `note.title`）
```python
def dict_factory(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

conn = sqlite3.connect(DB_PATH)
conn.row_factory = dict_factory
rows = conn.cursor().execute('SELECT * FROM wrong_notes').fetchall()
```

### 路由支持带 `/` 的分类
```python
@app.route('/category/<path:name>')   # ⭐ path: 允许斜杠
def category(name): ...
```

## 七、踩过的坑

1. **markdown 解析**：原方案正则太严格（只匹配 `- **xxx**：`），漏掉一半笔记。改成"加粗可选 + emoji 可选"后才收齐 55 条。
2. **`<name>` vs `<path:name>`**：分类名 `平台歧义 / 卷面 bug` 的 `/` 会被路由器当成多段路径 → 404。改用 `<path:name>`。
3. **VSCode 集成浏览器**：徽章在集成浏览器里鼠标变 I 字、点不动——改用 Chrome 正常。
4. **Bootstrap 中文乱码**：控制台 `gbk` 编码显示乱码，但**浏览器里正常**，写文件时 `encoding="utf-8"` 即可。

## 八、可选升级（未做）

- `/add` 手动添加新错题
- `/edit/<id>` 编辑错题
- `/delete/<id>` 删除错题
- 按优先级（🔴/⚠️/🚫）筛选
- 答题正确率统计

## 九、参考资料

- [Flask 官方教程](https://flask.palletsprojects.com/tutorial/)
- [Bootstrap 5.3 文档](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Jinja2 模板](https://jinja.palletsprojects.com/)
