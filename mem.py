#!/usr/bin/python
from ctypes import *
for  i  in  range(1,1000):
	mem=create_string_buffer(1048576*i)
	print i
	mem=None

