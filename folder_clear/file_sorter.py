"""
桌面文件自动分类器
扫描指定文件夹，按后缀自动分类移动到对应文件夹
"""
import os
import shutil

# 文件分类规则：后缀名 -> 目标文件夹
FILE_TYPES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "文档": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".md"],
    "视频": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def get_category(filename):
    """根据文件后缀判断分类"""
    ext = os.path.splitext(filename)[1].lower()  # 获取后缀并转小写
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "其他"  # 未匹配的文件统一放到「其他」文件夹


def sort_files(folder_path):
    """扫描并分类移动文件"""
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return

    # 统计移动结果
    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 跳过文件夹，只处理文件
        if not os.path.isfile(file_path):
            continue

        category = get_category(filename)
        # 目标文件夹路径
        target_dir = os.path.join(folder_path, category)
        # 目标文件完整路径
        target_path = os.path.join(target_dir, filename)

        # 创建目标文件夹（已存在则不报错）
        os.makedirs(target_dir, exist_ok=True)

        # 移动文件
        shutil.move(file_path, target_path)
        print(f"[{category}] {filename}")
        moved_count += 1

    print(f"\n完成！共移动 {moved_count} 个文件")


if __name__ == "__main__":
    # 默认扫描桌面，可修改为任意路径
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"正在扫描: {desktop}\n")
    sort_files(desktop)
