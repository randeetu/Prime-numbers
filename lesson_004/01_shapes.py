#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (600, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
#
# def triangle(point, angle=0):
#     for _ in range(3):
#         v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
#         v.draw()
#         angle += 120
#         point = v.end_point
#
#
# def square(point, angle=0):
#     for _ in range(4):
#         v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
#         v.draw()
#         angle += 90
#         point = v.end_point
#
#
# def pentagon(point, angle=0):
#     for _ in range(5):
#         v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
#         v.draw()
#         angle += 72
#         point = v.end_point
#
#
# def hexagon(point, angle=0):
#     for _ in range(6):
#         v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
#         v.draw()
#         angle += 60
#         point = v.end_point
#
#
# point_0 = sd.get_point(50, 50)  # 1-я часть
# triangle(point=point_0)  # триугольник
#
# point_0 = sd.get_point(50, 250)  # 1-я часть
# square(point=point_0)  # квадрат
#
# point_0 = sd.get_point(250, 100)  # 1-я часть
# pentagon(point=point_0)  # пятиугольник
#
# point_0 = sd.get_point(300, 300)  # 1-я часть
# hexagon(point=point_0)  # шестиугольник
#
# sd.sleep(5)
# sd.clear_screen()  # очистка 1-й части

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.


def all_figures(point, end_line, lines, degree, angle=0):
    for _ in range(lines):
        v = sd.get_vector(start_point=point, angle=angle, length=120, width=3)
        v.draw()
        angle += degree
        point = v.end_point
    sd.line(start_point=end_line, end_point=point, width=3)


def triangle():
    all_figures(point=sd.get_point(50, 50), end_line=sd.get_point(50, 50), lines=2, degree=120)


def square():
    all_figures(point=sd.get_point(50, 250), end_line=sd.get_point(50, 250), lines=3, degree=90)


def pentagon():
    all_figures(point=sd.get_point(250, 50), end_line=sd.get_point(250, 50), lines=4, degree=72)


def hexagon():
    all_figures(point=sd.get_point(250, 250), end_line=sd.get_point(250, 250), lines=5, degree=60)


triangle()
square()
pentagon()
hexagon()

# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# зачет!
