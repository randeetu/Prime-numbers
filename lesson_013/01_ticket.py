#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_, to, date, save_to=None):
    save_to = 'images/end_file.png' if save_to is None else save_to
    image = Image.open('images/ticket_template.png')

    draw = ImageDraw.Draw(image)
    font_path = os.path.join('fonts', 'ofont.ru_Rubik.ttf')
    font = ImageFont.truetype(font_path, size=14)

    draw.text((46, 124), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((46, 192), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((46, 258), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((287, 258), date, font=font, fill=ImageColor.colormap['black'])

    image.show()
    image.save(save_to)


# make_ticket(fio='Krotov', from_='Moskow', to='Samara', date='30.11.2021', save_to='end_file.png')
make_ticket(fio='Krotov', from_='Moskow', to='Samara', date='30.11.2021')

# Зачёт!
