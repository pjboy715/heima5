# 1.接收用户输入的文件名
old_name = input('请输入您要备份的文件名：')
print(old_name)

# 2.规划备份文件名
# 2.1提取目标文件后缀 --最右侧的点之后就是后缀名 --字符串从右查找rfind
index = old_name.rfind('.')
print(index)

# 判断文件名有效性
if index > 0:
    postfix = old_name[index:]

# 2.2组织备份的文件名，xx[备份]后缀
# 通过源文件名切片来组成新文件名
# print(old_name[:index])
# print(old_name[index:])
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)

# 3.备份文件写入数据(数据与原文件一直)
# 3.1打开源文件和备份文件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 3.2源文件读取，备份文件写入
# 不确定目标文件大小时，循环读取写入，避免文件过大
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

# 3.3关闭文件
old_f.close()
new_f.close()
