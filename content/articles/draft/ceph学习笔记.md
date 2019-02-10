Title: ceph学习笔记
Slug: ceph-tutorial
Date: 2016-11-06 22:52
Modified: 2016-11-06 22:52
Tags: ceph, 
Status: draft
[TOC]

# ceph入门

## ceph简介
ceph系统是一种分布式存储解决方案，可以通过多台计算机进行配置，搭建ceph集群并提供块设备存储、对象存储和文件系统服务。

ceph项目的设计思想是很先进的，其源于Sage Weil在加州大学攻读博士期间的一篇论文。ceph项目简单来说目的就是应对PB级别的存储需求的，当然ceph在设计上是没有存储理论上限的。

正如ceph官网所言：

>
>Ceph is a unified, distributed storage system designed for excellent performance, reliability and scalability.


ceph是一个分布式存储系统，提供了优良的性能，可靠性和可扩展性。可靠性就会ceph存储系统会尽可能地保证数据不会丢失，可扩展性包括系统规模和存储容量的可扩展。此外ceph在运维上还提供了自动化运维特性，包括数据自动replication；自动re-balancing；自动failure detection和自动failure recoery。

## ceph存储系统结构
ceph存储系统如下图所示分为四个层次：

![ceph_system_structure.png]({filename}/images/ceph_system_structure.png)

1. 首先是最底层的RADOS基础存储系统，所有存储在ceph系统的用户数据最终都是由这一层来存储的。理解RADOS是理解ceph系统的关键。

2. 基础库librados，这一层对底层RADOS系统进行抽象和封装，并向上提供API。

3. 高层应用接口，这一层有RADOS GW、RBD、ceph FS。分别提供对外网关接口，块设备接口和文件系统接口。

4. 应用层，基于librados和高层应用接口开发出来的应用方法，比如云对象存储，云硬盘等。


## RADOS存储系统结构
RADOS基础存储系统结构如下图所示：

![rados_system_structure]({filename}/images/rados_system_structure.png)

RADOS系统由很多OSDs组成，其称之为OSD deamon进程，ceph osd daemon 功能是存储数据，处理数据的复制、恢复、回填、再均衡并通过检查其他osd daemon的心跳来向ceph monitor提供一些监控信息。ceph monitor 维护着展示集群状态的各个图表。

PG（Placement Group）在RADOS存储系统中，最终存储的是一个具有最大size的最小对象Object，比如上层的文件最终将分成这样一系列的Object。PG是用来（基于CRUSH算法）组织Object和位置映射的，一个Object只能映射到一个PG，然后Object通过PG映射到多个OSDs上，这里就牵涉到数据分布均匀性和数据修复问题。



## ceph存储集群
整个ceph存储集群的部署就是配置好一个个ceph节点，还有网络，还有ceph存储集群。一个ceph存储集群至少需要一个ceph monitor 和两个ceph osd daemon（OSDs）。如果是ceph文件系统客户端则还需要ceph metadata server（MDS）。

- ceph status 或者 `ceph -s` ： 查看整个ceph集群的状态
- rados lspools ： 列出pool情况
- ceph osd tree : 列出osd的情况

- ceph metadata server 为ceph文件系统存储元数据。元数据服务器使得POSIX文件系统的用户在不对Ceph集群造成负担的前提下，执行诸如ls、find等基本命令。
- RBD rados block device 是ceph对外提供块设备服务
- MDS ceph文件系统依赖的元数据服务
- CRUSH ceph使用的数据分布算法



## 各个Map监控信息
- Montior Map： 包含集群的 fsid 、位置、名字、地址和端口，也包括当前版本、创建时间、最近修改时间。要查看监视器图，用 `ceph mon dump` 命令。

- OSD Map： 包含集群 fsid 、创建时间、最近修改时间、存储池列表、副本数量、归置组数量、OSD 列表及其状态（如 up 、 in ）。要查看OSD运行图，用 `ceph osd dump` 命令。

- PG Map： 包含归置组版本、其时间戳、最新的 OSD 运行图版本、占满率、以及各归置组详情，像归置组 ID 、 up set 、 acting set 、 PG 状态（如 active+clean ），和各存储池的数据使用情况统计。

