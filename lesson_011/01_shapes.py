#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def all_figures(point, angle, length):
        for _ in range(n):
            v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v.draw()
            angle += 360 / n
            point = v.end_point
        sd.line(start_point=point, end_point=point, width=3)

    return all_figures


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()

# Зачёт!
