# Flask 错题本项目 - 启动方案

> 创建日期：2026-09-03  
> 计划详情：`.omo/plans/next-steps.md` → 方向一

## 一、环境准备（5分钟）

### 1. 检查 Python
```powershell
& "C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe" --version
```
预期输出：`Python 3.14.x`

### 2. 安装 Flask
```powershell
& "C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe" -m pip install flask
```

## 二、项目结构

```
web_wrong_notes/
├── README.md          # 本文件
├── app.py             # Flask 主程序（明天写）
├── init_db.py         # 初始化数据库+导入数据（明天写）
├── templates/         # HTML 模板（明天建）
│   ├── base.html
│   ├── index.html
│   ├── detail.html
│   └── practice.html
└── databases/         # 数据库文件夹（明天建）
    └── wrong_notes.db
```

## 三、启动步骤（明天按顺序做）

### Step 1：Flask Hello World（10分钟）
创建 `app.py`，实现：
- 导入 Flask
- 创建应用实例
- 写一个路由 `/`，返回"Hello 错题本"
- 启动开发服务器

**验证**：浏览器打开 `http://127.0.0.1:5000` 看到文字

### Step 2：初始化数据库（15分钟）
创建 `init_db.py`：
- 连接 `databases/wrong_notes.db`
- 创建表（字段见下方）
- 解析 `archive/wrong_notes.md` 并导入
- 写一个 `app.py` 路由 `/list` 显示所有错题

**表结构**（匹配 wrong_notes.md 实际格式）：
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER PRIMARY KEY | 自增ID |
| category | TEXT | 分类（文件操作/类与对象/SQLite...） |
| title | TEXT | 要点标题（**加粗**部分） |
| content | TEXT | 完整内容（整条笔记） |
| priority | TEXT | 重点标记（🔴/⚠️/🚫/空） |

**解析规则**（init_db.py 怎么读 wrong_notes.md）：
- 读文件，逐行处理
- 行以 `## ` 开头 → 分类名（如"1. 文件操作"→截取"文件操作"）
- 行以 `- ` 开头 → 一条知识点：
  - 提取 `**...**` 内容 → title
  - 整行去掉 `- ` → content
  - 检测 🔴/⚠️/🚫 标记 → priority（没有则为空）
- 其他行（`# `、`>`、空行）→ 跳过

**验证**：访问 `/list` 看到按分类分组的笔记列表

### Step 3：模板渲染（20分钟）
- 创建 `templates/base.html`（导航栏、页脚）
- 创建 `templates/index.html`（错题列表）
- 用 Bootstrap CDN 美化（不用学 CSS）

**验证**：列表页有样式，手机也能看

### Step 4：搜索 + 筛选（20分钟）
- 添加 `/search?q=关键词` 路由
- 添加 `/category/<name>` 路由（按分类筛选）

**验证**：能搜索、能按分类筛选

### Step 5：随机练习（15分钟）
- 添加 `/practice` 路由
- 随机抽 10 题，显示题目，隐藏答案
- 点击"显示答案"显示对错

**验证**：能随机出题

## 四、关键代码片段（明天看）

### 数据库路径（避免在根目录创建）
```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'databases')
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, 'wrong_notes.db')
```

### Flask 最小应用
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello 错题本'

if __name__ == '__main__':
    app.run(debug=True)
```

### 连接数据库
```python
import sqlite3
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("SELECT * FROM wrong_notes")
rows = cur.fetchall()
conn.close()
```

### 解析 wrong_notes.md 导入数据库
```python
import re

def parse_wrong_notes(md_path):
    """把 wrong_notes.md 解析成 [(category, title, content, priority), ...]"""
    notes = []
    category = ""
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("## "):
                # 分类：取"数字. 名称"里的名称
                category = re.sub(r"^## \d+\.\s*", "", line).split("（")[0]
            elif line.startswith("- **"):
                # 提取加粗标题
                m = re.match(r"- \*\*(.+?)\*\*[：:]\s*(.*)", line)
                title = m.group(1) if m else line[2:]
                content = m.group(2) if m else ""
                # 检测重点标记
                priority = ""
                for mark in ("🔴", "⚠️", "🚫"):
                    if mark in line:
                        priority = mark
                        break
                notes.append((category, title, content, priority))
    return notes
```

## 五、参考资源

- Flask 官方教程：https://flask.palletsprojects.com/tutorial/
- Bootstrap CDN：https://getbootstrap.com/docs/5.3/getting-started/introduction/
- Jinja2 模板：https://jinja.palletsprojects.com/

## 六、明天开新会话时说

```
"我要做 Flask 错题本项目，路径 web_wrong_notes/，已读启动方案，开始 Step 1"
```

---

**预计总时间**：1.5-2 小时（分5步，每步 15-20 分钟）  
**难度**：⭐⭐（比 tkinter 简单，代码量少）