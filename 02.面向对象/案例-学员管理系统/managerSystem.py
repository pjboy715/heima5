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

