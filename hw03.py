'''задача № 1'''

def my_f(a, b):
    try:
        a = float(a)
        b = float(b)
        castnoe = a / b
        return castnoe
    except ZeroDivisionError:
        return 'На ноль делить нельзя! (но можно)'
    except ValueError:
        return 'Нужно ввести число.'

a = input('Введите первое число:')
b = input('Введите второе число:')
my_f(a, b)
print('Частное первого и второго числа:', my_f(a, b))

''' задача № 2'''

def user_info():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    year_ob = input('Год рождения: ')
    city = input('Город проживания: ')
    email = input('Электронная почта: ')
    phonenum = input('Номер телефона: ')
    print(name, surname, year_ob, city, email, phonenum)
user_info()

'''задача № 3'''

'''var 1'''
def my_func(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a >= b and b > c:
        s = a + b
        return s
    if a > b and c >= b:
        s = a + c
        return s
    if c >= a and b > a:
        s = b + c
        return s
a = input('Введите певое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')
print('Сумма наибольших чисел: ', my_func(a, b, c))

'''var2'''
def my_func(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a + b +c) - min(a, b, c)
    return s

a = input('Введите певое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')
print('Сумма наибольших чисел: ', my_func(a, b, c))

'''задача № 4'''

'''var 1 with **'''

def m_func(x, y):
    x = int(x)
    y = int(y)
    vstep = x ** y
    return vstep

x = input('Введите действительное положительное число x: ')
y = input('Введите целое отрицательное число y: ')
print('x в степени y: ', m_func(x, y))

'''var 2 with **'''

def m_func_2(x, y):
    x = int(x)
    y = int(y)
    d = int(y * -1)
    step = 1 / (x ** d)
    return step

x = input('Введите действительное положительное число x: ')
y = input('Введите целое отрицательное число y: ')
print('x в степени y: ', m_func_2(x, y))

'''задача № 5'''

def z_5():
    s = 0
    while True:
        try:
            li = input('Введите числа через пробел: ')
            li = [int(x) for x in li.split()]
            s += sum(li)
            print(s)
        except ValueError:
            for el in li:
                if el == 'q':
                    i = li.index(el)
                    li = li[0:i]
                    li = [int(x) for x in li.split()]
                    s += sum(li)
                    print(s)
                    return s

z_5()

'''задача № 6'''

def int_func():
    slovo = input('vvedite slovo malenkimi latinskimi bukvami:')
    if slovo.islower():
        print(slovo.capitalize())
    else:
        print('Error')
int_func()

'''задача № 7'''

def int_func():
    slovo = input('vvedite slova malenkimi latinskimi bukvami:')

    if slovo.islower():
        print(slovo.title())

    else:
        print('Error')
int_func()
