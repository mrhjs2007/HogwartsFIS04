# 1、自己写一个面向对象的例子：
#
# 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
import yaml


class Animal:

    #类的静态属性
    name = None
    color = None
    age = None
    gender = None

    #构造方法类的动态属性
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print(f"{self.name}会叫",end="")


    def run(self):
        print(f"{self.name}会跑")

# 创建子类【猫】，继承【动物类】，


class Cat(Animal):
    def __init__(self, name, color, age, gender,hair):

    # 复写父类的__init__方法，继承父类的属性，#继承父类的属性
        super().__init__(name, color, age, gender)

    #添加一个新的属性，毛发=短毛，
        self.hair = hair

    # 添加一个新的方法， 会捉老鼠，
    def catch(self):
        print("捉到了老鼠")



# 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def shout1(self):
        super().shout()
        print("喵喵叫")

# 创建子类【狗】，继承【动物类】，
class dog(Animal):

# 复写父类的__init__方法，继承父类的属性，
    def __init__(self,name, color, age, gender,hair):
        super().__init__(name, color, age, gender)
# 添加一个新的属性，毛发=长毛，
        self.hair = hair
# 添加一个新的方法， 会看家，
    def function(self):
        print("会看家")

#
# 复写父类的【会叫】的方法，改成【汪汪叫】
    def shout2(self):
        super().shout()
        print("会汪汪")
# 调用 name== ‘main’：

if __name__ == '__main__':

    with open("Animal.yaml","r",encoding="utf-8") as  f:
        datas1 = yaml.safe_load(f)
        #取yaml对应值
        # print(datas1['cat'][0])
        # print(datas1['dog'][0])
#实例化对象
cat1 = Cat(datas1['cat'][0], datas1['cat'][1],datas1['cat'][2], datas1['cat'][3],datas1['cat'][4])
print(f"名字叫‘{datas1['cat'][0]}’的猫，它颜色是{cat1.color},{cat1.age}岁，{cat1.gender},{cat1.hair}的小猫",end="")
cat1.catch()


# 创建一个猫猫实例
#
# 调用捉老鼠的方法
#
# 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

# 创建一个狗狗实例
dog1 = dog(datas1['dog'][0], datas1['dog'][1],datas1['dog'][2], datas1['dog'][3],datas1['dog'][4])

print(f"名字叫'{dog1.name}'的狗，它颜色是{dog1.color},年龄{dog1.age}岁,{dog1.gender},{dog1.hair}的小狗",end="")
# 调用【会看家】的方法
dog1.function()

# 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
#
# 2、使用yaml 来管理猫猫，狗狗的属性