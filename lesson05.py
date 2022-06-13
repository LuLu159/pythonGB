#1
with open('test1.txt', 'w', encoding='utf-8') as f:
    line = ' '
    print('Введите данные. Дл окончания ввода данных используте пустую строку')
    while line != '':
        line = input()
        print(line, file=f)

#2
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for i, line in enumerate(text, 1):
        w = len(line.split())
        print(f'Строка {i} содержит {w} слов')
#3
worker = 0
sum_slr = 0

with open('fio.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sum_slr += int(line.split()[1])
        worker += 1
        if int(line.split()[1]) < 20000:
            print(line.split()[0])
print(f'Средняяя величина дохода сотрудников - {round(sum_slr / worker, 2)}')

#4
numb = {'One' : 'Раз', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

with open('test3.txt', 'w+', encoding='utf=8') as f1:
    with open('test2.txt', 'r', encoding='utf=8') as f2:
        for line in f2:
            f1.writelines(line.replace(line.split()[0], numb[line.split()[0]]))
        f2.seek(0)
        info = f2.read()
        print(info)
#5
from random import randint

with open('test5.txt', 'w', encoding='utf=8') as f:
    numbers = [randint(1, 10) for i in range(10)]
    f.write(' '.join(map(str, numbers)))

print('Сумма числе равна', sum(numbers))

#6
with open('test6.txt', 'r', encoding='utf-8') as f:
    full_text = f.readlines()
    for line in full_text:
        dic = ''
        for i in line:
            dic = ''.join([dic, (i if i in '1234567890' else ' ')])
        res = [int(x) for x in dic.split()]
        print(f'{line.split()[0]} : {sum(res)}')

#7
import json

with open('test8.json', 'w', encoding='utf-8') as f_write:
    with open('test7.txt', 'r', encoding='utf-8') as f_read:
        profit = {line.split()[0]: int(line.split()[2])- int(line.split()[3]) for line in f_read}
        result = [profit, {'average_profit': sum([int(i) for i in profit.values() if int(i) > 0])}]
    json.dump(result, f_write)
