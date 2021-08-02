#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class OrderedParserMin:
    key_word = 'NOK'
    time = 'min'

    def __init__(self, file_name, out_file):  # по умолчанию события NOK и время минуты
        self.file_name = file_name
        self.out_file = out_file
        self.stat = {}
        self.readying = []

    def collect(self):  # сборщик
        with open(self.file_name, 'r', encoding='cp1251') as file:  # открываем файл и построчно проходим по нему
            for line in file:
                if self.key_word in line:
                    if self.time == 'min':
                        sample = line[1:17]
                    elif self.time == 'hour':
                        sample = line[1:14]
                    elif self.time == 'month':
                        sample = line[1:8]
                    elif self.time == 'year':
                        sample = line[1:5]
                    if sample in self.stat:
                        self.stat[sample] += 1
                    else:
                        self.stat[sample] = 1

    def write_in_file(self):
        for time, num in self.stat.items():  # пересобираем в нужном виде
            self.readying.append([time, num])
        with open(self.out_file, 'w+', encoding='cp1251') as file:
            for i in range(len(self.readying)):
                file.write('[{time}] = {num}\n'.format(time=self.readying[i][0], num=self.readying[i][1]))
                print('[{time}] = {num}\n'.format(time=self.readying[i][0], num=self.readying[i][1]))


class OrderedParserHour(OrderedParserMin):
    key_word = 'NOK'
    time = 'hour'


class OrderedParserMonth(OrderedParserMin):
    key_word = 'NOK'
    time = 'month'


class OrderedParserYear(OrderedParserMin):
    key_word = 'NOK'
    time = 'year'


meter = OrderedParserMin(file_name='events.txt', out_file='out_events.txt')  # до минут
# meter = OrderedParserHour(file_name='events.txt', out_file='out_events.txt')  # до часа
# meter = OrderedParserMonth(file_name='events.txt', out_file='out_events.txt')  # до месяца
# meter = OrderedParserYear(file_name='events.txt', out_file='out_events.txt')  # до года
meter.collect()  # собираем информацию
meter.write_in_file()  # Печатаем в файл

#  можно проверять все 4 среза
# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

# Зачёт!
