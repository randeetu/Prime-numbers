#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile
import collections
import operator


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class SortByQuantityBack:
    key = 1
    reverse = True

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_stat_char = collections.defaultdict(int)

    def unzip(self):  # Анзип
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        for self.filename in zip_file.namelist():
            zip_file.extract(self.filename)
        self.file_name = self.filename

    def collect(self):  # сборщик
        if self.file_name.endswith('.zip'):  # если зип то анзипаем
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:  # открываем файл и построчно считаем символы
            for line in file:
                for char in line:
                    if char.isalpha():  # и выбираем только буквы
                        self.file_stat_char[char] += 1

    def printed(self, wl=None):  # Принт в консоль форматированного вывода
        print('{txt:*^27}'.format(txt='*'))
        print('* {a_1:^10} =   {a_2:^7}  *'.format(a_1='Буква', a_2='частота'))
        print(' {txt:*^25} '.format(txt=' * '))
        if str(wl[0][0]).isdigit():  # если является числом то берем буквы со второй позиции
            for i in range(len(wl)):
                print('* {alp:^10} =   {num:7}  *'.format(alp=wl[i][1], num=wl[i][0]))
        else:  # иначе берем буквы с первой позиции
            for i in range(len(wl)):
                print('* {alp:^10} =   {num:7}  *'.format(alp=wl[i][0], num=wl[i][1]))
        print('{txt:*^27}'.format(txt='*'))
        char_sum = 0
        for alpha, numbers in self.file_stat_char.items():  # Подсчет суммы всех букв
            char_sum += numbers
        print('* {a_1:^10} =   {a_2:^7}  *'.format(a_1='ИТОГО', a_2=char_sum))
        print('{txt:*^27}'.format(txt='*'))

    def sort(self):  # по частоте по убыванию
        work_list = sorted(meter.file_stat_char.items(), key=operator.itemgetter(self.key), reverse=self.reverse)
        meter.printed(wl=work_list)


class SortByQuantityForward(SortByQuantityBack):  # по частоте по возростанию
    key = 1
    reverse = False


class SortByAlphaBack(SortByQuantityBack):  # по алфавиту
    key = 0
    reverse = False


class SortByAlphaForward(SortByQuantityBack):  # по алфавиту в обратном порядке
    key = 0
    reverse = True


meter = SortByQuantityBack(file_name='python_snippets/voyna-i-mir.txt.zip')
# meter = SortByQuantityForward(file_name='python_snippets/voyna-i-mir.txt.zip')
# meter = SortByAlphaBack(file_name='python_snippets/voyna-i-mir.txt.zip')
# meter = SortByAlphaForward(file_name='python_snippets/voyna-i-mir.txt.zip')
meter.collect()
meter.sort()

#  можно проверять все 4 сортировки
#  Попробуйте реализовать разные типы сортировки в разных классах.
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

# Зачёт!
