# AZLibrary

下载 Z-Library 书籍，并重命名。

Download Z-Library by Pirate Library Mirror And Rename.



相关：

* 简体中文 | [English](README_eng.md)

* [处理过程流水账](other/README.md)



## 说明

* torrent：种子（书籍）
* index：用于重命名的索引（来自数据库导出）
* tree：用于重命名的索引（来自实际文件夹）
* other：其他文件，用于学习交流
  * reference：参考资料
  * process：处理时使用的过程文件
  * torrent-index：种子（数据库）



## 使用步骤



### 一、下载书籍

* 安装 BT 下载软件，推荐使用 [qBittorrent](https://www.qbittorrent.org/download)
* 通过种子下载：仅使用 torrent-zlib1、torrent-zlib2
* 一个种子下载完，就可进行此种子的重命名啦



### 二、重命名

#### 方式一：使用 index 重命名（来源：本资源 index 目录）

1. 安装 Python 环境，安装需要的 Python 包：pip install pathvalidate。
2. 运行 `rename_by_txt.py` 脚本。
   * 首先选择文件夹：存放下载书籍的文件夹。
   * 其次选择索引 txt 文件：注意和种子的对应关系。
   * 最后选择文件夹：重命名后，输出文件夹。
3. 脚本运行完成后，查看日志，手动处理未能成功重命名的文件。



> 备注：
>
> 有两个索引文件，因为超过了 100MB，所以分割为两部分，重命名时需注意。
>
> 百度网盘分享：链接: https://pan.baidu.com/s/1t4crgUno_STip0DU4caIkg?pwd=gyv9 提取码: gyv9



#### 方式二：使用 tree 重命名（来源：本资源 tree 目录）

1. 安装 Python 环境
2. 运行 `rename_by_tree.py` 脚本
   * 首先选择文件夹：存放下载书籍的文件夹。
   * 其次选择索引 txt 文件：注意和种子的对应关系。
   * 最后选择文件夹：重命名后，输出文件夹。
3. 脚本运行完成后，查看日志，手动处理未能成功重命名的文件。



> 备注：持续更新中
>



#### 方式一和方式二对比：

|        | 优点                         | 缺点                               |
| ------ | ---------------------------- | ---------------------------------- |
| 方式一 | 覆盖 zlib1、zlib2 所有种子   | 索引数远远大于实际文件数量，冗余高 |
| 方式二 | 根据实际文件目录生成，冗余低 | 未完全覆盖所有种子，持续更新中     |



### 三、其他

* 重命名后文件名称格式：ZlibID-文件名.格式

  ```sh
  示例：1-Руководство по не знаю чему 123213.fb2.zip
  如果不希望这样命名，可自行调整脚本
  ```

* pilimi-zlib-0-119999.torrent 作为第一个种子，下载速度较快，但没有中文书籍，且格式多为 fb2.zip





### 待办

- [ ] tree 索引：进行中
- [ ] zlib3
- [ ] Book Searcher 搭建
- [ ] zlib1（7TB），索引文件数量：x，实际文件数量：x
- [ ] zlib2（24TB），索引文件数量：x，实际文件数量：x
- [ ] zlib3（xTB），索引文件数量：x，实际文件数量：x
