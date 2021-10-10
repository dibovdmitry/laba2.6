#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

if __name__ == '__main__':
    Airplane = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            path = input("Название пункта назначения рейса ")
            number = input("Номер рейса ")
            model = float(input("Тип самолёта "))

            Airplanes = {
                'path': path,
                'number': number,
                'model': model,
            }

            Airplane.append(Airplanes)
            if len(Airplane) > 1:
                Airplane.sort(key=lambda item: item.get('path', ''))

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

            for idx, Airplanes in enumerate(Airplane, 1):
                print(
                    '| {:>4} | {:<25} | {:<20} | {:>25} |'.format(
                        idx,
                        Airplanes.get('path', ''),
                        Airplanes.get('number', ''),
                        Airplanes.get('model', 0),
                    )
                )
            print(line)

        elif command.startswith('select '):
            today = date.today()

            parts = command.split(' ', maxsplit=2)
            sel = int(parts[1])

            count = 0
            for Airplanes in Airplane:
                if Airplanes.get('path') == sel:

                    count += 1
                    print(
                        '{:>4}: {}'.format(count, Airplanes.get('path', ''))
                    )
                    print('Номер рейса', Airplanes.get('number', ''))
                    print('Тип самолёта:', Airplanes.get('model', ''))

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
