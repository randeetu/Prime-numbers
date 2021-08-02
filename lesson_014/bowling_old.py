class Bowling:

    def __init__(self, game_result):
        self.game_result = game_result
        self.reason_error = ''

    def error_checking(self):
        # проверка на отсутствие лишних символов и наличие необходимых
        for item in set(self.game_result):
            if item in set('X/-123456789'):
                pass
            else:
                self.reason_error = 'Присутствуют недопустимые символы'
                return self.reason_error

        # проверка, что в результате 5 фреймов или 10 бросков ('X' считается за 2 броска)
        if len(self.game_result) == 20:
            pass
        elif len(self.game_result) + self.game_result.count('X') == 20:
            pass
        else:
            self.reason_error = 'Количество полноценных фреймов меньше или больше 10'
            return self.reason_error

        # проверка на правильность написания связки spare
        if list(self.game_result).count('/'):
            check_result = list(self.game_result)
            while check_result.count('X'):
                check_result.remove('X')
            while check_result.count('/'):
                id_slash = check_result.index('/')
                if id_slash != 0 and (id_slash % 2) != 0:
                    del check_result[id_slash]
                    del check_result[id_slash - 1]
                else:
                    self.reason_error = 'Связка(и) spare записаны некорректно'
                    return self.reason_error

        # Проверка на то, что сумма каждых 2 бросков не больше 10
        if list(self.game_result) is not None:
            check_result = list(self.game_result)
            # Сначала удаляем лишние символы для проверки
            while check_result.count('X'):
                check_result.remove('X')
            while check_result.count('/'):
                del_id = check_result.index('/')
                del check_result[del_id]
                del check_result[del_id - 1]
            # Приравниваем промахи к нулю
            while check_result.count('-'):
                dah_id = check_result.index('-')
                check_result[dah_id] = '0'
            # Проверяем, что каждой цифре по паре и результат не больше 10
            while check_result:
                if (len(check_result) % 2) == 0:
                    if int(check_result[0]) + int(check_result[1]) < 10:
                        del check_result[0]
                        del check_result[0]
                    else:
                        self.reason_error = 'Сумма очков фрейма не относящегося к strike или spare больше 9 очков'
                        return self.reason_error

    def get_score(self):
        if self.error_checking():
            print(f'Прислан ошибочный результат = {self.game_result} || {self.reason_error}')
            return self.reason_error
        else:
            # Проверка на то, что внутри все числа
            if self.game_result.isdigit():
                n = 0
                for num in list(self.game_result):
                    n += int(num)
                print(f'Количество очков для результатов "{self.game_result}" - {n}')
                return n

            # Проверка на то, что внутри все буквы, а значит все X (страйки) умножаются на 20
            elif self.game_result.isalpha():
                print(f'Количество очков для результатов "{self.game_result}" - {len(self.game_result) * 20}')
                return len(self.game_result) * 20

            # Проверка на то, что внутри все промахи
            elif (len(self.game_result) * '-') == self.game_result:
                print(f'Количество очков для результатов "{self.game_result}" - 0')
                return 0

            # Проверка на все остальные результаты
            else:
                n = 0
                this_result = list(self.game_result)
                # удаляем все промахи
                if this_result.count('-'):
                    while this_result.count('-'):
                        this_result.remove('-')

                # считаем сколько страйков в результате и удаляем их из списка (для дальнейшего удобства)
                if this_result.count('X'):
                    n += this_result.count('X') * 20
                    while this_result.count('X'):
                        this_result.remove('X')

                # считаем сколько спаров в результате и удаляем их и число перед ним из списка (для дальнейшего удобства)
                if this_result.count('/'):
                    n += this_result.count('/') * 15
                    while this_result.count('/'):
                        del_id = this_result.index('/')
                        del this_result[del_id]
                        del this_result[del_id - 1]

                # суммируем остальные числа
                for num in list(this_result):
                    n += int(num)

                print(f'Количество очков для результатов "{self.game_result}" - {n}')
                return n

    def get_tournament(self):
        if self.error_checking():
            # print(f'Прислан ошибочный результат = {self.game_result} || {self.reason_error}')
            return self.reason_error
        else:
            # Проверка на то, что внутри все числа
            if self.game_result.isdigit():
                n = 0
                for num in list(self.game_result):
                    n += int(num)
                return n

            # Проверка на то, что внутри все буквы, а значит все X (страйки) умножаются на 20
            elif self.game_result.isalpha():
                return len(self.game_result) * 20

            # Проверка на то, что внутри все промахи
            elif (len(self.game_result) * '-') == self.game_result:
                return 0

            # Проверка на все остальные результаты
            else:
                n = 0
                this_result = list(self.game_result)
                # удаляем все промахи
                if this_result.count('-'):
                    while this_result.count('-'):
                        this_result.remove('-')

                # считаем сколько страйков в результате и удаляем их из списка (для дальнейшего удобства)
                if this_result.count('X'):
                    n += this_result.count('X') * 20
                    while this_result.count('X'):
                        this_result.remove('X')

                # считаем сколько спаров в результате и удаляем их и число перед ним из списка (для дальнейшего удобства)
                if this_result.count('/'):
                    n += this_result.count('/') * 15
                    while this_result.count('/'):
                        del_id = this_result.index('/')
                        del this_result[del_id]
                        del this_result[del_id - 1]

                # суммируем остальные числа
                for num in list(this_result):
                    n += int(num)

                return n

    def get_rules(self):
        if self.error_checking():
            # print(f'Прислан ошибочный результат = {self.game_result} || {self.reason_error}')
            return self.reason_error
        else:
            # Проверка на то, что внутри все числа (просто суммируем их)
            if self.game_result.isdigit():
                n = 0
                for num in list(self.game_result):
                    n += int(num)
                return n

            # Проверка на то, что внутри все буквы. Зная, что верным может быть только один
            # состоящий из 10 страйков можем сразу посчитать и вывести ответ: 30+30+30+30+30+30+30+30+20+10 = 270
            elif self.game_result.isalpha():
                return 270

            # Проверка на то, что внутри все промахи (сразу выводим ответ равный нулю)
            elif (len(self.game_result) * '-') == self.game_result:
                return 0

            # Проверка на все остальные результаты
            else:
                n = 0  # изначальные очки
                this_result = list(self.game_result)  # делаем из строки список

                # заменяем все промахи на '0'
                if this_result.count('-'):
                    while this_result.count('-'):
                        symbol_id = this_result.index('-')
                        this_result[symbol_id] = '0'

                # считаем страйки в результате и удаляем их из списка (для дальнейшего удобства)
                if this_result.count('X'):
                    while this_result.count('X'):
                        symbol_id = this_result.index('X')
                        next_1_symbol_id = this_result.index('X') + 1
                        next_2_symbol_id = this_result.index('X') + 2
                        if symbol_id <= len(this_result) - 3:

                            if this_result[next_1_symbol_id] == 'X' and this_result[next_2_symbol_id] == 'X':
                                this_result[symbol_id] = str(30)

                            elif str(this_result[next_1_symbol_id]) == '0' and str(this_result[next_2_symbol_id]) == '/':
                                this_result[symbol_id] = str(20)
                            elif this_result[next_1_symbol_id] == 'X' and str(this_result[next_2_symbol_id]) == '0':
                                this_result[symbol_id] = str(20)
                            elif str(this_result[next_1_symbol_id]) == '0' and this_result[next_2_symbol_id] == 'X':
                                this_result[symbol_id] = str(20)
                            elif str(this_result[next_1_symbol_id]) == '0' and str(this_result[next_2_symbol_id]) == '0':
                                this_result[symbol_id] = str(10)

                            elif str(this_result[next_1_symbol_id]) != '0' and str(this_result[next_2_symbol_id]) == '/':
                                this_result[symbol_id] = str(20)
                            elif this_result[next_1_symbol_id] == 'X' and str(this_result[next_2_symbol_id]) != '0':
                                this_result[symbol_id] = str(20 + int(this_result[next_2_symbol_id]))
                            elif str(this_result[next_1_symbol_id]) != '0' and this_result[next_2_symbol_id] == 'X':
                                this_result[symbol_id] = str(20 + (this_result.index('X') + 1))
                            elif str(this_result[next_1_symbol_id]) != '0' and str(this_result[next_2_symbol_id]) == '0':
                                this_result[symbol_id] = str(10 + int(this_result[next_1_symbol_id]))
                            elif str(this_result[next_1_symbol_id]) == '0' and str(this_result[next_2_symbol_id]) != '0':
                                this_result[symbol_id] = str(10 + int(this_result[next_2_symbol_id]))
                            elif str(this_result[next_1_symbol_id]) != '0' and str(this_result[next_2_symbol_id]) != '0':
                                this_result[symbol_id] = str(10 +
                                                             int(this_result[next_1_symbol_id]) +
                                                             int(this_result[next_2_symbol_id]))

                        elif symbol_id == len(this_result) - 2:

                            if this_result[next_1_symbol_id] == 'X':
                                this_result[symbol_id] = str(20)

                            elif str(this_result[next_1_symbol_id]) == '0' and str(this_result[next_2_symbol_id]) == '/':
                                this_result[symbol_id] = str(20)
                            elif str(this_result[next_1_symbol_id]) == '0' and str(this_result[next_2_symbol_id]) == '0':
                                this_result[symbol_id] = str(10 +
                                                             int(this_result[next_1_symbol_id]) +
                                                             int(this_result[next_2_symbol_id]))
                            elif int(this_result[next_1_symbol_id]) and str(this_result[next_2_symbol_id]) == '/':
                                this_result[symbol_id] = str(20)
                            elif int(this_result[next_1_symbol_id]) and int(this_result[next_2_symbol_id]):
                                this_result[symbol_id] = str(10 +
                                                             int(this_result[symbol_id + 1]) +
                                                             int(this_result[symbol_id + 2]))

                        elif symbol_id == len(this_result) - 1:
                            this_result[symbol_id] = str(10)

                # считаем сколько спаров в результате и удаляем их и число перед ним из списка
                if this_result.count('/'):
                    while this_result.count('/'):
                        symbol_id = this_result.index('/')
                        next_1_symbol_id = this_result.index('/') + 1
                        if symbol_id <= len(this_result) - 2:
                            if str(this_result[next_1_symbol_id]) == '0':
                                this_result[symbol_id] = str(10)
                                del this_result[symbol_id - 1]
                            elif str(this_result[next_1_symbol_id]) != '0' and int(this_result[next_1_symbol_id]) >= 10:
                                this_result[symbol_id] = str(20)
                                del this_result[symbol_id - 1]
                            elif str(this_result[next_1_symbol_id]) != '0' and int(this_result[next_1_symbol_id]) <= 9:
                                this_result[symbol_id] = str(10 + int(this_result[symbol_id + 1]))
                                del this_result[symbol_id - 1]
                        elif symbol_id == len(this_result) - 1:
                            this_result[symbol_id] = str(10)
                            del this_result[symbol_id - 1]

                # суммируем числа
                for num in list(this_result):
                    n += int(num)

                return n
