# 定义功能界面函数
def info_print():
    '''功能界面'''
    print('{:-^20}'.format('请选择功能'))
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-' * 24)


# 等待存储所有学员的信息
info = []


# 添加学员信息的函数
def add_info():
    '''添加学员函数'''
    # 用户输入：学号，姓名，手机号
    new_id = input('请输入学号')
    new_name = input('请输入姓名')
    new_tel = input('请输入手机号')
    # 判断是否添加：如果学员姓名已经存在则报错提示，不存在则添加数据
    global info
    # 不允许姓名重复：判断用户输入的姓名和列表中字典的name对应值相等提示
    for i in info:
        if new_name == i['name']:
            print('该用户已存在')
            # 用户已存在退出添加
            return
    # 姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print(info_dict)


# 删除学员
def del_info():
    '''删除学员'''
    # 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')
    global info
    # 判断学员是否存在：如果存在则删除，否则报错提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('用户不存在')
    print(info)


# 修改学员
def modify_info():
    '''修改学员'''
    # 用户输入要修改的学员姓名
    modify_name = input('请输入要修改的学员姓名：')
    global info
    # 判断学员是否存在：如果存在则修改手机号，否则报错提示
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入手机号')
            break
    else:
        print('用户不存在')
    print(info)


# 查询学员
def search_info():
    '''查询学员'''
    # 输入要查找的学员姓名：
    search_name = input('请输入要查询的学员姓名：')
    global info
    # 判断学员是否存在：如果存在则输出学员信息，否则报错提示
    for i in info:
        if search_name == i['name']:
            print('{:-^16}'.format('查找到学员信息如下：'))
            print(f'该学员的学号是{i["id"]}，姓名是{i["name"]}，手机号是{i["tel"]}')
            print('-' * 25)
            break
    else:
        print('用户不存在')
    print(info)


# 显示所有学员
def print_all():
    '''显示所有学员信息'''
    # 打印提示字
    print(f'学号\t姓名\t手机号')
    # 打印所有信息
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')


# 系统功能需要循环使用，直到用户输入6，才退出系统
while True:
    # 1.显示功能界面
    info_print()
    # 2.用户输入功能序号
    user_num = int(input('请输入功能序号：'))
    # 3.按照用户输入的功能序号，执行不同的功能
    # 如果用户输入1.执行添加；如果用户输入2.执行删除......--多重判断
    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        exit_flag = input('确认要退出吗？ yes or no')
        if exit_flag == 'yes':
            break
    else:
        print('输入错误，请重新输入：')
