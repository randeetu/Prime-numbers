import simple_draw as sd


def rainbow(point_1=sd.get_point(-100, -750), step=8):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    r_1 = 1950
    for color in rainbow_colors:
        r_1 += step
        sd.circle(center_position=point_1, radius=r_1, width=20, color=color)
