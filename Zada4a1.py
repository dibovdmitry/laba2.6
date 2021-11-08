#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import date
import sys

if __name__ == '__main__':
    school = {'1а': 33, '1б': 29, '2а': 15, '2б': 19, '3а': 35, '3б': 15, '4а': 22, '4б': 32}
    for i in range(1):
        school.update({input('Название изменяемого класса: '): int(
            input('Количество учеников изменяемого класса: '))})
        school.update({input('Название нового класса: '): int(
            input('Количество учеников нового класса: '))})
        del school[input('Название расформировываемого класса: ')]
        sc = sum(school[item] for item in school)
        print('Начальная школа:', school)
        print('Количество учеников в начальной школе:', sc)
