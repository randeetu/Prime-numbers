#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

#  здесь ваш код
from my_burger import buns, cutlets, mustard, a_pickle, tomato, mayonnaise, cheese, ketchup, onion


def double_cheesburger():
    buns()
    cutlets()
    a_pickle()
    cheese()
    mayonnaise()
    ketchup()


def mu_burger():
    buns()
    cutlets()
    a_pickle()
    cheese()
    onion()
    tomato()
    mayonnaise()
    ketchup()
    mustard()


print('Рецепт двойного чизбургера:')
double_cheesburger()
print('Рецепт моего бургера: ')
mu_burger()

# зачет!
