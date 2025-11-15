import os


orders = []
filename = 'pizza.txt'
p = True
try:
    if not os.path.exists(filename):
        print(f'Ошибка: файл "{filename}" не существует!')
        p = False
        
    elif os.path.getsize(filename) == 0:
        print(f'Ошибка: файл "{filename}" пустой!')
        p = False

    else:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                order = line.split()
                if len(order) == 3: 
                    if order[2].isdigit():
                        orders.append(order)
                    else:
                        print('Ошибка: стоимость заказа должна быть числом!')
                        p = False
                        break
                else:
                    print('Ошибка: строка должна быть формата: дата название_пиццы стоимость_заказа!')
                    p = False
                    break

except Exception as e:
    print(f'Ошибка при работе с файлом: {e}')
    p = False

while p == True:
    while True:
        print('Выберите опцию:\n1. Список пицц\n2. Список дат\n3. Самый дорогой заказ\n4. Средняя стоимость заказа\n0. Выход')
        n = input('>>> ')

        if n in '12340':
            break
        else:
            print('Нет такой опции!\n')

    if n == '0':
        break

    elif n == '1':
        report1 = {}

        for i in orders:
            if i[1] in report1:
                report1[i[1]] += 1
            else:
                report1[i[1]] = 1
        
        report1 = dict(sorted(report1.items(), key=lambda x: x[1], reverse=True))

        print('\nСписок пицц:')
        for key in report1:
            print(f'{key}: {report1[key]}шт')

    elif n == '2':
        report2 = {}

        for i in orders:
            if i[0] in report2:
                report2[i[0]] += int(i[2])
            else:
                report2[i[0]] = int(i[2])
        
        print('\nСписок дат:')
        for key in report2:
            print(f'{key}: {report2[key]}руб')
    
    elif n == '3':
        report3 = []
        max = 0

        for i in orders:
            if max < int(i[2]):
                max = int(i[2])
                report3 = i

        print(f'\nСамый дорогой заказ был сделан {report3[0]}.\nЗаказали {report3[1]} на сумму {report3[2]}руб.')

    elif n == '4':
        report4 = 0
        q = 0

        for i in orders:
            report4 += int(i[2])
            q += 1
        report4 /= q

        print(f'\nСредняя стоимость заказа: {report4:.2f}')

    print('')
