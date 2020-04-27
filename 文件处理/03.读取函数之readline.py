f = open('test.txt', 'r')

content = f.readline()
print(f'第一行：{content}')

content = f.readline()
print(f'第二行：{content}')

f.close()
