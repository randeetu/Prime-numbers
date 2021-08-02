#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
# my_family = []
my_family = ['Sergey', 'Tatiana', 'Elena', 'Liliy', 'Anatoliy']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 181],
    [my_family[1], 179],
    [my_family[2], 172],
    [my_family[3], 159],
    [my_family[4], 187],
    # []
]
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

rost = str(my_family_height[0][1])
print('рост ' + my_family[0] + ' - ' + rost + ' см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

all_rost = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1]
print('Общий рост моей семьи - ', all_rost, ' см')

# зачет!
