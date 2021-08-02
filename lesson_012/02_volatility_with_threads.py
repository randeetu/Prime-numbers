#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
import os
from operator import itemgetter
from collections import OrderedDict
from threading import Thread


def data_file(name_folder_in=None):
    for dirpath, dirnames, filenames in os.walk(os.path.normpath(name_folder_in)):  # Добываем названия всех файлов
        for file_name in filenames:
            full_file_path = os.path.join(dirpath, file_name)  # Получаем путь до каждого файла
            tickers_path.append(full_file_path)


class TickerVolatility(Thread):

    def __init__(self, path_file, *args, **kwargs):
        super(TickerVolatility, self).__init__(*args, **kwargs)
        self.path_file = path_file  # Нормализируем путь до папки (для разных ОС)

    def run(self):
        with open(self.path_file, 'r', encoding='cp1251') as file:  # Читаем содержание файла
            next(file)  # Пропускаем строку с названиями столбцов
            line = next(file)  # Пеерходим ко второй строке
            line = line.split(',')  # Удаляем знак переноса строки и приводим к рабочему виду
            secid, tradetime, price, quantity = line  # Разбиваем на составляющие
            max_price = float(price)  # Создаем макс прайс
            min_price = float(price)  # Создаем мин прайс

            for line in file:  # построчно ищем мин и макс прайсы
                price = line.split(',')[2]  # Удаляем знак переноса строки и приводим к рабочему виду
                if float(price) > max_price:  # проверяем макс прайс
                    max_price = float(price)
                if float(price) < min_price:  # проверяем мин прайс
                    min_price = float(price)

        # После сбора максимальных и минимальных прайсов, переходим к вычислению волатильности
        half_sum = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / half_sum) * 100
        if volatility == 0:  # если нулевая
            zero_secid[secid] = 0  # сохраняем в словарь нулевых волатильностей
        else:  # если не нулевая
            not_zero_secid[secid] = round(volatility, 2)  # сохраняем в словарь не нулевых волатильностей


tickers_path = []  # список путей до файла
not_zero_secid = OrderedDict()  # словарь сделок с НЕ НУЛЕВОЙ волатильностью
zero_secid = {}  # словарь сделок с НУЛЕВОЙ волатильностью


def main():
    data_file(name_folder_in='trades')
    arranges = [TickerVolatility(path_file=file) for file in tickers_path]

    for arrange in arranges:
        arrange.start()
    for arrange in arranges:
        arrange.join()

    # Реализуем вывод нужной информации
    sort = sorted(not_zero_secid.items(), key=itemgetter(1))

    print('Максимальная волатильность: ')
    for secid_max_print in reversed(sort[-3:]):
        print(list(secid_max_print)[0], ' - ', list(secid_max_print)[1], '%')
    print('Минимальная волатильность: ')
    for secid_min_print in sort[0:3]:
        print(list(secid_min_print)[0], ' - ', list(secid_min_print)[1], '%')
    print('Нулевая волатильность: ')
    for secid_zero_print in zero_secid.items():
        print(list(secid_zero_print)[0], end=' ')


if __name__ == '__main__':
    main()

# Зачёт!
