"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""

from learn_python.work2.tonglao import Tonglao


# 虚竹类继承童姥类
class xuzu(Tonglao):
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

    def read(self):
        print("罪过罪过")


xz = xuzu(100, 200)
xz.read()
