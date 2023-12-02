def main():
    lines = read_file('Input.txt')
    total = 0
    for line in lines:
        line = line.strip()
        game_id, game_data = parse_game_data(line)
        if is_game_possible(game_data):
            total += game_id
    print(total)


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def parse_game_data(line):
    game_id, game_data = line.split(': ', 1)
    game_id = int(game_id.split(' ')[1])
    game_data = game_data.split('; ')
    game_data = [parse_turn_data(turn) for turn in game_data]
    return game_id, game_data


def parse_turn_data(turn):
    cubes = turn.split(', ')
    cubes = {color: int(count) for count, color in (cube.split(' ') for cube in cubes)}
    return cubes


def is_game_possible(game_data):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    for turn in game_data:
        for color, count in turn.items():
            if count > max_cubes[color]:
                return False
    return True


main()