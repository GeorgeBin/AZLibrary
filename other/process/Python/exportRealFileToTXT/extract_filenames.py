import os
import tkinter as tk
from tkinter import filedialog

# 隐藏主窗口
root = tk.Tk()
root.withdraw()

# 选择文件所在目录
InputFolderPath = filedialog.askdirectory(title="请选择文件所在目录")

if not InputFolderPath:
    print("没有选择任何目录。程序退出。")
    exit(1)

# 获取父目录路径和文件夹名称
parent_dir = os.path.dirname(InputFolderPath)
folder_name = os.path.basename(InputFolderPath)

# 设置输出文件路径，输出文件位于与选择目录同级的路径下，并与目录同名
output_file = os.path.join(parent_dir, f"{folder_name}.txt")

# 打开输出文件进行写入
with open(output_file, 'w', encoding='utf-8') as outfile:
    # 写入标题行
    outfile.write('"id"\t"name"\n')
    for filename in os.listdir(InputFolderPath):
        if os.path.isfile(os.path.join(InputFolderPath, filename)):
            # 分割文件名和扩展名
            name, ext = os.path.splitext(filename)
            # 检查是否包含 '-' 并分割 id 和 title
            if '-' in name:
                file_id, title = name.split('-', 1)
                # 按要求格式写入输出文件
                outfile.write(f'"{file_id}"\t"{title}{ext}"\n')

print(f"文件名提取结束，结果已保存到: {output_file}")
input("按任意键退出...")


