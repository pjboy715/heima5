f = open('test.txt', 'r')

# 文件内容如果换行，底层有\n，会有字节占位
# read不写参数表示读取所有内容
print(f.read(11))

f.close()
