##定义动物类
import yaml


class Animal:
    name: str = ''
    color: str = ''
    age: int = 1
    gender: str = '有小鸡鸡'

    ##初始化变量值
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    ##定义父类方法
    def run(self):
        print(f"{self.name}会跑")

    def call(self):
        print(f"{self.name}会叫")


##实例化一个对象猫，调用类变量及类方法
# #cat =Animal("小猫","橘色",2,"有小鸡鸡")
# print(cat.gender)
# cat.run()

##定义子类猫咪，继承Animal的属性，并有独有属性 hair
class Cat(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name} 会捉老鼠")

    def call(self):
        print(f"{self.name} 喵喵叫")


# jumao =cat("短毛","橘猫","橘白色",4,"没有小鸡鸡")
# jumao.skill()
# jumao.call()

##同理 定义一个子类狗
class Dog(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name} 会看家")

    def call(self):
        print(f"{self.name} 汪汪叫")


# gg =dog("长毛","土狗","黑色",2,"有小鸡鸡")
# gg.skill()
# gg.call()


if __name__ == '__main__':
    ##默认打开文档，打开yaml数据文档，并赋值给变量a
    with open("AnimalDate.yml", encoding="UTF-8") as a:
        animal = yaml.safe_load(a)
        # print(animal['cat'])
        # print(animal['dog'])

    ##通过读取yaml内文件的值
    hair = animal['cat']['hair']
    name = animal['cat']['name']
    color = animal['cat']['color']
    age = animal['cat']['age']
    gender = animal['cat']['gender']

    cat = Cat(hair, name, color, age, gender)
    print(f"猫咪的毛毛：{hair}，猫咪的品种：{name},猫咪的颜色：{color},猫咪的年龄：{age},猫咪的性别：{gender}")
    cat.skill()

    hair = animal['dog']['hair']
    name = animal['dog']['name']
    color = animal['dog']['color']
    age = animal['dog']['age']
    gender = animal['dog']['gender']
    dog = Dog(hair, name, color, age, gender)
    print(f"狗狗的毛毛：{hair}，狗狗的品种：{name},狗狗的颜色：{color},狗狗的年龄：{age},狗狗的性别：{gender}")
    dog.skill()

    # hair =animal['default']['hair']
    # name =animal['default']['name']
    # color =animal['default']['color']
    # age =animal['default']['age']
    # gender =animal['default']['gender']
    # default =Cat(hair, name, color, age, gender)
    # print(f"猫咪的毛毛：{hair}，猫咪的品种：{name},猫咪的颜色：{color},猫咪的年龄：{age},猫咪的性别：{gender}")
    # default.skill()
