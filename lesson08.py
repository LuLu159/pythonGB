#1
class Data_Birthday:
    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year

    @classmethod
    def set_date(cls, data):
        new_set = data.split('-')
        d, m, y = map(int, new_set)
        return cls(d, m, y)

    @staticmethod
    def valid_data(obj):
        if obj.d > 31:
            obj.d = 31
        elif obj.d < 1:
            obj.d = 1
        else:
            obj.d = obj.d
        if obj.m > 12:
            obj.m = 12
        elif obj.m < 1:
            obj.m = 1
        else:
            obj.m = obj.m
        if obj.y > 2022:
            obj.y = 2022
        return obj

    def __str__(self):
        return f'дата рождения: день - {self.d} месяц - {self.m} год - {self.y}'

my_set = '35-10-2020'
my_set2 = '5-15-1990'
d_1 = Data_Birthday.set_date(my_set)
print(d_1.d, d_1.m, d_1.y)
d_2 = Data_Birthday.valid_data(d_1)
print(d_2.d, d_2.m, d_2.y)
print(d_2)

d_3 = Data_Birthday.set_date(my_set2)
d_3 = Data_Birthday.valid_data(d_3)
print(d_3)

#2
class ZeroDiv(Exception):
    def __init__(self, text):
        self.text = text

try:
    numb1 = int(input('введи делимое '))
    numb2 = int(input('введи делиТель '))
    if numb2 == 0:
        raise ZeroDiv('Not null')

except (ValueError, ZeroDiv) as err:
    print(err)
else:
    print(numb1/numb2)
finally:
    print('the end')

#3
class ElemStr(Exception):
    def __init__(self, text):
        self.text = text
my_list = []
while True:
    try:
        numb = input('Введите целое число в список (для остановки - stop) ')
        if numb == 'stop':
            break
        elif numb.isnumeric() == False:
            raise ElemStr('Введите число')
    except (ElemStr) as err:
        print(err)
    else:
        my_list.append(numb)

print(*my_list)

#4, 5
class Stomach:
#Класс Желудок, который принимает еду с ограничением по каллорийности
    def __init__(self, name):
        self.condition = []
        self.volume = 0
        self.name = name

    def get_food(self, x, y):
        self.condition.append(x)
        self.volume += y

    def condition_stomach(self):
        if self.condition is None:
            return f"{self.name}'s stomach is empty"
        elif self.volume <= 2500:
            return f"{self.name}'s stomach has {self.condition[-1]}"
        else:
            return f"{self.name}'s stomach has {self.condition[-1]}. Stop eating today."

class Food:
    def __init__(self, kind, units):
        self.kind = kind
        self.units = units

    def __str__(self):
        return f"It's a {self.kind}"

class Meat(Food):
    def __init__(self, kind, units, preparation):
        super().__init__(kind, units)
        self.preparation = preparation

    def __str__(self):
        return f"It's a {self.preparation} {self.kind}"

class Fruit(Food):
    def __init__(self, kind, units):
        super().__init__(kind, units)

    def __str__(self):
        return f"It's a {self.kind}"

class Sweets(Food):
    def __init__(self, kind, units, sugar=True):
        super().__init__(kind, units)
        self.sugar = sugar

    def __str__(self):
        if self.sugar:
            return f"It's a {self.kind} with sugar"
        else:
            return f"It's a good sweets - {self.kind}"

m1 = Food('meat', 400)
v1 = Stomach('Vasily')
v1.get_food(m1.kind, m1.units)
print(m1)
print(v1.condition_stomach())

m2 = Meat('fish', 300, 'fried')
v1.get_food(m2.kind, m2.units)
print(v1.condition_stomach())
print(m2)

m3 = Sweets('chocolate', 2200)
print(m3)
v1.get_food(m3.kind, m3.units)
print(v1.condition_stomach())

#6
class Complex_number:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __add__(self, other):
        # (a1+b1i) + (a2+b2i) = (a1+a2) + (b1+b2)i
        return Complex_number(self.a + other.a, self.b + other.b)

    def __str__(self):
        if self.b > 0 and self.a != 0:
            return f'{self.a} + {self.b}i'
        elif self.b != 0 and self.a == 0:
            return f'{self.b}i'
        elif self.b < 0 and self.a != 0:
            return f'{self.a} {self.b}i'
        elif self.b == 0:
            return f'{self.a}'

    def __mul__(self, other):
        # (a1+b1i) * (a2+b2i) = (a1*a2 - b1*b2) + (b1*a2 + a1*b2) i
        return Complex_number((self.a * other.a - self.b * other.b), (self.b * other.a + self.a * other.b))

cmplx_num1 = Complex_number(2, 3)
cmplx_num2 = Complex_number(-2, -5)
cmplx_num3 = Complex_number(6, -3)
cmplx_num4 = Complex_number(1, 2)

print(cmplx_num1)
print(cmplx_num2 + cmplx_num1)
print(cmplx_num1 + cmplx_num3)
print(cmplx_num2 + cmplx_num3)

print(cmplx_num4 * cmplx_num1)
print(cmplx_num2 * cmplx_num3)