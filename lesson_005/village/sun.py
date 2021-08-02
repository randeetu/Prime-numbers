import simple_draw as sd


def sun():
    x_sun, y_sun = 150, 600
    point_sun = sd.get_point(x_sun, y_sun)
    radius = 50
    sd.circle(center_position=point_sun, radius=radius, color=sd.COLOR_YELLOW, width=50)
