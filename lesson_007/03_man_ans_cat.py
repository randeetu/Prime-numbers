#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 0
        self.house = None
        self.rubbish = 0

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def cat_go_to_the_house(self, house):
        self.house = house
        self.fullness += 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} МЯЯЯЯЯЯЯУУУУУ КУПИ ЕДЫ!!!!!!'.format(self.name), color='red')

    def sleep(self):
        cprint('{} МУР МЯУ как же сладко я поспал'.format(self.name), color='green')
        self.fullness -= 10

    def spoil_the_wallpaper(self):
        cprint('{} МУР МЯУ я тут обои испортил, УБЕРИСЬ!'.format(self.name), color='green')
        self.fullness -= 10
        self.house.rubbish += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер, и напоследок просил передать, что ты ужасный хозяин'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.spoil_the_wallpaper()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.mini_friend = 0

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        self.house.money = 150
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def shelter_a_cat(self):
        for cat in pets:
            cat.cat_go_to_the_house(house=my_sweet_home)
            self.mini_friend += 1

    def eat(self):
        if self.house.man_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.man_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def man_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.man_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cat_shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def cleaning(self):
        cprint('{} Убрал за котом'.format(self.name), color='green')
        self.house.rubbish -= 100
        self.fullness -= 20

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.mini_friend == 0:
            self.shelter_a_cat()
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.man_food < 10:
            self.man_shopping()
        elif self.house.cat_food < 10:
            self.cat_shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.rubbish >= 100:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.man_food = 0
        self.cat_food = 0
        self.money = 0
        self.rubbish = 0

    def __str__(self):
        return 'В доме человеческой еды осталось {}, кошачьей {}, денег осталось {}, грязи {}'.format(
            self.man_food, self.cat_food, self.money, self.rubbish)


citizens = [Man(name='Вася')]
pets = [Cat(name="Барсик")]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for pet in pets:
        pet.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for pet in pets:
        print(pet)
    print(my_sweet_home)

# Зачёт!
