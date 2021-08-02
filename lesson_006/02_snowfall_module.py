#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

import snowfall as sf

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
sd.resolution = (900, 600)
N = 50  # кол-во снежинок

sf.creating_snow(n=N)  # создать_снежинки(N)
while True:
    sd.start_drawing()
    sf.print_snow(color=sd.background_color)  # нарисовать_снежинки_цветом(color=sd.background_color)
    sf.fall()  # сдвинуть_снежинки()
    sf.wind()  # ветер (колыхание по оси x)
    sf.print_snow(color=sd.COLOR_WHITE)  # нарисовать_снежинки_цветом(color)
    fallen_snowflakes = sf.fallen_snow()  # выявление снежинок достигших низа
    if fallen_snowflakes:
        sf.del_fallen_snow(del_snow=fallen_snowflakes)  # удалить_снежинки(номера)
        sf.new_snow(new=fallen_snowflakes)  # создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

# Зачёт!
