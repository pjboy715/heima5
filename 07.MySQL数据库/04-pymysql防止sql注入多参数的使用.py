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
sql = 'insert into yongle(orderid,account,pay,refund,payment,orderdate) values(%s,%s,%s,%s,%s,%s)'
print(sql)

try:
    # 4.执行sql语句,传入多参数可以使用列表、元组、字典
    cursor.execute(sql, (10000441, 60, 60, 60, 7, '2018-09-28',))
    # 提交修改的数据到数据库
    conn.commit()
except Exception as e:
    # 对修改的数据撤销回滚
    conn.rollback()

finally:
    # 5.关闭游标
    cursor.close()
    # 6.关闭连接
    conn.close()
