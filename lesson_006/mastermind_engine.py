from random import shuffle


def number():
    global num
    number_roll = list(range(10))
    shuffle(number_roll)
    if number_roll[0] == 0:
        num = number_roll[1:5]
    else:
        num = number_roll[:4]
    return num


def new_game():
    global count, bull, cow
    count = 0
    bull = 0
    cow = 0
    print(number())
    pass


def check(rn=None):
    global bull, cow
    bull = 0
    cow = 0
    for x in range(0, 4):
        if rn[x] == num[x]:
            bull += 1
        elif rn[x] in num:
            cow += 1
    return bull, cow


num = []
bull = 0
cow = 0
count = 0
