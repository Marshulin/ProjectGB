# задание № 1

a = 12
b = 8
print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)
print(a * b)
print(a ** b)

name = 'Marina'
city = 'Saint-Petersburg'
print('name:', name)
print('city:', city)

name = input('Введите ваше имя: ')
city = input('Введите ваш город: ')
print('name:', name)
print('city:', city)

a = int(input('введите первое число:'))
b = int(input('введите второе число:'))
print('сумма первого и второго числа:', a + b)

# задание № 2

sec = int(input('Введите секунды:'))
ss = sec % 60
mm = (sec % 3600) // 60
hh = sec // 3600
print('чч: ', hh, 'мм: ', mm, ' сс: ', ss, )

# задание № 3

n = input('Введите число n:')
a = n
b = n + n
c = n + n + n
a = int(a)
b = int(b)
c = int(c)
summa = int(a + b + c)
print('Сумма n+nn+nnn =', summa)

# задание № 4

num = int(input('Введите целое положительное число: '))
maxfig = 0

while num > 0:
    fig = num % 10
    num = num // 10
    if fig > maxfig:
        maxfig = fig
        if fig == 9:
            break

print(maxfig)

# задание № 5

profit = float(input('Сумма выручки в рублях: '))
losses = float(input('Укажите сумму убытков в рублях:'))
if profit > losses:
    print('Прибыль')
if profit < losses:
    print('Убытки')

# задание № 6

if profit > losses:
    prib = profit - losses
    rentab = prib / profit
    print('Рентабельность:', rentab)
    peop = int(input('Число сотрудников:'))
    icforone = prib / peop
    print('Прибыль на одного сотрудника:', icforone, 'рублей')

# задание № 7

a = int(input('kilometers on the first day:'))
b = int(input('kilometers goal:'))
day = 1

while a < b:
    a = a + ((a/100)*10)
    day += 1
    if a >= b:
        print('you wiil achieve the goal for:', day, 'days')
if a == b:
    print('you have already achieved your goal!')
