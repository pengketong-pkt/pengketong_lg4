"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""


# 定义Bug类
class Bug:
    def __init__(self, number, title, type, state, level):
        self.number = number  # bug编号
        self.title = title  # bug标题
        self.type = type  # bug类型
        self.state = state  # bug状态
        self.level = level  # bug等级

    # 创建bug方法
    def create(self):
        print("创建一个bug")

    # 关闭bug方法
    def close(self):
        print("关闭一个bug")


# 定义汽车类
class Car:
    def __init__(self, name, color, logo):  # 构造函数
        self.name = name  # 名称
        self.color = color  # 颜色
        self.logo = logo  # logo图标

    # 开车方法
    def drive(self):
        print("自驾游")


# 定义NewCar类继承于汽车类
class NewCar(Car):
    def __init__(self, name, color, logo, exhaust):  # 构造函数，覆盖父类的init方法
        self.exhaust = exhaust  # 排量
        super(NewCar, self).__init__(name, color, logo)  # 把父类的init方法继承回来


# 定义枪类
class Gun:
    def __init__(self, name):  # 构造函数
        self.name = name  # 枪名

    # 瞄准方法
    def aim(self):
        print("瞄准目标")


# 定义笔类
class Pen:
    def __init__(self, color):  # 构造函数
        self.color = color  # 颜色

    # 书写方法
    def write(self):
        print("写字")


# 定义水果类
class Fruit:
    def __init__(self, name, color):  # 构造函数
        self.name = name  # 名称
        self.color = color  # 颜色


if __name__ == "__main__":
    bug1 = Bug("001", "标题", "代码错误", "激活状态", "一级")  # 实例化Bug类一个对象
    bug1.create()  # 调用Bug类的创建bug方法
    bug1.close()  # 调用Bug类的关闭bug方法

    car1 = Car("哈佛H6", "white", "哈佛logo")  # 实例化Car类一个对象
    car1.drive()  # 调用Car类的开车方法

    newcar1 = NewCar("新车", "white", "新车logo", "2.0排量")  # 实例化NewCar类一个对象
    newcar1.drive()  # 调用Car类的开车方法
    print(newcar1.name)  # 调用Car类的实例变量

    gun = Gun("手枪")  # 实例化Gun类一个对象
    gun.aim()  # 调用瞄准方法

    pen = Pen("black")  # 实例化Pen类一个对象
    pen.write()  # 调用书写方法

    fruit = Fruit("苹果", "red")  # 实例化Fruit类一个对象
    print(fruit.color)  # 调用Fruit类的实例变量
