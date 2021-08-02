# -*- coding: utf-8 -*-
import datetime
import re

import cv2
import peewee
import requests
from bs4 import BeautifulSoup as bs

# для парсинга
URL_SEARCH = f"https://pogoda1.ru/"
CITY = "moscow"

# регулярные выражения
RE_DEGREES = r"\[|\]|°"
RE_WIND = r"\[|\]|\n"
RE_PRESSURE_AND_HUMIDITY = r"\[|\]"

# картинки
BG_CARD = "python_snippets/external_data/probe.jpg"
SUN_CARD = "python_snippets/external_data/weather_img/sun.jpg"
RAIN_CARD = "python_snippets/external_data/weather_img/rain.jpg"
SNOW_CARD = "python_snippets/external_data/weather_img/snow.jpg"
CLOUD_CARD = "python_snippets/external_data/weather_img/cloud.jpg"

DB = peewee.SqliteDatabase("weather.db")


class ParserWeather:
    data_weather = []

    def __init__(self):
        """
        weather parsing
        """
        self.html = None

    def weather(self):  # получаем погоду
        weather_data = self.html.find_all("img", {"class": "weather-now-icon-img"})
        weather = bs(str(weather_data), features="html.parser").img["title"]
        return weather

    def degrees(self):  # получаем температуру
        degrees_data = self.html.find_all("div", {"class": "weather-now-temp"})
        degrees = bs(str(degrees_data), features="html.parser").text
        degrees = re.sub(RE_DEGREES, "", degrees)
        return degrees

    def pressure(self):  # получаем давление
        data = self.html.find_all("div", {"class": "weather-now-info"})
        pressure_data = bs(str(data[0]), features="html.parser").find_all(
            "span", {"class": "value"}
        )
        pressure = bs(str(pressure_data), features="html.parser").text
        pressure = re.sub(RE_PRESSURE_AND_HUMIDITY, "", pressure)
        return pressure

    def humidity(self):  # получаем влажность
        data = self.html.find_all("div", {"class": "weather-now-info"})
        humidity_data = bs(str(data[1]), features="html.parser").find_all(
            "span", {"class": "value"}
        )
        humidity = bs(str(humidity_data), features="html.parser").text
        humidity = re.sub(RE_PRESSURE_AND_HUMIDITY, "", humidity)
        return humidity

    def wind(self):  # получаем ветер
        wind_data = self.html.find_all("div", {"class": "weather-now-wind"})
        wind = bs(str(wind_data), features="html.parser").text
        wind = re.sub(RE_WIND, "", wind)
        return wind

    def parser_weather(self, first_date=None, last_date=None):  # парсер
        """
        weather parsing function
        :param first_date: format 'YYYY-MM-DD' (if not first_date => last_date=datetime.datetime.now().date())
        :param last_date: format 'YYYY-MM-DD' (if not last_date => last_date=first_date)
        """
        if first_date is None:
            first_date = str(datetime.datetime.now().date())
        if last_date is None:
            last_date = first_date
        first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d").date()
        last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
        while first_date <= last_date:
            response = requests.get(
                f"{URL_SEARCH}{CITY}/{last_date.day}-{last_date.month}-{last_date.year}"
            )
            if response.status_code == 200:
                self.html = bs(response.text, features="html.parser")
                self.data_weather.append(
                    {
                        "date": last_date,
                        "degrees": self.degrees(),
                        "weather": self.weather(),
                        "wind": self.wind(),
                        "humidity": self.humidity(),
                        "pressure": self.pressure(),
                    }
                )
                last_date -= datetime.timedelta(1)

            else:
                return f"Статус - {response.status_code}"
        else:
            return self.data_weather


