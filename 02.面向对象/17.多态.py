# 定义父类，提供公共方法
class Dog(object):
    def work(self):
        print('指哪打哪')


# 定义子类，子类重写父类方法
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


# 创建对象，调用不同的功能，传入不同的对象，观察执行结果
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