- CRUSH Map： 包含存储设备列表、故障域树状结构（如设备、主机、机架、行、房间、等等）、和存储数据时如何利用此树状结构的规则。要查看 CRUSH 规则，执行 `ceph osd getcrushmap -o {filename}` 命令；然后用 `crushtool -d {comp-crushmap-filename} -o {decomp-crushmap-filename}` 反编译；然后就可以用 cat 或编辑器查看了。

- MDS Map： 包含当前 MDS 图的版本、创建时间、最近修改时间，还包含了存储元数据的存储池、元数据服务器列表、还有哪些元数据服务器是 up 且 in 的。要查看 MDS 图，执行 `ceph mds dump` 。

## cephx认证系统
ceph用cephx认证系统来认证用户和守护进程。

Cephx 用共享密钥来认证，即客户端和监视器集群各自都有客户端密钥的副本。这样的认证协议使参与双方不用展现密钥就能相互认证，就是说集群确信用户拥有密钥、而且用户相信集群有密钥的副本。

要使用 cephx ，管理员必须先设置好用户。在下面的图解里， client.admin 用户从命令行调用来生成一个用户及其密钥， Ceph 的认证子系统生成了用户名和密钥、副本存到监视器然后把此用户的密钥回传给 client.admin 用户，也就是说客户端和监视器共享着相同的密钥。




# 手工部署细节
- 唯一标识符 Unique identifier 也就是 `fsid` 是集群的唯一标识，你可以通过 `uuidgen` 命令来生成一个fsid，然后写入ceph的配置文件中，默认是 `/etc/ceph/ceph.conf` 。

- 集群名字 Cluster Name 每个ceph集群都有自己的名字，默认是 ceph 
- 监视器名字 Monitor Name 每个集群里面的各个监视器


关于 ceph.conf 的具体配置细节这里就不做讨论了，后面的手工安装过程已经预先假定ceph.conf已经配置好了。


## 手工安装mon
1. create_keyring

    ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
    ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --set-uid=0 --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow'
    ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring

2. create_monmap
   分为两步：创建monmap和往里面加入mon。

   /usr/bin/monmaptool --create ${MONMAP_FILE} --fsid ${FSID}
   /usr/bin/monmaptool --add ${monName} ${monIp} ${MONMAP_FILE}

3. mkfs_mon
   monmap初始化数据

   rm -rf /var/lib/ceph/mon/ceph-${monName}
    user_cmd  mkdir -p /var/lib/ceph/mon/ceph-${monName}
    user_cmd  /usr/bin/ceph-mon --mkfs -i ${monName} --monmap $MONMAP_FILE --keyring /tmp/ceph.mon.keyring

4. start_mon
   启动mon服务，注意新建了两个额外的空白文件。

   touch /var/lib/ceph/mon/ceph-${monName}/done
    touch /var/lib/ceph/mon/ceph-${monName}/sysvinit
    service ceph start mon.${monName}



# 手工添加osd
1. /configure_osd.sh", "create"
   这里的主体就是

   ceph osd create 

2. /configure_osd.sh", "configure"
   配置部分最复杂的就是硬盘分区文件夹对应管理，目前这一部分是没有问题的。

后面的配置参考官方文档做了极大些简化，如下所示：

    # Mkfs osd
    "/usr/bin/ceph-osd -i ${osdNum} --mkfs --mkkey"
    
    /usr/bin/ceph auth add osd.${osdNum} osd 'allow *' mon 'allow profile osd' -i /var/lib/ceph/osd/ceph-${osdNum}/keyring
    
    # Ensure bucket
    user_cmd "/usr/bin/ceph osd crush add-bucket ${localHostId} host"
    user_cmd "/usr/bin/ceph osd crush move ${localHostId} root=${rootName}"
    # Add to bucket
    user_cmd "/usr/bin/ceph osd crush add osd.${osdNum} 1.0 host=${localHostId}"
    check_return_code $? "Add osd.${osdNum} to ${localHostId}" ""
    # Start osd
    touch /var/lib/ceph/osd/ceph-${osdNum}/sysvinit
    service ceph start osd.${osdNum}


3. "/configure_osd.sh", "start_ceph_service"

   service ceph start osd
   service ceph start mon










## 网络配置问题

