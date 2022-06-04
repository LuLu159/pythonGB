from sys import argv
file_name, work_time, rate, bonus = argv
print(f'Зарплата сотрудника составит {int(work_time) * int(rate) + int(bonus)} рублей')
