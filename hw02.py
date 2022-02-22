# задание № 1

li = [26, 'day', 'hello', 11, 'world', 7, 'happy', True, False]
print('Первый вариант:')
for element in li:
    print(type(element))
print('Второй вариант:')
for i in range(0,len(li)):
    print(type(li[i]))

# задание № 2

li1 = input('elementy:').split()
print(li1)

for i in range(1, len(li1), 2):
    li1[i - 1], li1[i] = li1[i], li1[i - 1]
    if len(li1) / 2 == int():
        li1[-1] = li1[-1]

print(li1)


# задание № 3

# через dict

di = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

num = int(input('Введите месяц в виде целого числа от 1 до 12:'))
for el in di:
    if num in di[el]:
        print(el)

# через list

z = [12, 1, 2]
v = [3, 4, 5]
s = [6, 7, 8]
a = [9, 10, 11]

num = int(input('Введите месяц в виде целого числа от 1 до 12:'))

for el in z, v, s, a:
    if num in z:
        print('зима')
        break
    if num in v:
        print('весна')
        break
    if num in s:
        print('лето')
        break
    if num in a:
        print('осень')
        break

# задание № 4

st = str(input('Введите строку из нескольких слов, разделённых пробелами:')).split()
for i, word in enumerate(st, 1):
    print(i, word[0:10])

# задание № 5

my_list = [7, 5, 3, 3, 2]
while True:
    num = int(input('Введите натуральное число:'))
    for el in my_list:
        if el == num:
            my_list.index(el)
            my_list.insert(my_list.index(el), num)
            print(my_list)
            break

        if el < num:
            my_list.index(el)
            my_list.insert(my_list.index(el), num)
            print(my_list)
            break
        if num < my_list[-1]:
            my_list.append(num)
            print(my_list)
            break




























# задание № 6