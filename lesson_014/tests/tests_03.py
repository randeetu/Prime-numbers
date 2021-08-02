from unittest import TestCase
from bowling import Bowling


class GetScoreErrors(TestCase):
    errors = [
        'Присутствуют недопустимые символы',
        'Количество полноценных фреймов меньше или больше 10',
        'Связка(и) spare записаны некорректно',
        'Сумма очков фрейма не относящегося к strike или spare больше 9 очков',
    ]

    # Проверяем ошибочный ввод
    def test_error_01_less_than_10_frames(self):
        bowling = Bowling('1111111111111111111')
        result = bowling.get_rules()
        self.assertIn(result, self.errors)

    def test_error_02_more_than_10_frames(self):
        bowling = Bowling('111111111111111111111')
        result = bowling.get_rules()
        self.assertIn(result, self.errors)

    def test_error_03_symbol(self):
        bowling = Bowling('STRIKE-1/spare-3')
        result = bowling.get_rules()
        self.assertIn(result, self.errors)

    def test_error_04_slash(self):
        bowling = Bowling('222222////222222////')
        result = bowling.get_rules()
        self.assertIn(result, self.errors)

    def test_error_05_sum_couple(self):
        bowling = Bowling('12357948751235794875')
        result = bowling.get_rules()
        self.assertIn(result, self.errors)

    # Проверяем разные позиции и связки 'X"
    def test_06_X(self):
        bowling = Bowling('--------------X----')
        result = bowling.get_rules()
        result_true = 10
        self.assertEqual(result, result_true)

    def test_07_X_end(self):
        bowling = Bowling('------------------X')
        result = bowling.get_rules()
        result_true = 10
        self.assertEqual(result, result_true)

    def test_08_sum_XX(self):
        bowling = Bowling('------------XX----')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_09_sum_XX_end(self):
        bowling = Bowling('----------------XX')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_10_sum_XXX(self):
        bowling = Bowling('----------XXX----')
        result = bowling.get_rules()
        result_true = 60
        self.assertEqual(result, result_true)

    def test_11_sum_XXX_end(self):
        bowling = Bowling('--------------XXX')
        result = bowling.get_rules()
        result_true = 60
        self.assertEqual(result, result_true)

    # Проверяем все связки 'X" и int > 0
    def test_12_sum_X_int_int(self):
        bowling = Bowling('------------X25----')
        result = bowling.get_rules()
        result_true = 24
        self.assertEqual(result, result_true)

    def test_13_sum_X_int_int_end(self):
        bowling = Bowling('----------------X25')
        result = bowling.get_rules()
        result_true = 24
        self.assertEqual(result, result_true)

    def test_14_sum_int_int_X(self):
        bowling = Bowling('------------25X----')
        result = bowling.get_rules()
        result_true = 17
        self.assertEqual(result, result_true)

    def test_15_sum_int_int_X_end(self):
        bowling = Bowling('----------------25X')
        result = bowling.get_rules()
        result_true = 17
        self.assertEqual(result, result_true)

    def test_16_sum_int_int_X_int_int(self):
        bowling = Bowling('------------25X25--')
        result = bowling.get_rules()
        result_true = 31
        self.assertEqual(result, result_true)

    def test_17_sum_int_int_X_int_int_end(self):
        bowling = Bowling('--------------25X25')
        result = bowling.get_rules()
        result_true = 31
        self.assertEqual(result, result_true)

    # Проверяем все связки 'X" и int spare
    def test_18_sum_X_int_slash(self):
        bowling = Bowling('------------X2/----')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_19_sum_X_int_slash_end(self):
        bowling = Bowling('----------------X2/')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_20_sum_X_and_double_int_slash(self):
        bowling = Bowling('------------X2/6/--')
        result = bowling.get_rules()
        result_true = 46
        self.assertEqual(result, result_true)

    def test_21_sum_X_and_double_int_slash_end(self):
        bowling = Bowling('--------------X2/6/')
        result = bowling.get_rules()
        result_true = 46
        self.assertEqual(result, result_true)

    def test_22_sum_int_slash_X(self):
        bowling = Bowling('------------2/X----')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_23_sum_int_slash_X_end(self):
        bowling = Bowling('----------------2/X')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_24_sum_double_int_slash_and_X(self):
        bowling = Bowling('------------2/6/X--')
        result = bowling.get_rules()
        result_true = 46
        self.assertEqual(result, result_true)

    def test_25_sum_double_int_slash_and_X_end(self):
        bowling = Bowling('--------------2/6/X')
        result = bowling.get_rules()
        result_true = 46
        self.assertEqual(result, result_true)

    # Проверяем все связки 'X" и '0' spare
    def test_26_sum_X_zero_slash(self):
        bowling = Bowling('------------X-/----')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_27_sum_X_zero_slash_end(self):
        bowling = Bowling('----------------X-/')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_28_sum_X_and_double_zero_slash(self):
        bowling = Bowling('------------X-/-/--')
        result = bowling.get_rules()
        result_true = 40
        self.assertEqual(result, result_true)

    def test_29_sum_X_and_double_zero_slash_end(self):
        bowling = Bowling('--------------X-/-/')
        result = bowling.get_rules()
        result_true = 40
        self.assertEqual(result, result_true)

    def test_30_sum_zero_slash_X(self):
        bowling = Bowling('-------------/X----')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_31_sum_zero_slash_X_end(self):
        bowling = Bowling('-----------------/X')
        result = bowling.get_rules()
        result_true = 30
        self.assertEqual(result, result_true)

    def test_32_sum_double_zero_slash_and_X(self):
        bowling = Bowling('-------------/-/X--')
        result = bowling.get_rules()
        result_true = 40
        self.assertEqual(result, result_true)

    def test_33_sum_double_zero_slash_and_X_end(self):
        bowling = Bowling('---------------/-/X')
        result = bowling.get_rules()
        result_true = 40
        self.assertEqual(result, result_true)

    # тесты на рандомную запись
    def test_random_1(self):
        bowling = Bowling('811/X--3/XX171/43')
        result = bowling.get_rules()
        result_true = 127
        self.assertEqual(result, result_true)

    def test_random_2(self):
        bowling = Bowling('X3-7211--X2/9/X6/')
        result = bowling.get_rules()
        result_true = 116
        self.assertEqual(result, result_true)
