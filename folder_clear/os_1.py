import os

# 你的桌面路径（改成你自己的）
desktop = r"C:\Users\Hunggy\Desktop"

# 列出桌面所有文件名
files = os.listdir(desktop)

'''
for f in files:
    name, ext = os.path.splitext(f)
    print(f"文件名: {name}, 后缀: {ext}")
'''

"""photo = os.makedirs('C:\\Users\\Hunggy\\Desktop\\图片', exist_ok=True)"""

import shutil
original_folder = os.path.join(desktop, "ab11f3718e126ce1c1a444b1e8c52d10.jpeg")
target_folder = os.path.join(desktop, "图片", "ab11f3718e126ce1c1a444b1e8c52d10.jpeg")

shutil.move(original_folder, target_folder)
