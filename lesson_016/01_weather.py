# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

import argparse

import datetime
import sys
from pprint import pprint

from parser_weather import DatabaseUpdater, ImageMaker

version = "0.0.1"

im = ImageMaker()
db_updater = DatabaseUpdater()


def create_parser():
    arg_parser = argparse.ArgumentParser(
        prog="WEATHER",
        description="""Программа по парсингу, сохранению, 
                                         рисованию и показу погоды за выбранные даты""",
        epilog="""(c)Автор не несет никакой ответственности ни за что.""",
        add_help=False,
    )

    parent_group = arg_parser.add_argument_group(title="Параметры")
    parent_group.add_argument("-h", "--help", action="help", help="Справка")
    parent_group.add_argument(
        "-v",
        "--version",
        action="version",
        help="Вывести номер версии",
        version="%(prog)s {}".format(version),
    )

    subparsers = arg_parser.add_subparsers(dest="command")

    # Добавление прогнозов за диапазон дат в базу данных
    save_weather_data_parser = subparsers.add_parser(
        "save",
        add_help=False,
        help="=> adding rows to database for specific dates",
        description="""программа загружает строки из базы данных""",
    )
    save_weather_data_group = save_weather_data_parser.add_argument_group(title="Параметры")
    save_weather_data_group.add_argument(
        "-fd",
        "--first_date",
        action="store",
        type=str,
        help="Дата начала периода",
        metavar="YYYY-MM-DD",
    )
    save_weather_data_group.add_argument(
        "-ld",
        "--last_date",
        action="store",
        type=str,
        help="Дата окончания периода",
        metavar="YYYY-MM-DD",
    )
    save_weather_data_group.add_argument("-h", "--help", action="help", help="Справка")

    # Получение прогнозов за диапазон дат из базы
    load_weather_data_parser = subparsers.add_parser(
        "load",
        add_help=False,
        help="=> loading rows from database for specific dates",
        description="""программа загружает строки из базы данных""",
    )
    load_weather_data_group = load_weather_data_parser.add_argument_group(title="Параметры")
    load_weather_data_group.add_argument(
        "-fd",
        "--first_date",
        action="store",
        type=str,
        help="Дата начала периода",
        metavar="YYYY-MM-DD",
    )
    load_weather_data_group.add_argument(
        "-ld",
        "--last_date",
        action="store",
        type=str,
        help="Дата окончания периода",
        metavar="YYYY-MM-DD",
    )
    load_weather_data_group.add_argument("-h", "--help", action="help", help="Справка")

    # Создание открыток из полученных прогнозов
    draw_postcard_parser = subparsers.add_parser(
        "draw",
        add_help=False,
        help="=> drawing postcards with the weather for certain dates",
        description="""программа рисует открытки с погоду за выбранные даты""",
    )
    draw_postcard_group = draw_postcard_parser.add_argument_group(title="Параметры")
    draw_postcard_group.add_argument(
        "-fd",
        "--first_date",
        action="store",
        type=str,
        help="Дата начала периода",
        metavar="YYYY-MM-DD",
    )
    draw_postcard_group.add_argument(
        "-ld",
        "--last_date",
        action="store",
        type=str,
        help="Дата окончания периода",
        metavar="YYYY-MM-DD",
    )
    draw_postcard_group.add_argument("-h", "--help", action="help", help="Справка")

    # Выведение полученных прогнозов на консоль
    print_weather_parser = subparsers.add_parser(
        "print",
        add_help=False,
        help="=> print rows from database for specific dates",
        description="""программа выводит в консоль погоду за выбранные даты""",
    )
    print_weather_group = print_weather_parser.add_argument_group(title="Параметры")
    print_weather_group.add_argument(
        "-fd",
        "--first_date",
        action="store",
        type=str,
        help="Дата начала периода",
        metavar="YYYY-MM-DD",
    )
    print_weather_group.add_argument(
        "-ld",
        "--last_date",
        action="store",
        type=str,
        help="Дата окончания периода",
        metavar="YYYY-MM-DD",
    )
    print_weather_group.add_argument("-h", "--help", action="help", help="Справка")

    return arg_parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.command == "save":
        print(f"Команда = {namespace.command}")
        db_updater.save_weather_data(
            first_date=namespace.first_date, last_date=namespace.last_date
        )
        if namespace.first_date is None:
            namespace.first_date = str(datetime.datetime.now().date())
        elif namespace.last_date is None:
            namespace.last_date = namespace.first_date
        print(
            f"Данные были сохранены за период с {namespace.first_date} по {namespace.last_date}"
        )
    elif namespace.command == "load":
        print(f"Команда = {namespace.command}\n")
        print("Были получены следующие строки:")
        pprint(
            db_updater.load_weather_data(
                first_date=namespace.first_date, last_date=namespace.last_date
            )
        )
    elif namespace.command == "draw":
        print(f"Команда = {namespace.command}")
        period = db_updater.load_weather_data(
            first_date=namespace.first_date, last_date=namespace.last_date
        )
        im.postcard(weather=period)
    elif namespace.command == "print":
        print(f"Команда = {namespace.command}\n")
        period = db_updater.load_weather_data(
            first_date=namespace.first_date, last_date=namespace.last_date
        )
        for day in period:
            print(
                f'Дата: {day["date"]}\n'
                f'Погода: {day["weather"]}\n'
                f'Температура: {day["degrees"]}\n'
                f'Ветер: {day["wind"]}\n'
                f'Влажность: {day["humidity"]}\n'
                f'Давление: {day["pressure"]}\n'
            )
    else:
        print(
            "\nВы не выбрали ни одной команды. \nПо умолчанию показываю вам Погоду за последние 7 дней\n"
        )
        period = db_updater.load_weather_data(
            first_date=str(datetime.datetime.now().date() - datetime.timedelta(6)),
            last_date=str(datetime.datetime.now().date()),
        )
        for day in period:
            print(
                f'Дата: {day["date"]}\n'
                f'Погода: {day["weather"]}\n'
                f'Температура: {day["degrees"]}\n'
                f'Ветер: {day["wind"]}\n'
                f'Влажность: {day["humidity"]}\n'
                f'Давление: {day["pressure"]}\n'
            )

# ниже написал строки для тестов работоспособности консольных функций (для удобства)

# По умолчанию показывается погода за последние 7 дней
# python 01_weather.py

# Хелпы по программе в целом и по каждой функции в отдельности
# python 01_weather.py -h
# python 01_weather.py save -h
# python 01_weather.py load -h
# python 01_weather.py draw -h
# python 01_weather.py print -h

# Проверка сохранения данных в базу (если не проставлять даты по умолчанию берется сегодняшний день)
# python 01_weather.py save
# python 01_weather.py save -fd 2021-05-01
# python 01_weather.py save -fd 2021-10-01 -ld 2021-10-05

# Выгружает данные из базы (если не проставлять даты по умолчанию берется сегодняшний день)
# python 01_weather.py load
# python 01_weather.py load -fd 2021-05-01
# python 01_weather.py load -fd 2021-10-01 -ld 2021-10-05

# Рисует открытик за выбранные даты (если не проставлять даты по умолчанию берется сегодняшний день)
# python 01_weather.py draw
# python 01_weather.py draw -fd 2021-05-01
# python 01_weather.py draw -fd 2021-10-01 -ld 2021-10-05

# Печатает в консоль строка за выбранные даты (если не проставлять даты по умолчанию берется сегодняшний день)
# python 01_weather.py print
# python 01_weather.py print -fd 2021-05-01
# python 01_weather.py print -fd 2021-10-01 -ld 2021-10-05

# зачет!
