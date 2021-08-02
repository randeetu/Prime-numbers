import simple_draw as sd


def snowflake_function():
    quantity_snowflake = 35
    x_point_rnd = [sd.random_number(10, 500) for _ in range(quantity_snowflake)]
    y_point_rnd = [sd.random_number(100, 500) for _ in range(quantity_snowflake)]
    length_rnd = [sd.random_number(10, 30) for _ in range(quantity_snowflake)]
    start_point = {}
    for i in range(len(x_point_rnd)):
        start_point[i] = {'x': x_point_rnd[i], 'y': y_point_rnd[i], 'length': length_rnd[i]}
    while True:
        sd.start_drawing()
        for i_snowflake_function, snowflake in start_point.items():
            if snowflake['y'] < 50:
                snowflake['y'] += 484
            point_bg = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point_bg, snowflake['length'], color=sd.background_color)
            snowflake['y'] -= sd.random_number(10, 30)
            if snowflake['x'] <= 1:
                snowflake['x'] += 500
            if snowflake['x'] >= 500:
                snowflake['x'] -= 500
            snowflake['x'] += sd.random_number(-10, 10)
            point_white = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point_white, snowflake['length'], color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(0.05)
        if sd.user_want_exit():
            break
