import simple_draw as sd


def smile():
    x_smile, y_smile = 825, 150
    point_smile = sd.get_point(x_smile, y_smile)
    radius = 30
    sd.circle(center_position=point_smile, radius=radius, color=sd.COLOR_RED, width=4)
    x1, y1, x2, y2 = x_smile-0, y_smile+5, x_smile-10, y_smile+5
    for _ in range(2):
        start_point_smile = sd.get_point(x1, y1)
        end_point = sd.get_point(x2, y2)
        sd.line(start_point=start_point_smile, end_point=end_point, color=sd.COLOR_RED, width=4)
        x1 += 20
        x2 += 20
        x3, y3, x4, y4 = x_smile-10, y_smile-10, x_smile+10, y_smile-10
        for _ in range(1):
            start_point_smile = sd.get_point(x3, y3)
            end_point = sd.get_point(x4, y4)
            sd.line(start_point=start_point_smile, end_point=end_point, color=sd.COLOR_RED, width=4)
