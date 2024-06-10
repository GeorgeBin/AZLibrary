import os
import tkinter as tk
from tkinter import filedialog


# 隐藏主窗口
root = tk.Tk()
root.withdraw()

InputFolderPath = filedialog.askdirectory()  # 文件所在目录
intoTreeFilePath = filedialog.askopenfilename()  # 索引文件

with open(intoTreeFilePath, 'w', encoding='utf-8') as outfile:
    # 写入标题行
    outfile.write('"id"\t"name"\n')
    for filename in os.listdir(InputFolderPath):
        if os.path.isfile(os.path.join(InputFolderPath, filename)):
            # 分割文件名和扩展名
            name, _ = os.path.splitext(filename)
            # 检查是否包含 '-' 并分割 id 和 title
            if '-' in name:
                file_id, title = name.split('-', 1)
                # 按要求格式写入输出文件
                outfile.write(f'"{file_id}"\t"{title}{os.path.splitext(filename)[1]}"\n')


input("文件名提取结束")
# root.destroy()
