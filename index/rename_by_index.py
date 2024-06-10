import os
import csv
import tkinter as tk
from tkinter import filedialog
from pathvalidate import sanitize_filename

# 列名
header_names = ['zlibrary_id', 'extension', 'title']
MAX_FILENAME_LENGTH = 250


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


error_file = os.path.join(OutPutFolderPath, 'rename_err.txt')  # 定义输出日志路径：发生错误
no_file = os.path.join(OutPutFolderPath, 'rename_no.txt')  # 定义输出日志路径：没有找到文件

bookIndexList, malformed_lines = parse_txt_file(IndexFilePath)

# 打开输入文件和错误文件
with open(error_file, 'w', newline='', encoding='utf-8') as errorfile, open(no_file, 'w', newline='', encoding='utf-8') as notFindFile:
    writer_err = csv.writer(errorfile)
    writer_err.writerow(['zlibrary_id', 'extension', 'title', 'err'])
    writer_no = csv.writer(notFindFile)
    writer_no.writerow(['zlibrary_id', 'extension', 'title'])

    numberOfSuccess = 0
    numberOfNotFound = 0
    numberOfError = 0
    numberOfWriteError = 0

    # 重命名文件
    for i, book in enumerate(bookIndexList, start=1):
        try:
            zlibrary_id = book["zlibrary_id"]
            extension = book["extension"]
            title = book["title"]
            # print(f"book={book}")

            old_path = os.path.join(InputFolderPath, zlibrary_id)
            if os.path.exists(old_path):

                max_title_length = MAX_FILENAME_LENGTH - len(zlibrary_id) - len(extension) - 3

                if len(title) > max_title_length:
                    truncated_title = title[:max_title_length]
                else:
                    truncated_title = title

                newname = f"{zlibrary_id}-{truncated_title}.{extension}"
                newname2 = sanitize_filename(newname)  # 移除非法字符-->如果长度超标，可能会造成后缀丢失
                new_path = os.path.join(OutPutFolderPath, newname2)
                os.rename(old_path, new_path)
                # print(f"文件存在：{zlibrary_id}")
                numberOfSuccess += 1
            else:
                try:
                    writer_no.writerow([zlibrary_id, extension, title])  # 文件不存在，记录到错误文件中
                    print(f"文件不存在：{zlibrary_id}")
                    numberOfNotFound += 1
                except Exception as e2:
                    print(f"写日志发生错误(rename_no.txt)：{e2}")
                    numberOfWriteError += 1
        except Exception as e:
            print(f"重命名发生错误：{e}")
            numberOfError += 1
            try:
                writer_err.writerow([zlibrary_id, extension, title, str(e)])  # 记录错误信息到错误文件中
            except Exception as e3:
                print(f"写日志发生错误(rename_err.txt)：{e3}")
                numberOfWriteError += 1

        if i % 1000 == 0:
            print(f"进度：{i}/{len(bookIndexList)}")  # 每 1000 条输出一次进度日志

# 打印统计信息
print(f"索引解析错误数量: {malformed_lines}")
print(f"重命名成功数量: {numberOfSuccess}")
print(f"文件不存在数量（有日志 rename_no.txt）: {numberOfNotFound}")
print(f"重命名错误数量（有日志 rename_err.txt）: {numberOfError}")
print(f"写日志发生错误数量: {numberOfWriteError}")

input("转换结束")
# root.destroy()
