#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import simple_draw as sd

sd.resolution = (1200, 900)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle_1 = angle - sd.random_number((30 - 30/100*40), (30 + 30/100*40))
    next_angle_2 = angle + sd.random_number((30 - 30/100*40), (30 + 30/100*40))
    next_length = length * (sd.random_number((75 - 75/100*20), (75 + 75/100*20)) / 100)
    draw_branches(start_point=next_point, angle=next_angle_1, length=next_length)
    draw_branches(start_point=next_point, angle=next_angle_2, length=next_length)


root_point = sd.get_point(600, 30)
draw_branches(start_point=root_point, angle=90, length=200)

sd.pause()

# зачет!
