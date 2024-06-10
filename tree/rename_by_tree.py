import os
import tkinter as tk
from tkinter import filedialog

# 列名
header_names = ['id', 'name']


def parse_txt_file(filename):
    data = []
    numberOfIndexError = 0
    with open(filename, 'r', encoding='utf-8') as f:
        next(f)  # 跳过表头行
        for line in f:
            fields = line.strip().split('\t')
            if len(fields) != len(header_names):
                print(f"索引文件中，此行无法解析: {line.strip()}")
                numberOfIndexError = 1 + numberOfIndexError
                continue
            row_data = {header_names[index]: fields[index].strip('"') for index in range(len(header_names))}
            data.append(row_data)
    return data, numberOfIndexError


# 隐藏主窗口
root = tk.Tk()
root.withdraw()

InputFolderPath = filedialog.askdirectory()  # 下载文件所在目录
IndexFilePath = filedialog.askopenfilename()  # 索引文件
OutPutFolderPath = filedialog.askdirectory()  # 重命名后文件输出目录

bookIndexList, malformed_lines = parse_txt_file(IndexFilePath)

numberOfSuccess = 0
numberOfNotFound = 0
numberOfError = 0
numberOfWriteError = 0

# 重命名文件
for i, book in enumerate(bookIndexList, start=1):
    try:
        zlibrary_id = book["id"]
        fileName = book["name"]

        old_path = os.path.join(InputFolderPath, zlibrary_id)
        if os.path.exists(old_path):
            newname = f"{zlibrary_id}-{fileName}"
            new_path = os.path.join(OutPutFolderPath, newname)
            os.rename(old_path, new_path)
            numberOfSuccess += 1
        else:
            try:
                print(f"文件不存在：{zlibrary_id}")
                numberOfNotFound += 1
            except Exception as e2:
                print(f"写日志发生错误(rename_no.txt)：{e2}")
                numberOfWriteError += 1
    except Exception as e:
        print(f"重命名发生错误：{e}")
        numberOfError += 1

    if i % 100 == 0:
        print(f"进度：{i}/{len(bookIndexList)}")  # 每 100 条输出一次进度日志

# 打印统计信息
print(f"索引解析错误数量: {malformed_lines}")
print(f"重命名成功数量: {numberOfSuccess}")
print(f"文件不存在数量: {numberOfNotFound}")
print(f"重命名错误数量: {numberOfError}")
print(f"写日志发生错误数量: {numberOfWriteError}")

input("转换结束")
# root.destroy()
