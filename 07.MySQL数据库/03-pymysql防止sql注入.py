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
# 准备sql语句，使用防sql注入的sql语句，%s是sql语句的参数和字符串的%s不一样，不要加引号
sql = 'SELECT * FROM yongle WHERE orderid = %s ;'
print(sql)

# 4.执行sql语句
cursor.execute(sql, (10000440,))
# 获取结果
result = cursor.fetchall()
for row in result:
    print(row)

# 5.关闭游标
cursor.close()

# 6.关闭连接
conn.close()
