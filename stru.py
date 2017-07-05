# _*_ coding=utf-8 _*_
import struct

print "从左往右地址增加"


# native byteorder
buffer = struct.pack("ihb", 1, 2, 3)
print "本机小端规则"
print repr(buffer)
print struct.unpack("ihb", buffer)

# data from a sequence, network byteorder
data = [1, 2, 3]
buffer = struct.pack("!ihb", *data)
print "网络大端规则"
print repr(buffer)
print struct.unpack("!ihb", buffer)
