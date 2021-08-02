#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def catching():
    name, email, age = line.split(' ')
    age = int(age)
    if len(line.split(' ')) == 3:
        if not name.isalpha():
            raise NotNameError()
        if '.' not in email or '@' not in email:
            raise NotEmailError()
        if 10 <= age <= 99:
            pass
        else:
            raise ValueError('поле возраст НЕ является числом от 10 до 99 в строке')
    else:
        raise ValueError()


with open('registrations.txt', 'r', encoding='utf-8') as reg_list:
    with open('registrations_good.log', 'w') as file1, open('registrations_bad.log', 'w') as file2:
        for line in reg_list:
            line = line[:-1]
            try:
                catching()
            except ValueError as exc:
                if 'not enough values to unpack' in exc.args[0]:
                    file2.write(line + '\n')
                    print(f'Не хватает данных для одного из переменных в строке || {line}')
                else:
                    file2.write(line + '\n')
                    print(f'поле возраст НЕ является числом от 10 до 99 в строке || {line}')

            except NotNameError:
                file2.write(line + '\n')
                print(f'поле имени содержит НЕ только буквы в строке || {line}')
            except NotEmailError:
                file2.write(line + '\n')
                print(f'поле email НЕ содержит @ и .(точку) в строке || {line}')
            else:
                file1.write(line + '\n')
                print(line)

# Зачёт!
