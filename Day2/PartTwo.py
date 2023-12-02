def main():
    lines = read_file('Input.txt')
    total_power = 0

    for line in lines:
        line = line.strip()
        game_id, game_data = parse_game_data(line)
        min_cubes = calculate_min_cubes(game_data)
        power = calculate_power(min_cubes)
        total_power += power

    print(total_power)


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


def calculate_min_cubes(game_data):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for turn in game_data:
        for color, count in turn.items():
            min_cubes[color] = max(min_cubes[color], count)
    return min_cubes


def calculate_power(cubes):
    return cubes['red'] * cubes['green'] * cubes['blue']


main()
