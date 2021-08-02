import simple_draw as sd


def soon():
    x_soon, y_soon = 150, 600
    point_soon = sd.get_point(x_soon, y_soon)
    radius = 50
    sd.circle(center_position=point_soon, radius=radius, color=sd.COLOR_YELLOW, width=50)
