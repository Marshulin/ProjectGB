'''задача №1'''

with open('new.txt', 'w+', encoding='utf-8') as f:
    st = 0
    while True:
        st = input('Введите данные: ')
        if st != '':
            f.write(f'{st}\n')
        if st == '':
            print('Ввод данных окончен!')
            break

'''задача №2'''

with open('text.txt', 'r+', encoding='utf-8') as f_obj:
    t = f_obj.readlines()
    print('Кол-во строк в файле: ', len(t))
    n = 0
    for el in t:
        el = el.split()
        n += 1
        print('Кол-во слов в строке №', n, ':', len(el))

'''задача №3'''

with open('sot.txt', 'r+', encoding='utf-8') as f:
    st = f.readlines()
    print('сотрудник имеет оклад менее 20 тысяч: ')

    for el in st:
        el = el.split()
        fio = el[0]
        zp = float(el[1])
        if zp < 20000:
            print(fio)
    newst = [el.split() for el in st]
    newst1 = [float(i[1]) for i in newst]
    sr = sum(newst1)//len(st)
    print('Средняя величина дохода сотрудников: ', sr)

'''задача №4'''

with open('eng.txt', 'r') as f:
    old_data = f.read()

    new_data = old_data.replace('One', 'Один')
    new_data = new_data.replace('Two', 'Два')
    new_data = new_data.replace('Tree', 'Три')
    new_data = new_data.replace('Four', 'Четыре')

with open('rus.txt', 'w', encoding='utf-8') as f:
    f.write(new_data)


'''задача №5'''

with open('new1.txt', 'w+') as f:
    arg1 = 1
    arg2 = 2
    arg3 = 3
    f.write(f'{arg1} {arg2} {arg3}')
    s = arg1 + arg2 + arg3
    print('Сумма чисел в файле: ', s)

'''задача №6'''

with open("pre.txt", 'r+', encoding='utf-8') as file:
    f = file.readlines()
    for el in f:
        h = ''
        for e in el:
            h = ''.join([h, (e if e in '0123456789' else ' ')])
        allh = [int(i) for i in h.split()]
        print(f'"{el.split()[0]}" - {sum(allh)}')


'''задача №7'''

with open("firmy.txt", 'r+', encoding='utf-8') as f:
    pribyl = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
    sredpribyl = {'average_profit': sum([int(el) for el in pribyl.values() if int(el) > 0])/ len([int(el) for el in pribyl.values() if int(el) > 0])}
    itigoviyspisok = [pribyl, sredpribyl]
    with open('firmy.json', 'w+', encoding='utf-8') as fj:
        import json
        json.dump(itigoviyspisok, fj)




