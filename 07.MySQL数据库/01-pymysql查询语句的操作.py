# 1.导包
import pymysql

# 2.创建连接对象
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='qwe.123',
                       database='test1',
                       charset='utf8')

# 3.获取游标，操作sql语句
cursor = conn.cursor()
sql = 'select * from yongle;'

# 4.执行sql语句
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# 5.关闭游标
cursor.close()

# 6.关闭连接
conn.close()
