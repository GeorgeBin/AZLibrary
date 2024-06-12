# 本地图书库的下载与存储实践

关于 Pirate Library Mirror、Z-Library、Anna's Archive、Book Searcher



## 简介

目的：在自己的硬盘上囤积存储一些书籍

上网时看到了 Pirate Library Mirror 资源相关文章，看到其包含书籍约千万本，于是我的仓鼠症就犯了，想要收集下载这些文件。

其图书资源来源于 Z-Library，后被 Anna获取后 发布种子也就是 Pirate Library Mirror，再后来 Anna 构建了自己的网站 Anna's Archive，目标是收藏人类图书的 10%，目前已收录 5%。

于是我收集了种子，种子下载后，发现其内文件都是以  Z-Library ID（数字） 命名的，所以根据其提供的数据库文件，建立了索引。而后感觉这个东西可能有点用，所以整理了一下，提供出来。

主要内容：种子+索引+重命名脚本。



## 背景介绍

#### 来历：

- [Z-library 免魔法全攻略，看完直接拥有 31T 资源 - 奔跑中的奶酪](https://www.runningcheese.com/zlibrary)



#### 下载&处理：

* [Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)

* [zlibrary被封后，网上有许多zlibrary的种子。如何使用？ - 钥匙挂的回答 - 知乎](https://www.zhihu.com/question/567076605/answer/2812667224)



#### 大小：

- zlib1（7TB）
- zlib2（24TB）





## 我的摸索与实践

下载内容：zlib1（7TB）+ zlib2（24TB）

存储容量：随缘（取决于自己有几块硬盘）

存储介质：机械硬盘

硬盘格式：NTFS

下载方式：种子

下载软件：[qBittorrent](https://www.qbittorrent.org/download)

索引制作：MySQL 导出 txt

文件命名：zlibID-书名.格式

主要参考文章：[Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)



### 我的处理流程：

1. 下载种子文件

   * 种子文件来源：[Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)
   * 通过 md5 对比，与 [安娜的档案](https://annas-archive.org/torrents/zlib) 网站上提供的种子是同一文件

2. ~~索引获取方式一：直接使用软件进行重命名~~

   * 软件来源：[如何恢复从 Pirate Library Mirror 的 Z-Library 馆藏项目下载的电子书文件名](https://bookfere.com/post/1032.html)

   * 备注：不可行，软件使用的在线 API 已失效

3. ~~索引获取方式二：使用网友提供的 txt 文件~~

   * txt 文件来源：[Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)

   * 备注：文章内提供的 txt 为中文书籍，这样下载的其他书籍就浪费了😁

4. ~~索引获取方式三：使用 books.csv 导出索引~~

   * books.csv 来源：[zlib-searcher 相关资源 -Cmj's OneDrive](https://onedrive.caomingjun.com/zh-CN/%F0%9F%96%A5%E8%BD%AF%E4%BB%B6/zlib-searcher/)

   1. 使用网友提供的 books.csv（为 pilimi-zlib2-index-2022-08-24-fixed 全量导出） 文件
   2. Python 脚本处理：清理不可读字符，清理无用列
   3. Python 脚本处理：按照种子内文件范围，分割为多个索引 txt

   * 备注：此 csv 文件过大，无法用 Microsoft Office 打开
   * 备注：放弃此方式，csv 文件内有部分没有 id 的脏数据，难以处理

5. 索引获取方式四：下载 pilimi-zlib2-index-2022-08-24-fixed.torrent 自行导出

   * 导出方法来源：[Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)
   * pilimi-zlib2-index-2022-08-24-fixed.torrent  下载后解压约 8GB
   * 备注：不需要下载 pilimi-zlib-index-2022-06-28.torrent

6. 安装 MySQL

   * 安装时使用传统密码方式

   * 安装后，配置内存和超时时间
   * 注意 Mac 系统下 my.cnf 文件，使用命令行下 vim 编辑，否则可能会有编码问题

7. 安装 Nacivat

   1. 连接 MySQL
   2. 导入 sql 文件
   3. 编写 SQL 查询语句，测试确认语句可用

8. 安装 Python

   1. 这里使用的 PyCharm Community
   2. 安装 Python 环境以及用到的包

9. 导出索引 txt

   1. 使用 Python 脚本，连接 MySQL，从 txt 读取一行，拼接 SQL 语句
   2. 执行 SQL 语句，将结果保存到 txt 文件
   3. 批量重命名 txt 文件，和 torrent 文件名匹配

10. 一个种子下载完成后，使用 `rename_by_txt.py` 脚本 + “索引 txt”，重命名文件

11. 拷贝、存储

12. 继续下载下一个种子



## 其他选择

在线网站找书（单本下载）：

- Z-Library：官网、客户端、telegram 机器人
- Anna's Archive：官网

在线索引网站搜索 + IPFS（单本下载）

本地索引 Book Searcher + IPFS（单本下载）

下载：

- 种子（批量下载）
- ~~利用网盘离线种子~~（基本不可行了，被国内外各大网盘屏蔽，只有数据库种子能离线）
- IPFS（单本下载）
- Resilio Sync 同步（800GB 中文 epub 书籍，参考 [通过Resililo Sync下载Z-library中文EPUB图书（800G） - 梁川的文章 - 知乎](https://zhuanlan.zhihu.com/p/581771867)）
- 使用 NAS 下载（种子、Resilio Sync）

存储：

- 机械硬盘
- 磁带

直接购买：可尝试联系已经下载过此资源的各位大佬（适合公司）

- [Zbooks 软件作者](https://zhuanlan.zhihu.com/p/670325718)



> 备注：
>
> 1. 文章中提到的多数资源，需要魔法才能访问
> 2. 下载后的图书文件，尽量不要再上传网盘，可能会被封



## 参考链接：

[Z-Library](https://zh.singlelogin.re/)

[Anna's Archive](https://annas-archive.org/)

[qBittorrent](https://www.qbittorrent.org/download)



[Z-library 免魔法全攻略，看完直接拥有 31T 资源 - 奔跑中的奶酪](https://www.runningcheese.com/zlibrary)

[Pirate Library Mirror 项目研究 - 砂菱叶的文章 - 知乎](https://zhuanlan.zhihu.com/p/581483526)

[zlibrary被封后，网上有许多zlibrary的种子。如何使用？ - 钥匙挂的回答 - 知乎](https://www.zhihu.com/question/567076605/answer/2812667224)

[六百万册书，足够看几辈子 - 波罗揭谛 - 知乎](https://zhuanlan.zhihu.com/p/670325718)

[超千万本电子书资源](https://slyw.me/2022/11/12/200/)

[如何恢复从 Pirate Library Mirror 的 Z-Library 馆藏项目下载的电子书文件名](https://bookfere.com/post/1032.html)

[将全网电子书收入囊中 - 软件分享 - LINUX DO](https://linux.do/t/topic/48986/5)

[zlib-searcher 相关资源 -Cmj's OneDrive](https://onedrive.caomingjun.com/zh-CN/%F0%9F%96%A5%E8%BD%AF%E4%BB%B6/zlib-searcher/)

[通过Resililo Sync下载Z-library中文EPUB图书（800G） - 梁川的文章 - 知乎](https://zhuanlan.zhihu.com/p/581771867)
