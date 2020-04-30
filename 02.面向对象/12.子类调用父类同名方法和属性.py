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
# 添加和父类同名的属性和方法
# 如果子类和父类拥有同名属性和方法，子类创建对象调用时为子类属性和方法
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'

    def make_cake(self):
        # 加自己的初始化原因:若不加自己的初始化,kongfu属性值将是上一次调用的init内的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性：将父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名.函数()
        # 再次调用初始化的原因：要调用父类的同名方法和属性，属性在init初始化位置，所以需要再次调用
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 用徒弟类创建对象，调用实例属性和方法
daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()

daqiu.make_master_cake()

daqiu.make_school_cake()

daqiu.make_cake()

# 查询继承关系
print(Prentice.__mro__)
