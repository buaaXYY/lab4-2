class People:
    name = "Tom"
    __age = 18

    def __init__(self, age):
        self.__age=age
        self.height = 1.75
        self.weight = 70

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def BMI(self):
        bmi = self.weight / self.height ** 2
        return bmi

p = People(20)
print(p.name)
print(People.name)

p.name = "张三"
print(p.name)
print(People.name)

print(p.get_age())
p.set_age(25)
print(p.get_age())

p.sex = "male"
print(p.sex)

if p.BMI()<23:
    print("Normal Weight!")
else:
    print("Over Weight!")







