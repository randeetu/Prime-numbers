#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for n in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(n)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self.prime_numbers = []
#         self.n = n
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     def get_prime_numbers(self):
#         self.i += 1
#         for prime in self.prime_numbers:
#             if self.i % prime == 0:
#                 return False
#         return True
#
#     def __next__(self):
#         while self.i < self.n:
#             if self.get_prime_numbers():
#                 self.prime_numbers.append(self.i)
#                 return self.i
#         else:
#             raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     primes = set()
#     for prime_num in range(2, n):
#         if all(prime_num % p > 0 for p in primes):
#             primes.add(prime_num)
#             yield prime_num
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


# 1)
def lucky_number(n):
    len_n = len(str(n)) // 2  # получаем кол-во цифр с каждой стороны
    n_1 = str(n)[0:len_n]  # получаем сами цифры в начале
    if len(str(n)) % 2 == 0:  # равное число цифр
        n_2 = str(n)[len_n:]  # получаем сами цифры в конце
    else:  # НЕ равное число цифр
        n_2 = str(n)[len_n + 1:]  # получаем сами цифры в конце
    sum_n_1 = sum(map(int, n_1))  # получить сумму 1 половины числа
    sum_n_2 = sum(map(int, n_2))  # получить сумму 2 половины числа

    if sum_n_1 == sum_n_2:
        return True
    else:
        return False


numbers = [1, 11, 12, 21, 515, 123, 321, 4444, 44344, 92083, 10000001, 10400001]
print('\nЗадание 3.1: Проверка числа на "Счастливость"')
for number in numbers:
    if number < 9 and lucky_number(number):
        print('Это цифра, она является простым числом', '// Начальное число:', number)
    elif lucky_number(number):
        print(True, '// Начальное число:', number)
    elif not lucky_number(number):
        print(False, '// Начальное число:', number)


# 2)
def palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


numbers = [1, 11, 12, 21, 515, 123, 321, 4444, 44344, 723327, 10000001, 10400001]
print('\nЗадание 3.2: Проверка числа на "Палиндромность"')
for number in numbers:
    if number < 9 and palindrom(number):
        print('Это цифра, она является простым числом', '// Начальное число:', number)
    elif palindrom(number):
        print(True, '// Начальное число:', number)
    elif not palindrom(number):
        print(False, '// Начальное число:', number)


# 3)
def full_generator(n):
    primes = set()
    for prime_num in range(2, n):
        if all(prime_num % p > 0 for p in primes):
            primes.add(prime_num)
            if prime_num < 9:
                pass
            elif lucky_number(prime_num) and palindrom(prime_num):
                yield prime_num
            else:
                pass


print('\nЗадание 3.3: Проверка числа на "Счастливость" и "Палиндромность"')
for number in full_generator(n=10000):
    print(number, ' - Это простое число, одновременно является и палиндромом и счастливым числом')

# Зачёт!
