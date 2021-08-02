from unittest import TestCase
from bowling import Bowling


class GetScoreErrors(TestCase):
    errors = [
        'Присутствуют недопустимые символы',
        'Количество полноценных фреймов меньше или больше 10',
        'Связка(и) spare записаны некорректно',
        'Сумма очков фрейма не относящегося к strike или spare больше 9 очков',
    ]

    def test_less_than_5_frames(self):
        bowling = Bowling('1111111111111111111')
        result = bowling.get_tournament()
        self.assertIn(result, self.errors)

    def test_more_than_5_frames(self):
        bowling = Bowling('111111111111111111111')
        result = bowling.get_tournament()
        self.assertIn(result, self.errors)

    def test_error_symbol(self):
        bowling = Bowling('STRIKE-1/spare-3')
        result = bowling.get_tournament()
        self.assertIn(result, self.errors)

    def test_error_slash(self):
        bowling = Bowling('222222////222222////')
        result = bowling.get_tournament()
        self.assertIn(result, self.errors)

    def test_error_sum_couple(self):
        bowling = Bowling('12357948751235794875')
        result = bowling.get_tournament()
        self.assertIn(result, self.errors)
