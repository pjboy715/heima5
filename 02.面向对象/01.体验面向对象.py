# 需求：洗衣机  功能：能洗衣服
# 1.定义洗衣机类
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)

    # 获取实例属性
    def print_info(self):
        print(f'洗衣机宽度是:{self.width}')
        print(f'洗衣机高度是:{self.height}')


# 2.创建对象
# 对象名 = 类名()
haier = Washer()

# 添加实例属性
haier.width = 500
haier.height = 800

# 3.验证成果
haier.wash()
print(haier)
haier.print_info()
