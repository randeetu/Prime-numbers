# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...

# если изначально не писать число в виде строки - теряется точность!

import json
import re
from decimal import Decimal
from cowsay import dragon, cow
from datetime import datetime
from csv import writer
from termcolor import colored

DUNGEON_FILE = 'dungeon.csv'
RPG_FILE = 'rpg.json'

REMAINING_TIME = '123456.0987654321'
FIELD_NAMES = ['current_location', 'current_experience', 'current_date']

LOCATION_INITIALIZATION = r'(Location_\w+|Hatch)_tm([\d+|\d/.]+)'
MOB_AND_BOSS_INITIALIZATION = r'(Mob|Boss(|\d+))_exp(\d+)_tm(\d+)'


class Dungeons:

    def __init__(self, csv_names, rt=REMAINING_TIME):
        self.mob_and_boss = MobAndBoss()
        self.location_class = Location()
        self.current_experience = 0
        self.elapsed_time = 0
        self.rt = Decimal(rt)
        with open(DUNGEON_FILE, 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            csv_writer.writerow(csv_names)

    @staticmethod
    def turning(locations_branching, killed_mob_and_boss, mob_and_boss):
        locations = []
        for current_location, environment_in in locations_branching.items():
            if environment_in == "You are winner":
                return 'You are winner'
            for item in environment_in:
                if isinstance(item, dict):
                    locations.append(item)
                elif isinstance(item, str):
                    if not killed_mob_and_boss:
                        mob_and_boss.append(item)
            return current_location, mob_and_boss, locations

    def current_state(self, current_location, mob_and_boss, locations):
        with open(DUNGEON_FILE, 'a', newline='', encoding='utf8') as csv_file:
            csv_writer = writer(csv_file, )
            available_actions = []
            if mob_and_boss:
                available_actions.append("Уничтожить врага")
            if locations:
                available_actions.append("Пойти в другую локацию")
            available_actions.append("Сдаться и умереть")

            csv_writer.writerow([current_location, self.current_experience, datetime.now()])
            print('*' * 70)
            print(f" Вы сейчас в {current_location} и у вас {self.current_experience} опыта. ")
            print(f"До наводнения {self.rt} секунд.")
            print(f"{self.elapsed_time} времени уже прошло.")
            showing_mob_and_boss = list(map(lambda enm: '- Враг: ' + enm, mob_and_boss))
            showing_locations = list(map(lambda loc: '- Вход в локацию: ' + list(loc.keys())[0], locations))
            print("Перед вами:")
            print(*showing_mob_and_boss, sep='\n')
            print(*showing_locations, sep='\n')
            print(f"Пришло время выбора:")
            available_actions = \
                list(map(lambda act: str(available_actions.index(act) + 1) + '.' + act, available_actions))
            print(*available_actions, sep='\n')
            return available_actions

    @staticmethod
    def pick(action_length):
        available_choices = [str(i + 1) for i in range(action_length)]
        while True:
            print('*' * 70)
            option = input('Какое действие выберете? : ')
            print('*' * 70)
            if option in available_choices:
                break
        return option

    def killing(self, mob_and_boss):
        print('Доступные для уничтожения враги:')
        attacking_mob_and_boss = []
        for i in range(len(mob_and_boss)):
            attacking_mob_and_boss.append(str(i + 1) + '.' + mob_and_boss[i])
        print(*attacking_mob_and_boss, sep='\n')
        choose = self.pick(len(mob_and_boss))
        exp, tm = self.mob_and_boss.initialize(mob_and_boss[int(choose) - 1])
        self.current_experience += exp
        self.elapsed_time += Decimal(tm)
        self.rt -= Decimal(tm)
        return choose

    def step_location(self, locations):
        print('Доступные для входа локации:')
        locations_for_action = \
            list(map(lambda x: str(locations.index(x) + 1) + '.Пройти в локацию: ' + list(x.keys())[0], locations))
        print(*locations_for_action, sep='\n')
        choose = self.pick(len(locations))

        curr_location, tm = self.location_class.initialize(locations_for_action[int(choose) - 1])
        self.rt -= Decimal(tm)
        self.elapsed_time += Decimal(tm)

        return choose

    def step_dead(self):
        self.rt = 0
        return 'dead'

    def step_impasse(self):
        self.rt = 0
        return 'impasse'

    def step_exit(self):
        self.rt = 0.0
        return 'exit'

    def kill_enemy(self, mob_and_boss_scope):
        dead_mob_and_boss = int(self.killing(mob_and_boss_scope)) - 1
        mob_and_boss_scope.remove(mob_and_boss_scope[dead_mob_and_boss])
        killed_mob_and_boss = True
        return mob_and_boss_scope, killed_mob_and_boss

    def next_location(self, locations):
        locations_branching = locations[int(self.step_location(locations)) - 1]
        killed_mob_and_boss = False
        mob_and_boss_scope = []
        return locations_branching, mob_and_boss_scope, killed_mob_and_boss

    def processing(self):
        mob_and_boss_scope = []
        killed_mob_and_boss = False
        with open(RPG_FILE, 'r', encoding='utf8') as rpg:
            locations_branching = json.load(rpg)
        while True:
            turn = self.turning(locations_branching, killed_mob_and_boss, mob_and_boss_scope)
            if turn == 'You are winner':
                if self.current_experience >= 280:
                    return turn
                else:
                    return self.step_dead()
            else:
                current_location, mob_and_boss, locations = turn
                if not locations and not mob_and_boss:
                    return self.step_impasse()
                elif not locations or self.rt <= 0:
                    mob_and_boss_scope, killed_mob_and_boss = self.kill_enemy(mob_and_boss_scope)
                else:
                    todo_choice = self.current_state(current_location, mob_and_boss, locations)
                    action = todo_choice[int(self.pick(len(todo_choice))) - 1][2:]
                    if action == 'Уничтожить врага':
                        mob_and_boss_scope, killed_mob_and_boss = self.kill_enemy(mob_and_boss_scope)
                    elif action == 'Пойти в другую локацию':
                        locations_branching, mob_and_boss_scope, killed_mob_and_boss = self.next_location(locations)
                    elif action == 'Сдаться и умереть':
                        return self.step_exit()

    def run_game(self, rt=REMAINING_TIME):
        while True:
            check = self.processing()
            if check == 'You are winner':
                print(f"Победа. В запасе осталось времени: {self.rt}")
                break
            elif check == 'exit':
                dragon(colored(f'Вы решили сдаться и принять судьбу. \nНаводнение не заставило себя ждать. '
                               f'\nАмулет треснул, вас больше ничего не спасет.\nКОНЕЦ ИГРЫ!', 'red'))
                break
            elif check == 'impasse':
                dragon(colored(f'Вы в тупике, остается принять судьбу. \nНаводнение не заставило себя ждать. '
                               f'\nАмулет треснул, вас больше ничего не спасет.\nКОНЕЦ ИГРЫ!', 'red'))
                break
            elif check == 'dead':
                reload = input(colored('Хотите продолжить игру (yes/no) : ', 'red'))
                if 'yes' == str(reload):
                    print('*' * 70)
                    print(colored('НОВАЯ ИГРА!', 'yellow'))
                    print('*' * 70)
                    self.mob_and_boss = MobAndBoss()
                    self.location_class = Location()
                    self.current_experience = 0
                    self.elapsed_time = 0
                    self.rt = Decimal(rt)
                elif 'no' == str(reload):
                    print('*' * 70)
                    cow(colored(f'Вы решили сдаться и принять судьбу. \nВам лучше быть фермером, а не героем! '
                                f'\nКОНЕЦ ИГРЫ!', 'red'))
                    break


class Location:
    @staticmethod
    def initialize(location):
        finding_location = re.findall(LOCATION_INITIALIZATION, location)
        name_location = finding_location[0][0]
        throw_time = Decimal(finding_location[0][1])
        return name_location, throw_time


class MobAndBoss:
    @staticmethod
    def initialize(mobs_and_boss):
        finding_mob_and_boss = re.findall(MOB_AND_BOSS_INITIALIZATION, mobs_and_boss)
        health = int(finding_mob_and_boss[0][2])
        kill_time = Decimal(finding_mob_and_boss[0][3])
        return health, kill_time


print('*' * 70)
print(colored('НОВАЯ ИГРА!', 'yellow'))
print('*' * 70)
dungeons = Dungeons(csv_names=FIELD_NAMES)
dungeons.run_game()

# Учитывая время и опыт, не забывайте о точности вычислений!
