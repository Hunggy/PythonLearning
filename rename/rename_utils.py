import os


#test = r"C:\Users\Hunggy\Desktop\PythonLearning\rename\test"

class RenameTool:
    def __init__(self, base_name):
        self.base_name = base_name


    def find_available_name(self, ext, existing):
        """given existing filenames, return first available numbered name"""
        num = 1
        while f"{self.base_name}_{num:03d}{ext}" in existing:
            num += 1
        return f"{self.base_name}_{num:03d}{ext}"

    def rename_files(self,folder_path):
        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)
            if not os.path.isfile(old_path):  # 确保是文件而不是目录
                continue  # Skip directories
            ext = os.path.splitext(filename)[1]  # 获取文件扩展名
            new_name = self.find_available_name(
                ext,
                os.listdir(folder_path)   # 现成目录列表
            )
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(old_path, new_path)
            except OSError as e:
                print(f"改名失败：{old_path} -> {new_path}. 错误: {e}")
