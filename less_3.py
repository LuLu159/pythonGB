# 1
def division(numb1, numb2):
    try:
        numb_div = round(numb1 / numb2, 2)
        print(f'результат деления - {numb_div:0.2f} ')
    except ZeroDivisionError:
        print('Деление на ноль невозможно. Введите другое число')
'''
'''
numbers1 = int(input('Введите делимое '))
numbers2 = int(input('Введите делитель '))
division(numbers1, numbers2)

#2

def data_user(f_name, s_name, b_year, city, email, t_number):
    print(f'{f_name} / {s_name} / {b_year} /{city} / {email}/ {t_number}')

data_user(b_year=856, s_name="Sirius", f_name="Black", city="Hogvards", email = "SB@vandex.com", t_number= 123456)

#3
def two_max(my_list):
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    my_list.remove(max_2)
    two_m = max_1 + max_2
    return two_m

mylist = []
for i in range(1,4):
    mylist.append(int(input(f'введите {i} число ')))

print(two_max(mylist))

#4 / 1
def my_func(x, y):
    z = x ** y
    return z

x1 = int(input('Введи положительное число '))
y1 = int(input('Введи отрицательное число для введения в степеньо '))
print(f' Степень {y1} числа {x1} =  {my_func(x1, y1):0.3f}')

#4 / 2
def my_func1(x, y):
    z = 1
    if y<0:
       for i in range(0, abs(y)):
           z /= x
    else:
        for i in range(0, y):
           z *= x
    return z

x1 = int(input('Введи положительное число '))
y1 = int(input('Введи отрицательное число для введения в степеньо '))
print(f' Степень {y1} числа {x1} =  {my_func1(x1, y1):0.6f}')

#5
def my_sum(new_list):
   try:
      new_list = list(map(int, my_list))
      new_summ = sum(new_list)
      return new_summ
   except:
      print('введите корректную последовательность')

my_list = []
totl_sum = 0
my_list = input('Введите строку чисел, разделённых пробелом (остановка - S)').lower().split()

while 's' not in my_list:
   list_sum = my_sum(my_list)
   totl_sum += list_sum
   print(totl_sum)
   my_list = input('Введите строку чисел, разделённых пробелом (остановка - S)').split()
else:
   my_index = my_list.index('s')
   my_list = my_list[0:my_index]
   list_sum = my_sum(my_list)
   totl_sum += list_sum
   print(totl_sum)

#6
def int_func(my_world):
   My_world = my_world.title()
   return My_world

new_list = input('Введите слово ')
print(int_func(new_list))

#7
new_list2 = input('Введите текст ').split()
title_list = [int_func(el) for el in new_list2]
print(title_list)