ceph默认你只有一个网络，也就是public network，不过推荐的设置是有两个网卡（这将会带来性能极大的提升），一个网卡： public network， 一个网卡： cluster network。cluster network最好不能连外网，这样会更加安全点。而且cluster网卡最好速度很快，这样各个osd之间通信传输数据才会高效，10Gbps是推荐。

cluster network主要是给osds通信用，所以ceph的其他组件其实还是都依赖于public network的。



### mon那边

ceph的monitor默认监听端口是 `6789` ，然后其只管public network，其用到的 `{iface}` 是public network 的interface，其所用到的 `{ip-address}` 是 public network 的IP address。其所用的netmask是public network的 `{netmask}` 。

```
sudo iptables -A INPUT -i {iface} -p tcp -s {ip-address}/{netmask} --dport 6789 -j ACCEPT
```



### mds那边

ceph的mds server监听public network从 6800 开始的第一个可用的端口。类似上面的其也只管public network，其用到的 `{iface}` 是public network 的interface，其所用到的 `{ip-address}` 是 public network 的IP address。其所用的netmask是public network的 `{netmask}` 。



```
sudo iptables -A INPUT -i {iface} -m multiport -p tcp -s {ip-address}/{netmask} --dports 6800:6810 -j ACCEPT
```

### osd那边

ceph的osd deamons从当前ceph节点上的6800端口开始找可用端口，一个osd deamon需要三个端口：

- 一个用于和clients和monitors通信
- 一个用于和其他osds通信
- 一个用于心跳通信（heartbeating）

这些端口都是限于ceph节点Host机器上的，可以重复，为了防止osd deamons重启端口未正常释放，确保后面还有一些富余的端口号。

公网和私网分离之后，clients会通过公网连接osds，然后各个osds之间会通过私网来连接。这些在iptables那边的rules是分开的。

```
sudo iptables -A INPUT -i {iface}  -m multiport -p tcp -s {ip-address}/{netmask} --dports 6800:6810 -j ACCEPT
```

请确保上面的6810满足你的osd deamons数量要求。

### ceph.conf的配置

ceph.conf配置定义了整个ceph集群的一些信息，有：

- 集群id 也就是fsid
- 认证配置
- 集群成员
- host names
- host addresses
- keyrings路径
- journals路径
- data路径
- 其他runtime配置

该文件的查找先后顺序如下所示：

1. `$CEPH_CONF` 环境变量
2. -c path/path -c命令行参量
3. /etc/ceph/ceph.conf 系统默认路径
4. ~/.ceph/config 本地用户路径
5. ./ceph.conf 当前工作路径



原则上这个配置文件是管理整个集群的所有daemons的，但具体到某个daemon进程上，它又是按照上面的查找顺序限于本机查找的，也就是说，整个ceph集群的配置统一工作，是需要额外的管理的。

####  具体配置的覆盖

具体配置的覆盖是 [global] -> [mon] -> [mon.a] ，其他daemon类似。

#### global

```
[global]
public network = {public-network/netmask} # 注意用诸如10.0.0.0/24这样的格式
cluster network = {cluster-network/netmask} # 如果你定义了cluster network，那么osds会把心跳，osds之间的replication recovery通信都走cluster network。
```

#### 网络配置最小要求

网络配置最小要求是ceph的deamon进程在ceph.conf文件里面应该找到 `host` 变量，这个host变量也就是所谓的hostname也就是所谓的 `hostname -s` 。然后就是ceph集群已经指明monitor的ip address和端口。

一般具体就是某个daemon section下设置 `host` ，然后mon或者某个mon section下设置 `mon addr` 这个变量。

关于daemon具体的 `addr` 可能是不需要设置的，还不清楚在什么情况下确定可以不设置。



## 硬盘和文件系统配置

osd daemon最好在一个单独的硬盘上，如果你一定要在一个硬盘上做多个osd，那么最好是先做分区工作。

生产上推荐是用 `XFS`  文件系统格式。如果你使用的是 `ext4` 文件系统格式，那么在你的ceph.conf配置的osd section上推荐加上这么一行：

```
filestore xattr use omap = true
```

然后ceph官方手册说了一些 `btrfs` 文件格式的好话，说如果测试的话推荐用这个文件系统格式。



## mon的配置

