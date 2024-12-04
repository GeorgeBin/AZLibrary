# AZLibrary

使用 [安娜的档案](https://annas-archive.li/) 提供的资源，下载书籍（包括 Z-Library 等），并重命名。

Download Books Use [Anna’s Archive](https://annas-archive.li/) And Rename. Include Pirate Library Mirror and so on.

. 

* 简体中文 | [English](README_eng.md)

* [处理过程流水账](other/README.md)

. 

## 说明

* torrent：种子（书籍）
* index：用于重命名的索引（来自数据库导出）
* tree：用于重命名的索引（来自实际文件夹）
* other：其他文件，用于学习交流
  * reference：参考资料
  * process：处理时使用的过程文件
  * torrent-index：种子（数据库）

.

## 使用步骤

.

### 一、下载书籍

* 安装 BT 下载软件，推荐使用 [qBittorrent](https://www.qbittorrent.org/download)
* 通过种子下载：仅使用 torrent-zlib1、torrent-zlib2
* 一个种子下载完，就可进行此种子的重命名啦

.

### 二、重命名

#### 方式一：使用 index 重命名（来源：本资源 index 目录）

1. 安装 Python 环境，安装需要的 Python 包：pip install pathvalidate。
2. 运行 `rename_by_txt.py` 脚本。
   * 首先选择文件夹：存放下载书籍的文件夹。
   * 其次选择索引 txt 文件：注意和种子的对应关系。
   * 最后选择文件夹：重命名后，输出文件夹。
3. 脚本运行完成后，查看日志，手动处理未能成功重命名的文件。

.

> 备注：有两个索引文件，因超过 100MB，分割为两部分，重命名时需注意。
>

.

#### 方式二：使用 tree 重命名（来源：本资源 tree 目录）

1. 安装 Python 环境
2. 运行 `rename_by_tree.py` 脚本
   * 首先选择文件夹：存放下载书籍的文件夹。
   * 其次选择索引 txt 文件：注意和种子的对应关系。
   * 最后选择文件夹：重命名后，输出文件夹。
3. 脚本运行完成后，查看日志，手动处理未能成功重命名的文件。

.

> 备注：持续更新中
>

.

#### 方式一和方式二对比：

|        | 优点                         | 缺点                               |
| ------ | ---------------------------- | ---------------------------------- |
| 方式一 | -                            | 索引数远远大于实际文件数量，冗余高 |
| 方式二 | 根据实际文件目录生成，冗余低 | -                                  |

.

### 三、其他

* 重命名后文件名称格式：ZlibID-文件名.格式

  ```sh
  示例：1-Руководство по не знаю чему 123213.fb2.zip
  如果不希望这样命名，可自行调整脚本
  ```

* pilimi-zlib-0-119999.torrent 作为第一个种子，下载速度较快，但没有中文书籍，且格式多为 fb2.zip


.

### 待办

- [ ] 本地 Book Searcher 搭建
- [ ] zlib3
- [ ] duxiu

.

## Release

* zlib1：[已 release](https://github.com/GeorgeBin/AZLibrary/releases/tag/zlib1)

  * 总大小：6.15 TB
  * 索引文件数量：1468 万
  * 实际文件数量：218 万
* zlib2：[已 release](https://github.com/GeorgeBin/AZLibrary/releases/tag/zlib2)
  * 总大小：21.5 TB
  * 索引文件数量：775 万
  * 实际文件数量：381 万



## 历程

* 2024.12.04：zlib2 处理完成，发布 release
* 2024.11.20：研究 zlib3，发现网站提供了 duxiu 资源，一起研究一下
* 2024.11.19：更新了zlib2 相关资源
* 2024.07.04：发现百度网盘分享失效，移除分享链接
* 2024.07.04：zlib1 处理完成，发布 release
