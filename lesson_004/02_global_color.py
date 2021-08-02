#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
# вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def all_figures(point, end_line, lines, degree, angle=0):
    for _ in range(lines):
        v = sd.get_vector(start_point=point, angle=angle, length=120, width=3)
        v.draw(color=start_color)
        angle += degree
        point = v.end_point
    sd.line(start_point=end_line, end_point=point, width=3, color=start_color)


def triangle():
    all_figures(point=sd.get_point(50, 50), end_line=sd.get_point(50, 50), lines=2, degree=120)


def square():
    all_figures(point=sd.get_point(50, 250), end_line=sd.get_point(50, 250), lines=3, degree=90)


def pentagon():
    all_figures(point=sd.get_point(250, 50), end_line=sd.get_point(250, 50), lines=4, degree=72)


def hexagon():
    all_figures(point=sd.get_point(250, 250), end_line=sd.get_point(250, 250), lines=5, degree=60)


all_colors = {
    1: ['красный', sd.COLOR_RED],
    2: ['orange', sd.COLOR_ORANGE],
    3: ['yellow', sd.COLOR_YELLOW],
    4: ['green', sd.COLOR_GREEN],
    5: ['cyan', sd.COLOR_CYAN],
    6: ['blue', sd.COLOR_BLUE],
    7: ['purple', sd.COLOR_PURPLE]
}
print('Возможные цвета: ')

for number, colors in all_colors.items():
    print(number, ':', colors[0])
user_input = int(input("Введите желаемый цвет: "))
while user_input not in all_colors:
    print('Такого цвета нет')
    user_input = int(input("Введите желаемый цвет: "))
else:
    start_color = all_colors[user_input][1]

triangle()
square()
pentagon()
hexagon()

sd.pause()

# зачет!
