class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return '说明书'

haier = Washer(10,20)
print(haier)