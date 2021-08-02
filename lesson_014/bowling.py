import re


class Bowling:

    def __init__(self, game_result):
        self.game_result = game_result
        self.reason_error = ''
        self.res_split = []

    def error_checking(self):
        # меняем символы '-' на '0' для дальнейшей простоты работы
        for letter in self.game_result:
            if letter == '-':
                self.game_result = self.game_result.replace(letter, '0')

        split = re.split('(X)', self.game_result)  # разделяем строку на подстроки с 'X'
        for substring in split:
            if len(substring) % 2 == 0 and substring != '':  # проверяем на корректность длинны не пустых строк
                for check in re.findall('.{%s}' % 2, substring):  # разделяем на подстроки по 2 символа
                    # проверка на отсутствие лишних символов и наличие необходимых
                    for item in set(check):
                        if item in set('/0123456789'):
                            pass
                        else:
                            self.reason_error = 'Присутствуют недопустимые символы'
                            return self.reason_error

                    # проверяем на корректность написания связки spare
                    if check[0] == '/':
                        self.reason_error = 'Связка(и) spare записаны некорректно'
                        return self.reason_error

                    # Проверяем, что каждой цифре по паре и результат не больше 10
                    if check[1] == '/':
                        pass
                    elif int(check[0]) + int(check[1]) < 10:
                        pass
                    else:
                        self.reason_error = 'Сумма очков фрейма не относящегося к strike или spare больше 9 очков'
                        return self.reason_error
                self.res_split += re.findall('.{%s}' % 2, substring)
            elif substring == 'X':
                self.res_split += 'X'

        # Проверяем, что количество фреймов равно 10
        if len(self.res_split) != 10:
            self.reason_error = 'Количество полноценных фреймов меньше или больше 10'
            return self.reason_error

    def __getter(self):
        n = 0
        for frame in self.res_split:
            if frame == 'X':
                n += 20
            elif frame[1] == '/':
                n += 15
            else:
                n += (int(frame[0]) + int(frame[1]))
        return n

    def get_score(self):
        if self.error_checking():
            print(f'Прислан ошибочный результат = {self.game_result} || {self.reason_error}')
            return self.reason_error
        else:
            n = self.__getter()
            print(f'Количество очков для результатов "{self.game_result}" = {n}')
            return n

    def get_tournament(self):
        if self.error_checking():
            return self.reason_error
        else:
            n = self.__getter()
            return n

    def get_rules(self):
        if self.error_checking():
            return self.reason_error
        else:
            n = 0
            frame_id = 0
            while frame_id < len(self.res_split):
                frame = self.res_split[frame_id]
                if frame_id == len(self.res_split) - 1:
                    if frame == 'X':
                        n += 10
                    elif frame[1] == '/':
                        n += 10
                    else:
                        n += int(frame[0]) + int(frame[1])
                elif frame_id == len(self.res_split) - 2:
                    next_frame = self.res_split[frame_id + 1]
                    if frame == 'X':
                        if next_frame == 'X':
                            n += 20
                        elif next_frame[1] == '/':
                            n += 20
                        else:
                            n += 10 + int(next_frame[0]) + int(next_frame[1])
                    elif frame[1] == '/':
                        if next_frame == 'X':
                            n += 20
                        else:
                            n += 10 + int(next_frame[0])
                    else:
                        n += int(frame[0]) + int(frame[1])

                # остальные фреймы (с первого по 8)
                else:
                    next_frame = self.res_split[frame_id + 1]
                    next_2_frame = self.res_split[frame_id + 2]
                    if frame == 'X':
                        if next_frame == 'X':
                            if next_2_frame == 'X':
                                n += 30
                            else:
                                n += 20 + int((next_2_frame[0]))
                        elif next_frame[1] == '/':
                            n += 20
                        else:
                            n += 10 + int(next_frame[0]) + int(next_frame[1])
                    elif frame[1] == '/':
                        if next_frame == 'X':
                            n += 20
                        else:
                            n += 10 + int(next_frame[0])
                    else:
                        n += int(frame[0]) + int(frame[1])

                frame_id += 1
            return n
