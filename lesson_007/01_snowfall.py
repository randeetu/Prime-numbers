#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (600, 600)


def get_flakes(count=None):
    start_point = []
    for i in range(count):
        start_point.append(Snowflake())
    return start_point


def get_fallen_flakes():
    for i in flakes:
        if i.y_point_rnd < 10:
            flakes.remove(i)
            return len(flakes)


def append_flakes(count=None):
    if N > count:
        flakes.append(Snowflake())
        print(flakes)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x_point_rnd = sd.random_number(50, 600)
        self.y_point_rnd = sd.random_number(300, 600)
        self.length_rnd = sd.random_number(10, 30)

    def clear_previous_picture(self):  # очистить предыдущее изображение
        point_bg = sd.get_point(self.x_point_rnd, self.y_point_rnd)
        sd.snowflake(point_bg, self.length_rnd, color=sd.background_color)

    def move(self):  # движение
        if self.y_point_rnd > 5:
            self.y_point_rnd -= sd.random_number(5, 10)
        if self.x_point_rnd <= 1:
            self.x_point_rnd += 600
        if self.x_point_rnd >= 600:
            self.x_point_rnd -= 600
        self.x_point_rnd += sd.random_number(-10, 10)

    def draw(self):  # отрисовка
        point_white = sd.get_point(self.x_point_rnd, self.y_point_rnd)
        sd.snowflake(point_white, self.length_rnd, color=sd.COLOR_WHITE)

    def can_fall(self):  # достигла низа
        return self.y_point_rnd > self.length_rnd


# flake = Snowflake()
# while True:
#     sd.start_drawing()
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
N = 30
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    print(flakes)
    sd.start_drawing()
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Зачёт!
