#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import simple_draw as sd

sd.resolution = (1200, 900)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 10
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
sd.sleep(2)
sd.clear_screen()


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point_1, step, color):
    r_1 = 10
    for _ in range(3):
        r_1 += step
        sd.circle(center_position=point_1, radius=r_1, width=2, color=color)


point = sd.get_point(200, 100)
bubble(point_1=point, step=10, color=sd.random_color())
sd.sleep(2)
sd.clear_screen()
# Нарисовать 10 пузырьков в ряд
for x in range(100, 510, 50):
    point = sd.get_point(x, 200)
    bubble(point_1=point, step=5, color=sd.random_color())
sd.sleep(2)
sd.clear_screen()


# Нарисовать три ряда по 10 пузырьков
for y in range(500, 900, 60):
    for x in range(100, 510, 50):
        point = sd.get_point(x, y)
        bubble(point_1=point, step=5, color=sd.random_color())
sd.sleep(2)
sd.clear_screen()


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point_1=point, step=5, color=sd.random_color())
sd.sleep(2)

sd.pause()

# зачет!
