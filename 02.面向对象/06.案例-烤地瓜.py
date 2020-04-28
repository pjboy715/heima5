# 1.定义类：初始化属性、被烤和添加调料方法、显示对象信息的str
class SweerPotato():
    def __init__(self):
        # 被烤时间
        self.cook_time = 0
        # 地瓜状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        # 烤地瓜的方法
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def add_condiment(self, condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

    def __str__(self):
        # 返回状态信息
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_state}，调料有{self.condiments}'


# 2.创建对象并调用对应的实例方法
digua1 = SweerPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiment('辣椒面儿')
print(digua1)

digua1.cook(3)
digua1.add_condiment('酱油')
print(digua1)
