# 师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 定义徒弟类，继承师傅类和学校类
# 当一个类有多个父类，默认使用第一个弗雷德同名属性和方法
class Prentice(School, Master):
    pass


# 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()
