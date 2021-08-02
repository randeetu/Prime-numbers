#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x_1, y_1, x_2, y_2 = 50, 50, 350, 450
for color_1 in rainbow_colors:
    start_point = sd.get_point(x_1, y_1)
    end_point = sd.get_point(x_2, y_2)
    sd.line(start_point=start_point, end_point=end_point, color=color_1, width=4)
    x_1 += 5
    x_2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
def bubble(point_1, step):
    r_1 = 500
    for color in rainbow_colors:
        r_1 += step
        sd.circle(center_position=point_1, radius=r_1, width=20, color=color)


point = sd.get_point(700, -250)
bubble(point_1=point, step=22)

sd.pause()

# зачет!
