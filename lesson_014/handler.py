from bowling import Bowling


class Handler:

    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out

    def handler(self, mode):
        with open(self.file_in, 'r', encoding='UTF-8') as file_in:
            with open(self.file_out, 'w', encoding='UTF-8') as file_out:
                for line in file_in:
                    if '### Tour' in line:
                        name_winner = ''
                        game_result_winner = 0
                        tour = line.replace("\n", "")
                        file_out.write(tour + '\n')
                        print(tour)
                    elif 'winner is' in line:
                        file_out.write(f'winner is {name_winner}' + '\n')
                        print(f'winner is {name_winner}')
                    elif '\n' == line:
                        file_out.write('\n')
                        print('')
                    else:
                        name, game_result = line.split()
                        bowling = Bowling(game_result)
                        if mode == 'tournament':
                            points = bowling.get_tournament()
                        elif mode == 'rules':
                            points = bowling.get_rules()
                        if points == str(points):
                            file_out.write(f'{name} {game_result} ДИСКВАЛИФИКАЦИЯ {points} \n')
                            print(name, game_result, 'ДИСКВАЛИФИКАЦИЯ', points)
                        elif game_result_winner < points:
                            game_result_winner = points
                            name_winner = name
                            file_out.write(name + ' ' + game_result + ' ' + str(points) + '\n')
                            print(name, game_result, points)
                        else:
                            file_out.write(name + ' ' + game_result + ' ' + str(points) + '\n')
                            print(name, game_result, points)
