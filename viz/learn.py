import matplotlib.pyplot as plt

# 任务1：画第一张图——折线图
# 目标：显示温度变化折线图
# 数据：星期一到星期日的气温（自拟）
days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
temps = [25, 27, 26, 30, 33, 31, 29]

# 提示：
#   plt.plot(列表x, 列表y)  # 画折线
#   plt.xlabel("横轴名") / plt.ylabel("纵轴名")  # 坐标轴标签
#   plt.title("标题")      # 标题
#   plt.show()             # 显示图片（弹窗口）
#
# 跑起来看效果：应该弹出温度变化曲线窗口
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
"""
plt.plot(days, temps)
plt.xlabel("日期")
plt.ylabel("温度")
plt.title("一周气温变化")
plt.show()
"""
subjects = ["语文", "数学", "英语"]
scores = [85, 92, 88]
"""
plt.bar(subjects, scores)
plt.xlabel("科目")
plt.ylabel("分数")
plt.title("科目成绩")
plt.show()
"""

plt.figure(figsize=(8, 8))        # 一个画布
plt.subplot(2, 2, 1)              # 2行2列，第1个位置
plt.plot(days, temps)
plt.title("气温折线")

plt.subplot(2, 2, 2)              # 第2个位置
plt.bar(subjects, scores)
plt.title("成绩柱状")


labels =  ["优秀", "良好", "及格", "不及格"]
counts = [12, 18, 6, 3]

plt.subplot(2, 2, 3)              # 第3个位置
plt.pie(counts, labels=labels, autopct="%1.1f%%")
plt.title("成绩分布饼图")
plt.show()