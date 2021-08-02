import simple_draw as sd


def creating_snow(n=None):  # создание снежинкок
    global start_point
    x_point_rnd = [sd.random_number(10, 900) for i_1 in range(n)]
    y_point_rnd = [sd.random_number(100, 700) for i_2 in range(n)]
    length_rnd = [sd.random_number(10, 30) for i_3 in range(n)]
    start_point = {}
    for i in range(len(x_point_rnd)):
        start_point[i] = {'x': x_point_rnd[i], 'y': y_point_rnd[i], 'length': length_rnd[i]}


def print_snow(color=None):  # рисование снежинки
    for i, snowflake in start_point.items():
        point_bg = sd.get_point(start_point[i]['x'], start_point[i]['y'])
        sd.snowflake(point_bg, start_point[i]['length'], color=color)


def fall():  # падение снежинки
    for i, snowflake in start_point.items():
        start_point[i]['y'] -= sd.random_number(3, 18)  # sd.random_number(10, 30)


def wind():  # ветер (колыхание по оси x)
    for i, snowflake in start_point.items():
        if start_point[i]['x'] <= 1:
            start_point[i]['x'] += 900
        if start_point[i]['x'] >= 900:
            start_point[i]['x'] -= 900
        start_point[i]['x'] += sd.random_number(-10, 10)


def fallen_snow():  # выявление снежинок достигших низа
    list_fallen_snow = []
    for i, snowflake in start_point.items():
        if start_point[i]['y'] < 10:
            list_fallen_snow.append(i)
    print(list_fallen_snow)
    return list_fallen_snow


def del_fallen_snow(del_snow=None):  # удаление снежинок достигших низа
    for n in del_snow:
        del start_point[n]


def new_snow(new=None):  # создание новых снежинок
    for n in new:
        start_point[n] = dict(x=sd.random_number(10, 900),
                              y=sd.random_number(650, 700),
                              length=sd.random_number(10, 15))


start_point = {}
