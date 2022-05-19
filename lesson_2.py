# task 1

common = ['domskky nado', 19, 'otprvit -', True]
for elem in common:
    print(type(elem))
# task 2
elements = input('Введите значения для списка, разделенные пробелом ').split()
if len(elements) % 2 == 0:
    for i in range(0, len(elements)-1):
        elements[i], elements[i+1] = elements[i+1], elements[i]
else:
    for i in range(0, len(elements)-2):
        elements[i], elements[i+1] = elements[i+1], elements[i]
print(elements)

# task 3
year = {'winter':[1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month = int(input('введите номер месяца '))
for elem in year:
    if month in year[elem]:
        print(elem)
        break

# task 4
sentence = input('Введите предложение').split()
for i, el in enumerate(sentence, 1):
    if len(el) > 10:
        print(i, el[0:10])
    else:
        print(i, el)

# task 5
rating = [9, 8, 6, 6, 5, 3, 3]
new_elem = int(input('Введите доп число '))
rating.append(new_elem)
rating.sort(reverse=True)
print(rating)