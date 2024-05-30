# MySQL 安装、配置、启动

> 此文档针对 Mac 系统，介绍经验



### 下载

官方下载地址：https://downloads.mysql.com/archives/community/

筛选：选择操作系统、系统版本，如果系统版本里没有自己的版本，则调整 MySQL 版本，查找支持自己系统的版本。

因为我的系统是 Big Sur （11.7.10），所以下载的是 **macOS 11 (x86, 64-bit), DMG Archive**



### 安装

下载后直接安装，只是在安装的最后一步，选择密码类型时，选择旧版身份验证方法（legacy） 



### 配置

因为此次导入的数据库文件较大，所以需要配置 MySQL 内存和超时时长

如果导入过程报错

* server has gone away
* MySQL is running but PID file could not be found

则需要配置，可参考 本目录下 my.cnf 文件，注意用命令行下的 vim 编辑



### 启动、查看、关闭等操作

```sh
查看 MySQL 状态：sudo /usr/local/mysql/support-files/mysql.server status
关闭 MySQL：sudo /usr/local/mysql/support-files/mysql.server stop
启动 MySQL：sudo /usr/local/mysql/support-files/mysql.server start
```



