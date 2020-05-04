# 1.学员信息包含：姓名、性别、手机号；
# 2.添加`__str__`魔法方法，方便查看学员对象信息
class Student(object):
    def __init__(self, name, gender, tel):
        # 姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'
