#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import simple_draw as sd

sd.resolution = (900, 800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 75

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


x_point_rnd = [sd.random_number(10, 1200) for i_1 in range(N)]
y_point_rnd = [sd.random_number(100, 800) for i_2 in range(N)]
length_rnd = [sd.random_number(10, 30) for i_3 in range(N)]
start_point = {}
for i in range(len(x_point_rnd)):
    start_point[i] = {'x': x_point_rnd[i], 'y': y_point_rnd[i], 'length': length_rnd[i]}


while True:
    sd.start_drawing()
    for i, snowflake in start_point.items():
        if snowflake['y'] < 50:
            snowflake['y'] += 784
        point_bg = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(point_bg, snowflake['length'], color=sd.background_color)
        snowflake['y'] -= sd.random_number(10, 30)
        if snowflake['x'] <= 1:
            snowflake['x'] += 900
        if snowflake['x'] >= 900:
            snowflake['x'] -= 900
        snowflake['x'] += sd.random_number(-10, 10)
        point_white = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(point_white, snowflake['length'], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# зачет!
