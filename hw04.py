'''задание № 1'''

from sys import argv
print(argv)

path, v, s, p = argv
v, s, p = map(int, argv[1:])
zp = (v * s) + p
print(zp)

'''задание №2'''

old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [old[i] for i in range(1, len(old)) if old[i] > old[i - 1]]
print('Исходный список: ', old)
print('Элементы исходного списка, значения которых больше предыдущего элемента: ',new)

'''задание № 3'''

kratnye = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print("Кратные 20 и 21 числа в пределах от 20 до 240: ", kratnye)

'''задание №4'''

li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
newli = [el for el in li if li.count(el) == 1]
print('Представленный список: ',li)

print('Итоговый массив: ', newli)

'''задание №5'''

sp = [el for el in range(100, 1001) if el % 2 == 0]
print('Список чётных чисел от 100 до 1000: ', sp)
from functools import reduce
def su(a, b):
    res = a * b
    return res
print('Произведение всех элементов списка: ', reduce(su, sp))

'''задание №6'''

from itertools import count, cycle

for el in count(3):
    if el > 5:
        break
    print('Целое число от 3 до 10: ', el)

spi = [1, 2, 3]
print('Определённый список =) : ', spi)
i = 0
for el in cycle(spi):
    print('Элемент списка: ', el)
    i += 1
    if i > 5:
        break

'''задание №7'''

def fact(n):
    el = 1
    for i in range(1, n + 1):
        el *= i
        yield el

print('Факториалы чисел от 1 до n:')
n = int(input('Введите число "n" : '))
for el in fact(n):
    print(el)
