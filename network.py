#!/usr/bin/env python
#_*_encoding:utf-8_*_
#Input your ip address and netmask to figure out your network .
#申明：此脚本为交互式，默认情况下请执行python network.py
from IPy import IP
input_IP = raw_input('请输入ip地址:')
list1 = input_IP.split('.')
if len(list1) != 4:
  print "您输入的ip地址不合法，请重新输入！"
  exit()
for i in list1:
  if i.isdigit() == True and int(i) >=0 and int(i) <= 255:
    pass
  else:
    print "您输入的ip地址不合法，请重新输入！"
    exit()
input_Netmask = raw_input('请输入子网掩码:')
list2 = input_Netmask.split('.')
if len(list2) != 4:
  print "您输入的子网掩码不合法，请重新输入!"
  exit()
for i in list2:
  if i.isdigit() == True and int(i) >=0 and int(i) <= 255:
    pass
  else:
    print "您输入的子网掩码不合法，请重新输入!"
    exit()
print "您所在的网段为:%s" % (IP(input_IP).make_net(input_Netmask))
