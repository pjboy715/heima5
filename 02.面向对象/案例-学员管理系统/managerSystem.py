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


class StudentManager(object):
    def __init__(self):
        # 存储学员数据
        self.student = []

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
        print('添加学员')

    # 删除学员
    def del_student(self):
        print('删除学员')

    # 修改学员信息
    def modify_student(self):
        print('修改学员信息')

    # 查询学员信息
    def search_student(self):
        print('查询学员信息')

    # 显示所有学员信息
    def show_student(self):
        print('显示所有学员信息')

    # 保存学员信息
    def save_student(self):
        print('保存学员信息')

    # 加载学员信息
    def load_student(self):
        print('加载学员信息')
