import os
import shutil

desktop = r"C:\Users\Hunggy\Desktop"

# 1. 定义分类规则：后缀对应文件夹名

FILE_TYPES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif"],
    "文档": [".pdf", ".docx", ".txt"],
    "视频": [".mp4", ".avi", ".mkv"],
    "压缩包": [".zip", ".rar", ".7z"],
}
"""
for category, extensions in FILE_TYPES.items():
    if ext in extensions:
        print(f"属于: {category}")
        break
"""
# 2. 遍历桌面文件
"""
for filename in os.listdir(desktop):
    name, ext = os.path.splitext(filename)
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            print(f"属于: {category}")
            break

"""

for filename in os.listdir(desktop):
    name, ext = os.path.splitext(filename)
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            target_dir = os.path.join(desktop, category)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(os.path.join(desktop, filename), os.path.join(target_dir, filename))
           
            break
