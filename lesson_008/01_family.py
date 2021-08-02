#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 100
        self.cat_food = 30
        self.money = 50
        self.rubbish = 0
        self.stat_money = 0
        self.stat_eat = 0
        self.stat_cat_eat = 0
        self.stat_fur_coat = 0
        self.stat_game = 0

    def __str__(self):
        return 'В доме человеческой еды осталось {},кошачьей еды осталось {}, денег осталось {}, грязи {}'.format(
            self.food, self.cat_food, self.money, self.rubbish)

    def mood(self):
        self.rubbish += 5  # ежедневное падение показателя чистаоты
        if self.rubbish > 90:
            serge.happy -= 10
            masha.happy -= 10

    def home_stat(self):
        cprint('================== Итоги жизни за год =================='.format(), color='red')
        cprint('Денег заработано = {}'.format(self.stat_money), color='red')
        cprint('Съедено кошачьей еды = {}'.format(self.stat_cat_eat), color='red')
        cprint('Съедено еды = {}'.format(self.stat_eat), color='red')
        cprint('Куплено шуб = {}'.format(self.stat_fur_coat), color='red')
        cprint('Сыграно игр = {}'.format(self.stat_game), color='red')


class Man:

    def __init__(self, name):
        self.home = home
        self.name = name
        self.fullness = 30
        self.happy = 100

    def __str__(self):
        return '{}: сытость = {} и степень счастья = {}'.format(self.name, self.fullness, self.happy)

    def act_human(self):
        if self.fullness <= 0 or self.happy <= 0:
            cprint('{} умер!'.format(self.name), color='red')
            return
        else:
            self.act()

    def pet_the_cat(self):
        cprint('{} погладил кота'.format(self.name), color='blue')
        self.happy += 5

    def happy_human(self):
        pass

    def act(self):
        pass


class Husband(Man):

    def act(self):
        super().act()
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.home.money < 360:
            self.work()
        elif self.happy < 30:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.gaming()

    def eat(self):
        eating = randint(10, 30)
        if self.home.food >= eating:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += eating
            self.home.food -= eating
            self.home.stat_eat += eating
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.home.money += 150
        self.home.stat_money += 150
        self.fullness -= 10

    def gaming(self):
        super().happy_human()
        cprint('{} Играл в WoT'.format(self.name), color='green')
        self.happy += 20
        self.fullness -= 10
        self.home.stat_game += 1


class Wife(Man):

    def act(self):
        super().act()
        dice = randint(1, 6)
        if self.fullness <= 40:
            self.eat()
        elif self.home.food <= 30 or self.home.cat_food <= 10:
            self.shopping()
        elif self.home.rubbish >= 70:
            self.clean_house()
        elif self.happy <= 30:
            self.buy_fur_coat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.pet_the_cat()
        else:
            self.buy_fur_coat()

    def eat(self):
        eating = randint(10, 30)
        if self.home.food >= eating:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += eating
            self.home.food -= eating
            self.home.stat_eat += eating
        else:
            self.shopping()

    def shopping(self):
        if self.home.money >= 400:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.home.food += (self.home.money - 360)
            self.home.cat_food += 10
            self.home.money -= (self.home.money - 350)
            self.fullness -= 10
        elif self.home.money >= 80:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.home.food += 70
            self.home.cat_food += 10
            self.home.money -= 80
            self.fullness -= 10
        elif self.home.money > 1:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.home.food += self.home.money
            self.home.money = 0
            self.fullness -= 10
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
            self.fullness -= 10

    def buy_fur_coat(self):
        super().happy_human()
        if self.home.money >= 350:
            cprint('{} сходила в магазин за шубой!'.format(self.name), color='green')
            self.home.money -= 350
            self.happy += 60
            self.home.stat_fur_coat += 1
            self.fullness -= 10
        else:
            cprint('{} не хватило на покупку шубы, сидела и заедала горе!'.format(self.name), color='red')
            self.fullness -= 10

    def clean_house(self):
        if self.home.rubbish >= 90:
            cprint('{} Убрала дом, ну и бардак же развели'.format(self.name), color='red')
            self.home.rubbish -= randint(80, 100)
            self.fullness -= 10
        else:
            cprint('{} Убрала дом, лучше больше такого не допускать'.format(self.name), color='yellow')
            self.home.rubbish = 0
            self.fullness -= 10


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act_human()
#     masha.act_human()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
#     home.mood()  # ежедневное падение показателя чистаоты
# home.home_stat()  # Статистика по итогу прожитого периода

# Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.home = home
        self.name = name
        self.fullness = 30

    def __str__(self):
        return '{}: сытость = {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер!'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 40:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.home.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            dice = randint(1, 10)
            if dice:
                self.fullness += (dice * 2)
                self.home.cat_food -= dice
                self.home.stat_cat_eat += dice
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спал'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        cprint('{} драл обои'.format(self.name), color='yellow')
        self.home.rubbish += 5
        self.fullness -= 10


# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __str__(self):
        super().__str__()
        return '{}: сытость = {} и неизменное счастье = {}'.format(self.name, self.fullness, self.happy)

    def act(self):
        super().act()
        dice = randint(1, 6)
        if self.fullness <= 30:
            self.eat()
        elif dice == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.home.food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.home.food -= 10
            self.home.stat_eat += 10
        elif self.home.food > 0:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += self.home.food
            self.home.stat_eat += self.home.food
            self.home.food -= self.home.food
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} Весь день спал'.format(self.name), color='green')
        self.fullness -= 10


# Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act_human()
    masha.act_human()
    kolya.act_human()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')
    home.mood()  # ежедневное падение показателя чистаоты
home.home_stat()  # Статистика по итогу прожитого периода

# Зачёт!
