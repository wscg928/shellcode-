import ctypes
import string
flag = "ctypes.windll.kernel32.RtlMoveMemory(    ctypes.c_uint64(ptr),    buf,    ctypes.c_int(len(llehscode)))"

new3_list=[]
new2_list=list(flag)
for i in new2_list:
	new3_list.append(ord(i)+6)

print(new3_list)