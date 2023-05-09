

fo=open("foo.txt", "w+")
print(fo.name)


fo.write( "www.runoob.com!\nVery")
fo.close()
#!只有在close之后才能写入完成
#os.rename("foo.txt","foo1.txt" )
fo=open("foo.txt","r")
s=fo.read(5)
print(s)
print(fo.tell())
fo.seek(1)
print(fo.tell())
print(fo.read(5))
fo.seek(0,0)
s=fo.read()
print(s)
fo.close()
# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#!上面的语句等价于下面的with as 语句 切冒号后的二语句块结束后会自动调用close()
# with open('/path/to/file', 'r') as f:
#     print(f.read())