class ImageMaker:
    def __init__(self):
        """
        draw weather postcard
        """
        self.weather = None
        self.weather_image = None

    def _color_bg(self, bg_image):  # закрашиваем bg
        height, width, i = 0, 0, 0
        for _ in range(300):
            if (
                self.weather["weather"] == "cолнечно"
                or self.weather["weather"] == "ясно"
            ):
                bg_image[:, 0 + width: 75 + width] = (50 + i / 2, 255 - i / 8, 238)
                self.weather_image = cv2.imread(SUN_CARD, cv2.IMREAD_UNCHANGED)
            elif self.weather["weather"] == "дождливо":
                bg_image[:, 0 + width: 75 + width] = (50 + i / 2, 0 + i / 6, 0)
                self.weather_image = cv2.imread(RAIN_CARD, cv2.IMREAD_UNCHANGED)
            elif self.weather["weather"] == "снег":
                bg_image[:, 0 + width: 75 + width] = (128 + i / 2, 0 + i / 2, 0)
                self.weather_image = cv2.imread(SNOW_CARD, cv2.IMREAD_UNCHANGED)
            elif (
                self.weather["weather"] == "облачно"
                or self.weather["weather"] == "пасмурно"
            ):
                bg_image[:, 0 + width: 75 + width] = (55 + i / 2, 55 + i / 2, 55 + i / 2,)
                self.weather_image = cv2.imread(CLOUD_CARD, cv2.IMREAD_UNCHANGED)
            else:
                bg_image[:, 0 + width: 75 + width] = (0 + i / 6, 50 + i / 2, 0)
                self.weather_image = cv2.imread(CLOUD_CARD, cv2.IMREAD_UNCHANGED)
            i += 2
            width += 4

    def _write_text(self, bg_image):  # пишем тексты
        y_text_position = 75
        cv2.putText(
            bg_image,
            "ПОГОДА",
            (190, 25),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (125, 0, 125),
            3,
        )
        for item in self.weather:
            cv2.putText(
                bg_image,
                item,
                (25, y_text_position),
                cv2.QT_FONT_NORMAL,
                0.65,
                (0, 0, 0),
                2,
            )
            cv2.putText(
                bg_image,
                str(self.weather[item]),
                (125, y_text_position),
                cv2.FONT_HERSHEY_COMPLEX,
                0.70,
                (0, 0, 0),
                2,
            )
            y_text_position += 30

    def _draw_weather_image(self, bg_image):  # рисуем картинку
        rows, cols, channels = self.weather_image.shape
        overlay = cv2.addWeighted(
            bg_image[15: 15 + rows, 400: 400 + cols], 0, self.weather_image, 1, 0
        )
        bg_image[15: 15 + rows, 400: 400 + cols] = overlay

    def postcard(self, weather):  # собираем картинку
        """
        weather card collection function
        :param weather: get row from database
        """
        for line in weather:
            self.weather = line
            bg_image = cv2.imread(BG_CARD)
            self._color_bg(bg_image)
            self._write_text(bg_image)
            self._draw_weather_image(bg_image)
            # cv2.imshow(BG_CARD, bg_image)  # открываем фото для просмотра
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite(f"result_{str(line['date'])}.jpg", bg_image)


class Weather(peewee.Model):
    date = peewee.DateField(unique=True)
    degrees = peewee.CharField()
    weather = peewee.CharField()
    wind = peewee.CharField()
    humidity = peewee.CharField()
    pressure = peewee.CharField()

    class Meta:
        database = DB


class DatabaseUpdater:
    def __init__(self):
        """
        needed to work with the database
        """
        self.search = None

    def load_weather_data(self, first_date=None, last_date=None):
        data = []
        if first_date is None:
            first_date = str(datetime.datetime.now().date())
        if last_date is None:
            last_date = first_date
        while first_date <= last_date:
            try:
                lines = Weather.select().where(Weather.date == first_date).get()
            except peewee.DoesNotExist:
                self.save_weather_data(first_date)
                continue
            data.append(
                {
                    "date": lines.date,
                    "degrees": lines.degrees,
                    "weather": lines.weather,
                    "wind": lines.wind,
                    "humidity": lines.humidity,
                    "pressure": lines.pressure,
                }
            )
            first_date = str(
                datetime.datetime.strptime(first_date, "%Y-%m-%d").date()
                + datetime.timedelta(1)
            )
        return data

    def save_weather_data(self, first_date=None, last_date=None):
        self.search = parser.parser_weather(first_date, last_date)
        for day in self.search:
            try:
                Weather.insert(day).execute()
            except peewee.IntegrityError:
                continue


DB.create_tables([Weather, ])

parser = ParserWeather()
image = ImageMaker()
db_updater = DatabaseUpdater()


# ниже написал строки для тестов работоспособности функций (для удобства)


# TESTS PARSE WEATHER
# парсим данные задавая начальную дату и конечную
# print(parser.parser_weather(first_date="2022-01-25", last_date="2022-01-28"))

# парсим данные задавая только начальную дату
# print(parser.parser_weather(first_date="2022-01-24"))

# парсим данные не задавая даты (должна спарситься сегодняшняя дата)
# print(parser.parser_weather())

# TESTS DRAW WEATHER_CARD
# выгружаем из базы строку (по умолчанию за сегодня) и рисуем карточку
# search = db_updater.load_weather_data("2021-07-11", "2021-07-13")
# image.postcard(weather=search)


# TESTS CREATE NEW LINE IN DATABASE
# добавляем новые строки задавая начальную дату и конечную (если есть => print что существует)
# db_updater.save_weather_data(first_date="2022-01-01", last_date="2022-01-05")

# добавляем новые строки задавая только начальную дату (если есть => print что существует)
# db_updater.save_weather_data(first_date="2022-01-06")

# добавляем новые строки не задавая даты (должна создаться сегодняшняя дата) (если есть => print что существует)
# db_updater.save_weather_data()


# TESTS LOAD LINES IN DATABASE
# выгружаем из базы строки задавая начальную дату и конечную (если их нет изначально создадуться)
# print('test = 2021-07-11 - 2021-07-13')
# print(db_updater.load_weather_data("2021-07-11", "2021-07-13"))

# выгружаем из базы строку задавая только начальную дату (если ее нет изначально создастся)
# print('test = 2022-01-08')
# print(db_updater.load_weather_data("2022-01-08"))

# выгружаем из базы строку не задавая даты (должны получить за сегодняшнюю дату) (если ее нет изначально создастся)
# print('test = за сегодня')
# print(db_updater.load_weather_data())
