'''
- 存储数据的位置：文件(student.data)
  - 加载文件数据
  - 修改数据后保存到文件
- 存储数据的形式：列表存储学员对象
- 系统功能
  - 添加学员
  - 删除学员
  - 修改学员
  - 查询学员信息
  - 显示所有学员信息
  - 保存学员信息
  - 退出系统
'''

from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据
        self.student_list = []

    # - 定义程序入口函数
    def run(self):
        #   - 加载数据
        self.load_student()
        while True:
            # - 显示功能菜单
            self.show_menu()
            #   - 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))
            #   - 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询所有学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统 -- 退出循环
                break

    # - 定义系统功能函数，添加、删除学员等
    # 显示功能菜单 -- 打印序号和功能对应关系 -- 静态方法
    @staticmethod
    def show_menu():
        print('{:-^15}'.format('请选择如下功能'))
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询所有学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')
        print('-' * 20)

    # 添加学员
    def add_student(self):
        # - 用户输入姓名、性别、手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号码：')

        # - 创建该学员对象 -- 类，类在student文件中，先导入student模块，再创建对象
        student = Student(name, gender, tel)

        # - 将该学员对象添加到列表
        self.student_list.append(student)

        # 打印信息
        print(self.student_list)
        print(student)

    # 删除学员
    def del_student(self):
        # - 用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # - 遍历学员数据列表，如果用户输入的学员姓名存在则删除，否则则提示该学员不存在
        for i in self.student_list:
            if del_name == i.name:
                # 删除该学员对象
                self.student_list.remove(i)
                break
        else:
            print('查无此人！')

        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 修改学员信息
    def modify_student(self):
        # - 用户输入目标学员姓名；
        modify_name = input('请输入要修改的学员姓名：')
        # - 遍历学员数据列表，如果用户输入的学员姓名存在则修改学员的姓名、性别、手机号数据，否则则提示该学员不存在
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入新的学员姓名：')
                i.gender = input('请输入新的学员性别：')
                i.tel = input('请输入新的学员手机号：')
                print(f'修改该学员信息成功，姓名：{i.name}，性别{i.gender}，手机号{i.tel}')
        else:
            print('查无此人！')

    # 查询学员信息
    def search_student(self):
        # - 用户输入目标学员姓名
        search_student = input('请输入您要搜索的学员姓名：')
        # - 遍历学员数据列表，如果用户输入的学员姓名存在则打印学员信息，否则提示该学员不存在
        for i in self.student_list:
            if search_student == i.name:
                print(f'姓名是{i.name}，性别是{i.gender}，手机号是{i.tel}')
                break
        else:
            print('查无此人！')

    # 显示所有学员信息
    def show_student(self):
        # 打印表头
        print('姓名\t性别\t手机号')
        # 遍历学员数据列表，打印所有学员信息
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 保存学员信息
    def save_student(self):
        # - 打开文件
        f = open('student.data', 'w')
        # - 文件写入数据
        # 文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(new_list))
        # - 关闭文件
        f.close()

    # 加载学员信息
    def load_student(self):
        # - 尝试以`"r"`模式打开学员数据文件，如果文件不存在则以`"w"`模式打开文件
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        # - 如果文件存在则读取数据并存储数据
        # - 读取数据
        else:
            data = f.read()
            # - 转换数据类型为列表并转换列表内的字典为对象，存储学员数据到学员列表
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # - 关闭文件
            f.close()
