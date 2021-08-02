#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

for _ in range(10):
    x = sd.random_number(50, 600)
    y = sd.random_number(50, 600)
    point = sd.get_point(x, y)
    radius = 50
    sd.circle(center_position=point, radius=radius)
    x1, y1, x2, y2 = x-0, y+15, x-20, y+15
    for _ in range(2):
        start_point = sd.get_point(x1, y1)
        end_point = sd.get_point(x2, y2)
        sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_RED, width=4)
        x1 += 30
        x2 += 30
        x3, y3, x4, y4 = x-20, y-20, x+20, y-20
        for _ in range(1):
            start_point = sd.get_point(x3, y3)
            end_point = sd.get_point(x4, y4)
            sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_RED, width=4)
sd.pause()

# зачет!
