# Django-Netnote
## 简述

本项目是基于Django框架的云笔记系统，实现多用户登录，注册以及笔记的添加修改删除等操作，HTML页面没有进行响应美化，主要是后端的操作；

- 用户注册成功后，会直接进入登录界面，输入账号密码登录即可
- 登录成功后，会记住登录状态，下次打开页面直接进入笔记页面
- 用户退出后，会清理session，则下次再进入页面时，需要输入账号密码

## 安装Django

使用命令：

```shell
sudo pip3 install Django==2.2.12
```

本项目使用的是MySQL数据库，因此下面进行MySQL数据库配置

### MySQL数据库配置

#### 安装MySQL

```
1.安装:sudo apt install mysql-server
2.查看默认安装的MySQL的用户名和密码:sudo cat /etc/mysql/debian.cnf
3.登录MySQL:mysql -u debian-sys-maint -p
4.输入上文查看的密码
5.进入MySQL:use mysql;
6.刷新权限:flush privileges;
7.修改用户名和密码:ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456'; #密码设置为123456
8.刷新权限:flush privileges;
9.退出:exit;
10.重启MySQL:service mysql restart
11.mysql -u root -p    # 回车后输入自己修改后的密码即可
```

#### 验证配置

安装前确认ubuntu是否已安装 python3-dev 和  default-libmysqlclient-dev

验证python3-dev，若无输出则没有安装

```shell
sudo apt list --installed|grep -E 'python3-dev' 
```

验证default-libmysqlclient-dev，若无输出则没有安装

```shell
sudo apt list --installed|grep -E 'libmysqlclient-dev' 
```

安装python3-dev

```shell
sudo apt-get install python3-dev
```

安装default-libmysqlclient-dev

```shell
sudo apt-get install default-libmysqlclient-dev
```

确保上述两个库已经安装，执行 sudo pip3 install mysqlclient即可 

#### 创建数据库

该项目使用的数据库名称为:netnote

进入数据库后，创建该数据库

```sql
create database netnote default charset utf8;
```

#### fork项目后的操作

fork项目后，除了上文提到的环境配置，需要在项目根目录下运行以下指令：

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

启动项目:

```shell
python3 manage.py runserver
```

此时打开浏览器输入地址：127.0.0.1即可 则会进入云笔记首页

