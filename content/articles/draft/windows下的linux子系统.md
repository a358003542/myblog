Title: windows下的linux子系统
Slug: wsl
Date: 2018-08-02
Tags: wsl,
Status: draft

WSL 在windows10里面是个新概念，大体可以看做mingw或者cygwin的替代吧。随着windows对WSL开发更新，发现这个东西在某些时候是可以解决某些程序在linux下能跑在windows下不能跑的问题。

## WSL配置
首先需要用管理员方式运行powershell，然后运行：

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

然后重启系统。这个必须做，否则wsl会提示错误。

然后进去了之后设置用户名和密码，这个没什么好说的，这里的用户名不一定是root。

然后在windows系统的 `Settings -> Update and Security-> For develops` 哪里打开 Devoloper Mode，不清楚为什么，但推荐做一下，参看的是 [官方文档的这里](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10) 。

这样你在windows下输入bash就可以进入ubuntu系统了，

## ssh连接

**NOTICE：** 本小节可选项，可以不看。

主要就是修改 `/etc/ssh/sshd_config` 的一些配置，首先推荐把端口号改为 2222 或者什么的，因为windows系统现在外面可能还有个ssh服务会占用22端口，然后：

```
UsePrivilegeSeparation no #因为wsl没有实现chroot
PasswordAuthentication yes
ListenAddress 127.0.0.1      # 安全考虑
```

然后会提示什么文件找不到错误，如下：

```
sudo ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
sudo ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
sudo ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
```

在重启ssh服务，应该问题不大了：

```
sudo service ssh --full-restart
```

**NOTICE:** 如果你把ubuntu关闭了，那么ssh也就连不上了，网上有些解决方案说制作一个开机脚本后台启动的，觉得太麻烦了，就这个任务不愿意这么折腾，开发的时候注意打开ssh服务就是了。



## 额外的安装软件包

gcc g++ make cmake gdb这些软件包是需要在 WSL 里面安装的，推荐直接如下一并安装了：

```
sudo apt update
sudo apt upgrade
sudo apt install build-esstial
```



这样应该c语言的开发环境就搭建起来了，WSL 还是给人一种怪怪的感觉，并不是很好用，不过也算是一种尝试吧。


## 参考资料
1. [wsl官方文档](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)
2.  [wsl的ssh配置](https://hbaaron.github.io/blog_2017/%E5%9C%A8wsl%E4%B8%8B%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8sshd%E5%85%A8%E6%94%BB%E7%95%A5/)