Title: 理解SIP协议一书补充材料
Slug: understanding-sip-book-learning-notes
Date: 2019-08-30
Modified: 2019-09-20
Tags: protocol, sip



[TOC]

# 理解SIP一书补充材料

**下面是学习 Alan B. Johnston SIP Understanding the Session Initiation Protocol 这本书的内容 ** ，在学习阅读官方协议文档的基础上，选择了某些内容摘记在这里。



## 一个简单的会话建立例子


![img]({static}/images/sip_example_1.jpg)

1. Tesla先给Marconi发送INVITE消息

```text
INVITE sip:marconi@radio.org SIP/2.0
Via: SIP/2.0/UDP lab.high-voltage.org:5060;branch=z9hG4bKfw19b 
Max-Forwards: 70
To: G. Marconi <sip:Marconi@radio.org>
From: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 INVITE
Subject: About That Power Outage...
Contact: <sip:n.tesla@lab.high-voltage.org>
Content-Type: application/sdp
Content-Length: 158

v=0
o=Tesla 2890844526 2890844526 IN IP4 lab.high-voltage.org 
s=Phone Call
c=IN IP4 100.101.102.103
t=0 0
m=audio 49170 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

关于头字段的的含义解释更多的请参看官方文档对应部分。

2. Marconi给Tesla发送180响应 （To From Call-Id CSeq 都是直接Copy过来的， Via添加了一个received参数）更多响应信息制造细节参看官方文档
```text
SIP/2.0 180 Ringing
Via: SIP/2.0/UDP lab.high-voltage.org:5060;branch=z9hG4bKfw19b
;received=100.101.102.103
To: G. Marconi <sip:marconi@radio.org>;tag=a53e42
From: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 INVITE
Contact: <sip:marconi@tower.radio.org>
Content-Length: 0
```
3. 180响应会被忽略
4. 200响应 （还包含了sdp载体）

```text
SIP/2.0 200 OK
Via: SIP/2.0/UDP lab.high-voltage.org:5060;branch=z9hG4bKfw19b
;received=100.101.102.103
To: G. Marconi <sip:marconi@radio.org>;tag=a53e42
From: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 INVITE
Contact: <sip:marconi@tower.radio.org>
Content-Type: application/sdp
Content-Length: 155

v=0
o=Marconi 2890844528 2890844528 IN IP4 tower.radio.org 
s=Phone Call
c=IN IP4 200.201.202.203
t=0 0
m=audio 60000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

5. T给M发送ACK消息

```text
ACK sip:marconi@tower.radio.org SIP/2.0
Via: SIP/2.0/UDP lab.high-voltage.org:5060;branch=z9hG4bK321g 
Max-Forwards: 70
To: G. Marconi <sip:marconi@radio.org>;tag=a53e42
From: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 ACK
Content-Length: 0
```

6. 实际媒体会话过程
7. M给T发送BYE消息

```text
BYE sip:n.tesla@lab.high-voltage.org SIP/2.0
Via: SIP/2.0/UDP tower.radio.org:5060;branch=z9hG4bK392kf 
Max-Forwards: 70
To: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
From: G. Marconi <sip:marconi@radio.org>;tag=a53e42 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 BYE
Content-Length: 0
```

8. T给M发送BYE消息的200响应

```text
SIP/2.0 200 OK
Via: SIP/2.0/UDP tower.radio.org:5060;branch=z9hG4bK392kf
;received=200.201.202.203
To: Nikola Tesla <sip:n.tesla@high-voltage.org>;tag=76341 
From: G. Marconi <sip:marconi@radio.org>;tag=a53e42 
Call-ID: 123456789@lab.high-voltage.org
CSeq: 1 BYE
Content-Length: 0
```

INVITE方法是SIP协议里面很重要的一个方法，本例子可以说是最核心的SIP协议功能实现了。

关于本例子更多细节请参见官方文档，下面我会补充说明一些东西。

## 通过代理建立SIP呼叫例子

![Jietu20190911-114217](/Users/beixi/Desktop/Jietu20190911-114217.jpg)



## SIP注册例子