ceph的mons们维护着一个 master copy of cluster map，也就是ceph client 能够找到所有的ceph monitors ， ceph osd daemons ， ceph mds servers 通过连接一个ceph monitor 然后提出当前的 cluster map。有了这个cluster map还有 CRUSH 算法，ceph client就能够找到所有对象的位置了。



生产环境ceph集群最少应该有三个monitor daemon，测试环境可以只设一个mon。

mon daemon 默认把数据放在 `/var/lib/ceph/mon/$cluster-$id` 这里。



#### mon的部署基本流程

除非你用ceph-deploy工具不去考虑具体细节，否则mon的部署都应该如下流程走一遍，其中也包括一些cephx的认证配置的东西。

出于简洁性的考虑下面的步骤将会把对 ceph.conf 的一些配置更改操作步骤略去了，请读者自行补充。

1. 为你的集群创建一个 keyring 并为你的 mon 生成一个secret key

   ```
   ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
   ```

2. 生成一个administrator keyring 生成 client.admin 用户，并把这个用户加入到 keyring 中。

   ```
   ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --set-uid=0 --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow'
   ```

3. 把 client.admin 的key添加到 `ceph.mon.keyring` 里面

   ```
   ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
   ```

4. 生成mon map，将其保存到 `/tmp/monmap` 你至少需要一个 hostname 和 ip-address 参数，还有fsid参数，还有集群名字否则用默认的 `ceph` 。

   ```
   monmaptool --create --add {hostname} {ip-address} --fsid {uuid} /tmp/monmap
   ```

5. 确保你的mon data 文件夹是存在的

   ```
   sudo mkdir /var/lib/ceph/mon/{cluster-name}-{hostname}
   ```

6. 把上面的 mon map 还有keyring添加进来

   ```
   ceph-mon --mkfs -i {hostname} --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
   ```

7. 创建一个空白 `done` 文件

   ```
   sudo touch /var/lib/ceph/mon/ceph-node1/done
   ```

8. 启动mon

   ```
   sudo /etc/init.d/ceph start mon.node1
   ```




### mon之间的同步

当有多个mon的时候，mon之间会彼此看看谁有最新的cluster map，然后取出最新的cluster信息。在同步过程中，mon之间会出现三种角色：

1. Leader Leader第一个拥有最新的cluster map
2. Provider Provider有最新的cluster map，不过不是第一个有的。
3. Requester Requester的cluster map有点掉队了，需要进行同步操作。






## osd的配置

一个osd实际上就是一个ceph-osd deamon和Guest机上的一个存储点，如果一个Guest机上你设置了多个存储点，只需要一个ceph-osd deamon就可以了。



生产环境一般是一个节点（Guest机器）一个osd daemon，一个存储盘。

设置日志尺寸如下所示：

```
[osd]
osd journal size = 10000
```

osd daemon 默认把数据放在 `/var/lib/ceph/osd/$cluster-$id` 这里。你可以通过 `osd data` 改变这个值，推荐系统盘和osd盘分开，然后osd盘作为挂载点使用你需要先将其挂载好。

```
sudo mkfs -t {fstype} /dev/{disk}
sudo mount -o user_xattr /dev/{hdd} /var/lib/ceph/osd/ceph-{osd-number}
```



### osd的心跳

osd之间会彼此检查心跳（每6秒），这个心跳周期可以通过参数 `osd heartbeat interval `  来设置。如果一个osd deamon 20秒内没有返回心跳信息，那么就会被认为这个osd deamon `down` 了。这个时间可以通过 `osd heartbeat grace` 来设置。mon那边需要接受某个osd deamon `down` 的信息 `三次` 才会认为这个osd deamon已经down了。这个次数可以通过 `mon osd min down reports` ，默认一个osd报告者就可以了，你可以通过 `mon osd min down reporters` 来设置要求的报告者数目。

上面的是osd之间彼此沟通心跳，如果一个	osd没办法和任何其他的osd进行心跳沟通，那么每过30秒其会向mon请求最新的cluster map，这个时间由 `osd mon heartbeat interval`  设置。

然后是mon那边，如果一个osd deamon 一定时间内没有向mon进行报告，则会被认为是down了。具体有很多报告事件，这个后面再详细讨论。



### osd的日志

