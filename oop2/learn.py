# 任务：继承与多态练习
# 目标：
#   1. 定义父类 Animal（有 name 属性和 speak 方法）
#   2. 定义子类 Dog(Animal) 和 Cat(Animal)，各自重写 speak
#   3. 分别实例化，调用 speak 看多态效果
# 提示：
#   - 继承：class 子类名(父类名):
#   - 重写：子类里定义同名方法即可覆盖父类
#   - 多个对象调用同一个方法，各自做各自的事 = 多态
#
# 写完再尝试：再加一个子类（如 Pig、Bird），不用改任何调用代码就能新增动物

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."  # 父类默认的叫声

class Dog(Animal):
    def speak(self):
        return "汪汪!"

class Cat(Animal):
    def speak(self):
        return "喵喵!"

class Pig(Animal):
    def speak(self):
        return "哼哼!"



"""
dog = Dog("旺财")
cat = Cat("小黑")
pig = Pig("麦兆")
print(dog.name,dog.speak())
print(cat.name,cat.speak())
print(pig.name,pig.speak())"""

animals = [Dog("旺财"), Cat("小黑"), Pig("麦兆")]

for a in animals:
    print(a.name, a.speak())