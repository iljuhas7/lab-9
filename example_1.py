#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {'1а': 12, '1б': 24, '2а': 10, '2б': 8, '6a': 25, '6б': 13, '8а': 14, "9б": 12}
    while True:
        n = input('Введите название операции >>> ')
        if n == 'change':
            school.update({input(f'Название изменяемого класса: '): int(input(f'Количество учеников '
                                                                              f'изменяемого класса: '))})

        elif n == 'new':
            school.update({input(f'Название класса №: '): int(input(f'Количество учеников класса №: '))})

        elif n == 'remove':
            del school[input(f'Название расформировываемого класса: ')]

        elif n == 'print':
            print(school)

        elif n == 'sum':
            print(sum(school.values()))

        elif n == "help":
            print('\tchange - Изменилось количество учеников:')
            print('\tnew - В школе появился новый класс')
            print('\tremove - В школе был расформирован (удален) класс')
            print('\tprint - Выгрузка данных')
            print('\tsum - Число учеников')
            print('\texit - Выход')

        elif n == 'exit':
            break