日志的大小至少是 ( drive speed * filestore max sync interval ) * 2 ，不过最常见的实践是给日志文件专门弄个分区（SSD），然后把整个分区都挂载为专门用做存储日志。

日志设置为 `osd journal` 默认路径是： `/var/lib/ceph/osd/$cluster-$id/journal` 

日志大小设置为 `osd journal size` 默认大小是： `0` ... ， 所以你想要日志就需要设置这个值。

```
osd journal size = {2 * (expected throughput * filestore max sync interval)}
```

上面期待的吞吐量取硬盘吞吐量或网络吞吐量的最小值。





## 认证配置

认证配置应该都是全局的放在global section哪里。

认证配置默认是开启 `cephx` 认证。生产环境肯定是要开启来的。测试并没有这个要求，但最好也开启，并习惯有这个认证配置的存在。



#### 开启cephx

1. 创建一个 client.admin 的keyring

   ```
   ceph auth get-or-create client.admin mon 'allow *' mds 'allow *' osd 'allow *' -o /etc/ceph/ceph.client.admin.keyring
   ```

   这一步只要目标点 `/etc/ceph/ceph.client.admin.keyring` 已经有了那么就不应该做了。

2. 为你的monitor集群创建monitor secret key，这一部分在前面mon的基本配置中也看到过。

   ```
   ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
   ```

3. 把上面创建的 monitor secret key复制到每个mon的mon data哪里去。

4. 为每个osd生成一个secret key

   ```
   ceph auth get-or-create osd.{$id} mon 'allow rwx' osd 'allow *' -o /var/lib/ceph/osd/ceph-{$id}/keyring
   ```

5. 为每个mds生成一个secret key

   ```
   ceph auth get-or-create mds.{$id} mon 'allow rwx' osd 'allow *' mds 'allow *' -o /var/lib/ceph/mds/ceph-{$id}/keyring
   ```

   ​


### 术语

- FQDN fqdn Full Qualified Domain Name 全称域名，全称域名包含两部分：hostname和domain name。目前fqdn和hostname都是node001...之类的，但ceph-ansible的代码里面有些地方会区分。
- hostname 这是最常见的一个概念，从vagrant起在各个机器里面就已经确定了，说hostname或者说 `hostname -s` 或者说 `host` 通常都是指 node001... 之类的。目前各个虚拟机hostname也是可以自己ping得通的，可能有些配置的hostname只是一个名字，有的会有网络含义，不管怎么说，以后到物理机，首先请确保目标物理机的hostname可以ping得通，免得引起不必要的麻烦。



### METAVARIABLE

在ceph.conf里面有些特殊的变量，ceph会自动填充它们给与它们合适的值。

- `$cluster`  扩展为ceph集群的名字，默认为 `ceph`
- `$type`  扩展为 mds 或者 osd 或者 mon ，具体取决于是当前那个daemon进程在使用这个配置文件。
- `$id`  扩展为当前daemon的identifier，比如说 `osd.0` ，该值就是 `0` 。
- `$host`  扩展为当前daemon进程的host变量值，这个前面说过了每个daemon进程在ceph.conf里面都应该找到其对应的host变量
- `$name` 等价于 `$type.$id` 



### 运行时更改配置

```
ceph tell {daemon-type}.{id or *} injectargs --{name} {value} [--{name} {value}]
```

具体配置名有可能需要加上 `_` 或 `-` 。

### 运行时查看配置

```
ceph daemon {daemon-type}.{id} config show | less
```



# 安装diamond模块

