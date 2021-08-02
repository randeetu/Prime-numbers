#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint, choice

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


ENLIGHTENMENT_CARMA_LEVEL = 777
my_carma = 0
day = 0


class MainException(Exception):
    pass


class IamGodError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я не бог =("


class DrunkError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я напился"


class CarCrashError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я разбил машину"


class GluttonyError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я переел"


class DepressionError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я в дипрессии"


class SuicideError(MainException):

    def __str__(self):
        return f"День: {day} || карма = {my_carma} || Я самоубился"


my_exeption = (IamGodError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError(), SuicideError())


def one_day():
    global day, my_carma
    roll_day = randint(1, 13)
    roll_good_day = randint(1, 7)
    roll_error_day = choice(my_exeption)

    if roll_day != 13:
        my_carma += roll_good_day
    else:
        print(roll_error_day)
    day += 1
    return day, my_carma


while my_carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        one_day()
    except MainException as exc:
        pass
else:
    print('_' * 53)
    print(f'День: {day} || карма = {my_carma} || Вырвались из дня сурка!!!')

# https://goo.gl/JnsDqu

# Зачёт!
