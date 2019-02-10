Title: 学习centeos7系统
Slug: learning-centos7-system
Date: 2018-02-19
Modified: 2018-09-02
Tags: centos7

[TOC]

## 安装系统

centos7的安装目前最大的难点在硬盘分区上，加上新生代的uefi启动方式，还是有些新的问题需要讨论的。

记得以前早起折腾ubuntu系统时，最大的一个影响就是需要给linux系统安装预先分出一个swap分区，大约是内存的两倍，当时还不太懂这个有什么，按照 鸟哥的私房菜   一章的描述， 服务器一般内存都十几G-64G的内存，就不能按照这个公式来了，总之，分出3-4Gswap分区意思一下就可以了。



### 各个硬件在linux下的名字

这个需要了解下，参考 [鸟哥的私房菜第二章](http://linux.vbird.org/linux_basic/0130designlinux.php) ，

- 硬盘或者USB模拟的硬盘 ：   /dev/sd[a-p]
- CDROM或者DVDROM :  /dev/scd[0-1] , /dev/cdrom（当前cdrom） , /dev/sr[0-1]
- 打印机 ： /dev/lp[0-2] , /dev/usb/lp[0-15]
- 鼠标 ： /dev/input/mouse[0-15] , /dev/mouse (当前鼠标)

### UEFI 启动



### 分区推荐

按照鸟哥的私房菜推荐，不是随便玩玩，而是作为工作服务器，那么推荐还是如下多分几个区：

- /boot
- /
- /home
- /var
- swap


## firewall-cmd

防火墙策略管理命令： `firewall-cmd` ， 其中 `--list-all` 列出开启的端口号等情况， `--add-port` 来开放某个端口号，比如：

```
firewall-cmd --add-port=80/tcp
```

更多细节请参看 [这篇文章](http://wangchujiang.com/linux-command/c/firewall-cmd.html) ，下面就一些常用的用法简要说明之。

```bash
firewall-cmd --get-active-zones # 查看活动的区域
firewall-cmd --zone=work --add-interface=eth0 # 为某个区域指定网卡界面
# 默认的zone是public 
firewall-cmd --zone=work --list-ports # 列出所有开放的端口
firewall-cmd --zone=work --add-port=8080/tcp # 为某个区域开发端口
firewall-cmd --zone=work --add-service=ssh # 为某个区域开发服务
# 类似的还有 --remove-prot  和  --remove-service
firewall-cmd --get-services # 列出所有可用服务
```

**NOTICE:** 上面提及的操作如果不加 `--permanent` 参数那么只是临时有效，重启firewalld服务就会配置丢失。








## systemd

centos7引入了systemd，这真是一个好用的工具，以前我们接触的 `/etc/init.d` 下编写的服务脚本非常麻烦，然后我们喜欢使用supervisor来管理各个进程，现在假设有一个工具，一样简洁的配置管理语法，而且还是centos系统自带的，那么为什么不用这个工具来管理各个后台进程呢？这个工具就是systemd。

systemd服务都通过 `systemctl` 命令来管理的，实际上systemd是如此的基本，因为它已经取代inid成为了pid为1的进程，也就是后面的很多进程都是通过它来启动的，你甚至还可以通过systemctl来重启电脑，你就知道systemd服务是多么的底层了：

- systemctl reboot
- systemctl poweroff

system的systemd服务脚本放在 `/usr/lib/systemd/system` 哪里，用户的systemd服务脚本是放在 `/usr/lib/systemd/user` 哪里。或者你也可以放在 `/etc/systemd/system` 或者 `/etc/systemd/user` 哪里。

说是服务脚本，其实就是一个配置配置文件，内容大体如下：

```
[Unit]
Description=nginx - high performance web server
Documentation=http://nginx.org/en/docs/
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
PIDFile=/usr/local/nginx/logs/nginx.pid
ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf
ExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

Unit - Description 描述服务

Unit - Documentation 服务文档

Unit - After 服务依赖，只有依赖服务启动本服务才启动

Service - Type 启动类型，simple： 默认值，立即启动该服务； forking：以fork方式启动进程；oneshot：一次性进程；dbus：dbus启动；notify：服务启动完毕，通知systemd，然后继续向下执行。

Service - PIDFile pid文件路径

Service - ExecStartPre 启动前动作

Service - ExecStart 启动动作

Service - ExecReload reload动作

Service - ExecStop 停止动作

Service - PrivateTmp 临时空间

Service - ExecStartPost 启动后动作

Install  -  WantedBy 



systemd 东西还有点，后面有时间再慢慢补上，强烈推荐 [金步国翻译的systemd中文手册](http://www.jinbuguo.com/systemd/systemd.exec.html) 。





### 服务文件修改之后

一般是推荐配置文件外移，服务文件设置好之后就没必要修改了，如果服务文件修改了那么需要：

```
systemctl daemon-reload
```

### 日志管理

systemd统一管理所有日志，可用 `jourlnalctl` 命令来查看之。点名要看某个服务Unit：

```
jourlnalctl --unit=nginx
```

### 启动服务等等

启动服务重启服务暂停服务等等我想大家都很熟悉了吧：

```
systemctl start what.service
systemctl stop what.service
systemctl restart what.service
```

## centos7配置dns

发现centos7配置dns之后重启 network 服务配置就会丢失，需要在

```
/etc/NetworkManager/NetworkManager.conf
```

main哪里加上

```
dns = none
```

然后重启

```
systemctl restart NetworkManager.service
```

然后再如同以前一样修改 `/etc/resolv.conf` 。



## 配置语言



### 查看当前操作系统语言

```
cat /etc/locale.conf 
```

或者

```
localectl status
```

### 列出可用语言

```
locale -a
```
或者

```
localectl list-locales | grep zh
```



### 修改操作系统语言

```
sudo localectl set-locale LANG=zh_CN.utf8
```







## 参考资料

1. [鸟哥的私房菜](http://linux.vbird.org/linux_basic)
2. [systemd入门教程之命令](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html)
3. [systemd详解](https://www.xncoding.com/2016/06/07/linux/systemd.html)