[https://github.com/python-diamond/Diamond](https://github.com/python-diamond/Diamond)

diamond是用来收集信息的，其发出的信息格式如下：

```
servers.wanze-ubuntu.iostat.sda6.writes_merged 60.000 1469329380
```

```
什么path 值是多少 时间戳
```

这种格式具有通用性，后面carbon部分就是接受这种信息格式，甚至后面自己写额外的数据发送也应该按照这种格式来。 

diamond依赖 `configobj` 和 `psutil` 这两个模块。其中configobj似乎还依赖six模块，而psutil安装则需要花费一点功夫，首先需要安装 gcc

```
yum install gcc
```

然后是 python-devel 

```
yum install python-devel
```



diamond这里安装的是4.0.451，安装同上，然后这个模块安装后会在虚拟环境下创建一些额外功能的文件夹和文件，这个下面详细说明之。

1.  bin/diamond 虚拟环境下的可执行脚本，后面类似的不多说了。
2.  etc/diamond 这里放着diamond的配置，后续python模块的配置都推荐类似放在这里。
3.  share/diamond 这里放着diamond的一些资源

类似的虚拟环境文件夹设置有：

-   var/run 下面放着pid文件
-   var/log 下面放着日志文件
-   storage/ 等下carbon和graphite-web都会往里面塞一些内容，作为内容存储的地方。

现在我们虚拟环境下运行 `diamond` 就可以看到这个命令了，只是需要指定配置文件在哪里。

将/opt/sdsom/venv/etc/diamond 下的 diamond.conf.example 改名为 diamond.conf （现在先这样编写，后面安装时可以考虑批量往etc等地方塞配置文件。）

```
# Pid file
pid_file = /opt/sdsom/venv/var/run/diamond.pid

# Directory to load collector modules from
collectors_path = /opt/sdsom/venv/share/diamond/collectors/

# Directory to load collector configs from
collectors_config_path = /opt/sdsom/venv/etc/diamond/collectors/

# Directory to load handler configs from
handlers_config_path = /opt/sdsom/venv/etc/diamond/handlers/

# Directory to load handler modules from
handlers_path = /opt/sdsom/venv/share/diamond/handlers/
```

原则上所有的这些文件都应该放入 `/opt/sdsom/venv` 里面，现在先暂时这样写死了，后面应该考虑配置文件自动基于模块填充的生成机制。

```
### Defaults options for all Handlers
[[default]]

[[ArchiveHandler]]

# File to write archive log files
log_file = /opt/sdsom/venv/var/log/diamond/archive.log
```

这里的host变量是sdsom模块后面怎么修改了的，现在测试简单填写为127.0.0.1即可。这里的port将和后面的carbon直接对应。

```
[[GraphiteHandler]]
### Options for GraphiteHandler

# Graphite server host
host = 127.0.0.1

# Port to send metrics to
port = 6601
```

```
[[GraphitePickleHandler]]
### Options for GraphitePickleHandler

# Graphite server host
host = 127.0.0.1

# Port to send metrics to
port = 6602
```

默认的这些信息收集器是开启的：

```
[[CPUCollector]]
enabled = True

[[DiskSpaceCollector]]
enabled = True

[[DiskUsageCollector]]
enabled = True

[[LoadAverageCollector]]
enabled = True

[[MemoryCollector]]
enabled = True

[[VMStatCollector]]
enabled = True
```

先暂时留一两个方便测试用即可。

```
[handler_rotated_file]
```

```
class = handlers.TimedRotatingFileHandler
level = DEBUG
formatter = default
# rotate at midnight, each day and keep 7 days
args = ('/opt/sdsom/venv/var/log/diamond/diamond.log', 'midnight', 1, 7)
```

有些文件夹需要手工创建下：

```
mkdir -p /opt/sdsom/venv/var/log/diamond
mkdir -p /opt/sdsom/venv/var/run
```

配置完了之后，如下开启一个diamond进程，后续可以考虑用supervisor来管理开启。

```
diamond -c /opt/sdsom/venv/etc/diamond/diamond.conf 
```



然后我们可以去看下创建的pid文件已经相应的日志文件。关闭该diamond进程就是kill掉该进程号即可。 

# diamond配置进阶



# carbon和whisper合作收集和存储信息

**注意：** carbon在虚拟环境下的安装需要额外安装参数配置。

```
pip install --install-option="--prefix=/opt/sdsom/venv" --install-option="--install-lib=/opt/sdsom/venv/lib/${PYTHON_VESRSION}/site-packages" carbon-0.9.15.tar.gz
```

其依赖于 Twisted ，先把它安装上去。注意最新版本的twisted已经不支持python2.6了。（其依赖于zope.interface，不是很大直接从网络上安装了）

其依赖于 txAMQP-0.6.2.tar.gz 直接从网络上安装了。

其额外创建了 storage 文件夹前面已经提及。其额外创建的conf文件夹，里面是一些配置文件，后续建议都统一到 etc/carbon/ 文件夹里面去。

examples 文件夹还不清楚有啥用。

bin里面多了一些python可执行脚本文件，其中 `carbon-cache` 是直接和whisper交互的，然后aggregator和relay是高级功能，后续可以慢慢了解。

```
validate-storage-schemas.py
carbon-cache.py
carbon-aggregator.py
carbon-client.py
carbon-relay.py
```

然后还需要安装 whisper 模块

然后在虚拟环境文件夹下的那个conf文件夹里面有个carbon.conf.example，将其改名为carbon.conf，稍微做如下修改：

```
GRAPHITE_ROOT = /opt/sdsom/venv/
LOG_DIR = /opt/sdsom/venv/var/log/carbon/
PID_DIR = /opt/sdsom/venv/var/run
```

类似的还需要创建一个 storage-schemas.conf 文件。

启动carbon-cache进程如下执行：

```
carbon-cache.py start 
```

此外还有 status stop 子命令。 然后我们可以去storage那边去看下具体的输出wsp文件。



# 本地安装graphite-web

```
pip install --install-option="--prefix=/opt/sdsom/venv" --install-option="--install-lib=/opt/sdsom/venv/webapp" graphite-web-0.9.15.tar.gz 
```

webapp那边实际上就是 graphite-web 的一个django app。

## 安装django

由于目前sdsom代码是基于django（1.5.1）此外graphite-web依赖于 django-tagging (0.3.1) ，这个最好先限定版本号。

## graphite-web 数据库创建

```
django-admin.py syncdb --pythonpath ./webapp  --settings graphite.settings 
```

## graphite-web shell调试

```
django-admin.py shell --pythonpath ./webapp  --settings graphite.settings 
```



## 第一次shell 测试

这里新引入一个依赖包 pytz 

```
from graphite.render.attime import parseATTime
from graphite.render.datalib import fetchData
from django.conf import settings
import pytz
tzinfo = pytz.timezone(settings.TIME_ZONE)
until_time = parseATTime('now', tzinfo)

series = fetchData({'startTime': parseATTime('-30min', tzinfo),'endTime':until_time,'now':until_time,'localOnly':True},'servers.localhost.iostat.sda2.iops')

res = [i for i in series[0]]

>>> res
[None, None, 2.727, None, None, None, None, 1.24, None, None, None, None, 2.63, None, None, None, None, 1.097, None, None, None, None, 1.077, None, None]
```

## 开启graphite-web

```
django-admin.py runserver --pythonpath ./webapp --settings graphite.settings 0.0.0.0:8080
```

### 重要信息

1.  graphite-web 里面的 local_settings 里面可能有一些参数很重要，需要设置，其会通过graphite模块里面加载settings时自动加载。

2.  graphite-web 外网网页实际上现在就可以看了，但是要正常显示图片还需要安装cairocffi这个模块，这个模块安装起来依赖的东西就多了（主要是libffi-devel这个系统包等），而就目前的项目架构来说是没有必要的。

3.  graphite-web 官方文档推荐的做法是通过其提供的render api来获取数据，其和这里的 fetchData 的主要区别有，直接fetch少了缓冲cache层，然后还少了其他一些不太重要的包装。

4.  如果仅仅只是利用fetchData或其中的某个模块，那么后续可以考虑安装参数改为：

    pip install --install-option="--prefix=/opt/sdsom/venv" --install-option="--install-lib=/opt/sdsom/venv/lib/python2.7/site-packages" graphite-web-0.9.15.tar.gz 

将这个graphite直接作为模块安装进去。

还有如果仅仅只是利用fetchData函数，最多考虑后续加上Cache层，没必要用apache服务起来，也没有必要设置wsgi或者和sdsom等后面的django框架集成在一起。实际上graphite-web这个模块的django层可以考虑完全抽离出去，只是如果懒得做的话就这样了。



-----

# 参考资料

1.  [ceph from scratch](https://tobegit3hub1.gitbooks.io/ceph_from_scratch/content/index.html)
2.  [ceph浅析上](http://www.csdn.net/article/2014-04-01/2819090-ceph-swift-on-openstack)
3.  [ceph浅析中](http://www.csdn.net/article/2014-04-08/2819192-ceph-swift-on-openstack-m)