# 1.定义类，定义类属性
class Dog(object):
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

# 修改类属性
# 1.通过类进行修改
# Dog.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)

# 2.测试通过对象修改类属性,结果是为目标对象创建了一个实例属性，类和其他对象无影响
wangcai.tooth = 200
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)
