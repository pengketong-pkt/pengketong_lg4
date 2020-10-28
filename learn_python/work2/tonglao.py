"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），
调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。
血多的一方获胜。
"""
#定义天山童姥类
class Tonglao:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

    def see_people(self, name):
        if name == "WYZ" or name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("无名之辈，跪下！")

    def fight_zms(self, enemy_hp, enemy_power):
        now_hp = self.hp / 2
        now_attack = self.attack * 10
        while True:
            now_hp = now_hp - enemy_power
            enemy_hp = enemy_hp - now_attack
            if now_hp <= 0:
                print("童姥竟然输了！")
                break
            elif enemy_hp <= 0:
                print("你输了")
                break


if __name__ == '__main__':
    tonglao = Tonglao(10000, 600)
    tonglao.see_people("丁春秋")
    tonglao.fight_zms(30000, 1300)