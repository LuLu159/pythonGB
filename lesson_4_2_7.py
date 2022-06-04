#1
# направлено отдельным файлом
#2
def sort_list(raw_list):
   new_list = [raw_list[i] for i in range(1, len(raw_list)) if raw_list[i] > raw_list[i-1]]
   return new_list

my_list = [2, 5, 6, 2, 6, 5, 7, 0, 1]
print(sort_list(my_list))

#3
new_list2 = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(new_list2)

#4
my_list3 = [5, 8, 8, 8, 1, 1, 2, 3, 4, 4]
new_list3 = [m for m in my_list3 if my_list3.count(m) == 1 ]
print(new_list3)

#5
def mult_numb(x, y):
   return x * y

from functools import reduce
my_list5 = [el for el in range(10, 1001, 2)]
print(reduce(mult_numb, my_list5))

#6/1
from itertools import count, cycle

j = int(input('Введите стартовое число от 0 до 10 '))
for el in count(j):
    if el > 15:
        break
    else:
        print(el)
# 6/2
i = 0
for elem in cycle('Марияспасибо'):
    if i > 23:
        break
    print(elem)
    i += 1

#7
import math
def fuct(n):
    for el in range(1, n+1):
        yield math.factorial(el)

numb = int(input('Введите число '))
func = fuct(numb)
for el in func:
    print(el)