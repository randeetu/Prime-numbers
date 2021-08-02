import simple_draw as sd


def all_figures(point, end_line, lines, degree, angle=0, length=425):
    for _ in range(lines):
        v = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v.draw()
        angle += degree
        length -= length/2.1
        point = v.end_point
    sd.line(start_point=end_line, end_point=point, width=3)


def home():
    all_figures(point=sd.get_point(600, 250), end_line=sd.get_point(600, 250), lines=2, degree=160)
    sd.rectangle(left_bottom=sd.get_point(600, 0), right_top=sd.get_point(1025, 250), color=sd.COLOR_RED, width=4)
    i_wall = 2
    for y_1 in range(0, 250, 25):
        y_2 = y_1 + 25
        if i_wall % 2 == 0:
            x = 0
        else:
            x = 25
        i_wall += 1
        for x_1 in range(600+x, 1000, 50):
            x_2 = x_1 + 50
            start_point_wall = sd.get_point(x_1, y_1)
            end_point = sd.get_point(x_2, y_2)
            sd.rectangle(left_bottom=start_point_wall, right_top=end_point, color=sd.COLOR_RED, width=4)
    sd.rectangle(left_bottom=sd.get_point(750, 100), right_top=sd.get_point(900, 200))
