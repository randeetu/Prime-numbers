import simple_draw as sd


def draw_branches(start_point_tree=sd.get_point(1300, 0), angle=90, length=110):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point_tree, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle_1 = angle - sd.random_number((30 - 30/100*40), (30 + 30/100*40))
    next_angle_2 = angle + sd.random_number((30 - 30/100*40), (30 + 30/100*40))
    next_length = length * (sd.random_number((75 - 75/100*20), (75 + 75/100*20)) / 100)
    draw_branches(start_point_tree=next_point, angle=next_angle_1, length=next_length)
    draw_branches(start_point_tree=next_point, angle=next_angle_2, length=next_length)
