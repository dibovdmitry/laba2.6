#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


if __name__ == '__main__':
    airplane = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            path = input("Название пункта назначения рейса ")
            number = input("Номер рейса ")
            model = float(input("Тип самолёта "))

            airplanes = {
                'path': path,
                'number': number,
                'model': model,
            }

            airplane.append(airplanes)
            if len(airplane) > 1:
                airplane.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '_' * 4,
                '_' * 25,
                '_' * 20,
                '_' * 25,
            )
            print(line)
            print(
                '| {:^4} | {:^25} | {:^20} | {:^25} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер рейса",
                    "Тип самолёта"
                )
            )
            print(line)

            for idx, airplanes in enumerate(airplane, 1):
                print(
                    '| {:>4} | {:<25} | {:<20} | {:>25} |'.format(
                        idx,
                        airplanes.get('path', ''),
                        airplanes.get('number', ''),
                        airplanes.get('model', 0),
                    )
                )
            print(line)

        elif command.startswith('select '):
            today = date.today()

            parts = command.split(' ', maxsplit=10)
            sel = str(parts[1])

            count = 0
            for airplanes in airplane:
                if airplanes.get('path') <= sel:

                    count += 1
                    print(
                        '{:>4}: {}'.format(count, airplanes.get('path', ''))
                    )
                    print('Номер рейса', airplanes.get('number', ''))
                    print('Тип самолёта:', airplanes.get('model', ''))

            if count == 0:
                print("Нет таких рейсов.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <товар> - информация о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)
