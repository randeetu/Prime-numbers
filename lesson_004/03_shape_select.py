#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def all_figures(point, end_line, lines, degree, angle=0):
    for _ in range(lines):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=3)
        v.draw()
        angle += degree
        point = v.end_point
    sd.line(start_point=end_line, end_point=point, width=3)


def triangle():
    all_figures(point=sd.get_point(200, 200), end_line=sd.get_point(200, 200), lines=2, degree=120)


def square():
    all_figures(point=sd.get_point(200, 200), end_line=sd.get_point(200, 200), lines=3, degree=90)


def pentagon():
    all_figures(point=sd.get_point(200, 200), end_line=sd.get_point(200, 200), lines=4, degree=72)


def hexagon():
    all_figures(point=sd.get_point(200, 200), end_line=sd.get_point(200, 200), lines=5, degree=60)


figures = {
    1: ['triangle', triangle],
    2: ['square', square],
    3: ['pentagon', pentagon],
    4: ['hexagon', hexagon]
}

print('Возможные фигуры: ')
for number, name in figures.items():
    print(number, ':', name[0])

user_input = int(input("Введите желаемую фигуру: "))

while user_input not in figures:
    print('Такой фигуры нет')
    user_input = int(input("Введите желаемую фигуру: "))
else:
    selected_function = figures[user_input][1]
    selected_function()

sd.pause()

# зачет!
