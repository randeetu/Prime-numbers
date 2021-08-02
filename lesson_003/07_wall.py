#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# (цикл for)
import simple_draw as sd

sd.resolution = (600, 400)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x_1, y_1, x_2, y_2 = 0, 0, 100, 50
i = 2
for y_1 in range(0, 300, 50):
    y_2 = y_1 + 50
    if i % 2 == 0:
        x = 0
    else:
        x = 50
    i += 1
    for x_1 in range(0+x, 301, 100):
        x_2 = x_1 + 100
        start_point = sd.get_point(x_1, y_1)
        end_point = sd.get_point(x_2, y_2)
        sd.rectangle(left_bottom=start_point, right_top=end_point, color=sd.COLOR_RED, width=4)
sd.pause()

# зачет!
