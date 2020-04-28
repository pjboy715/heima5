class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __del__(self):
        print('对象已删除')

haier = Washer(10,20)
del haier