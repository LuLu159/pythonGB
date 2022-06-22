#1
class Mtrix:
    def __init__(self, mtrix_data):
        self.mtrix_data = mtrix_data

    def __str__(self):
        my_str = str()
        for row in self.mtrix_data:
            x = ' '.join(map(str, row))
            my_str += x + '\n'
        return my_str

#Не выходитсделать этот блок кода.
# Когда его запускаю, перестает работать первый блок с str
   # def __add__(self, other):
   #     mtr_sum = []
   #     for i in range(len(self.mtrix_data)):
   #        for j in range(len(self.mtrix_data[0])):
   #             mtr_sum.append(self.mtrix_data[i][j]+other.mtrix_data[i][j])
   #     return Mtrix(mtr_sum)

Matrix_2 = Mtrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
print(Matrix_2)

Matrix_3 = Mtrix([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
print(Matrix_3)
#print(Matrix_3+Matrix_2)

#2
from abc import ABC, abstractmethod
class MyAbstrClass(ABC):
    @abstractmethod
    def fabric_length(self):
        pass

class Clothes:
    def __init__(self, name, param):
        self.name = name
        self.param = param

class Coat(Clothes, MyAbstrClass):
    @property
    def fabric_length(self):
        return round((self.param / 6.5) + 0.5, 2)

class Suit(Clothes, MyAbstrClass):
    @property
    def fabric_length(self):
        return round((self.param * 2/100) + 0.3, 2)

suit1 = Suit('мужской костюм', 160)
print(suit1.fabric_length)

coat1 = Coat('зимнее пальто', 46)
print(coat1.fabric_length)

#3
class MyCells:
    def __init__(self, nucleus):
        self.nucleus = int(nucleus)

    def __add__(self, other):
        return MyCells(int(self.nucleus + other.nucleus))

    def __str__(self):
        return f'Клетка на {self.nucleus} ячеек'

    def __sub__(self, other):
        if self.nucleus >= other.nucleus:
            return MyCells(int(self.nucleus - other.nucleus))
        else:
            return 'Вычетание невозможно. Выбирайте клетку с большим количеством ячеек'

    def __mul__(self, other):
        return MyCells(int(self.nucleus * other.nucleus))

    def __truediv__(self, other):
        if self.nucleus // other.nucleus > 0:
            return MyCells(int(self.nucleus // other.nucleus))
        else:
            return 'Деление невозможно. Выбирайте клетку с большим количеством ячеек'

    def make_order(self, step):
        new_str = ('*' * step + '\n') * int(self.nucleus / step) + ('*' * (self.nucleus % step) + '\n')
        return new_str

cell1 = MyCells(10)
cell2 = MyCells(20)
cell3 = MyCells(18)
print(cell1+cell2)
print(cell3-cell2)
print(cell3*cell1)
print(cell3 / cell1)
print(cell2.make_order(3))