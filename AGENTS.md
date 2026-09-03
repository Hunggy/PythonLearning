# Python 学习进阶项目

## 当前状态（2026-08-30）
- **六级备考（2026年9月考试）**：5 大考点（类对象/文件/可视化/SQLite/tkinter）全部完成；
  ACGO 3 卷（96/94/66 分）+ CODE STUDY 6 卷（58-68/76）+ 官方卷 1 张全刷完；
  **考前错题清单 v2 已备**：wrong_notes.md（8 卷 11 类）+ mini_mock.md + review_cheatsheet.md + tomorrow_plan.md
- ⚠️ 考纲：9月适用 **2020 修订版**（数据结构类 2027 才考，已学完不复习）
- **pinyin_tool/ ✅ 已完成（2026-08-30）**：韵母学习卡/辨识测试/错题本/曲线/打字练习全部完成；可选升级（介音字/简繁）未做，无计划
- 📌 完整历史进度（各卷错题复盘/刷题细节）见 `docs/progress_archive.md`——需要时再读，不常驻

## 开发者背景
- 已过电子学会 Python 二级（2026年9月备考六级）
- 语法基础扎实：if/for/函数/列表/字典/文件读写

## 协作原则
1. 结果优先：先给思路和提示，用户自己写代码，需要时给参考
2. 分步拆解：复杂项目按模块拆分，每步能独立运行
3. 适度注释：核心逻辑中文注释，新库方法说明用途
4. 报错友好：先给修复思路，附带错误原因
5. 不重复基础：默认掌握 if/for/函数等入门语法
6. 用户说"ok"时，自己读文件看进展，不要等用户贴代码
7. 新建项目：英文小写文件夹 + learn.py 骨架（仅任务提示，不写答案）
8. 图片识别：用户贴图→提取脚本→look_at/multimodal-looker 识别
9. 已识别图片文件名加 `_done` 后缀
10. 代写边界：界面/逻辑代码必须用户自己写——只给任务清单+提示级线索；资料性工作可补全

## 代码规范
- 文件名英文小写+下划线（learn.py）；变量函数蛇形命名；单行中文注释

## 工具环境（本项目相关）
- python 不在 PATH，完整路径：`C:\Users\Hunggy\AppData\Local\Programs\Python\Python314\python.exe`
- 图片提取：`D:\Temp\Temp\opencode\extract_latest_image.py`
- 浏览器操控（ACGO/CODE STUDY 刷题）：playwright-cli attach --extension=chrome（详见全局 AGENTS.md）

## 已掌握库
os / shutil / random / time / requests / openpyxl / tkinter / json / csv / sqlite3 /
matplotlib / numpy / 类与对象（封装/继承/多态/super/类变量）