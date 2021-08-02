#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
except ValueError as exc:
    print(f'Невозможно преобразовать к числу, ошибка: {exc}')
except IndexError as exc:
    print(f'Выход за границы списка, ошибка: {exc}')
except Exception as exc:
    print(f'Неожиданная ошибка: {exc}')
else:
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

# Зачёт!
