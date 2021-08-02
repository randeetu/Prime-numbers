#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

#  здесь ваш код

from district.central_street.house1.room1 import folks as r1
from district.central_street.house1.room2 import folks as r2
from district.central_street.house2.room1 import folks as r3
from district.central_street.house2.room2 import folks as r4
from district.soviet_street.house1.room1 import folks as r5
from district.soviet_street.house1.room2 import folks as r6
from district.soviet_street.house2.room1 import folks as r7
from district.soviet_street.house2.room2 import folks as r8

all_people = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
print('На районе живут: ', ', '.join(all_people))

# зачет!
