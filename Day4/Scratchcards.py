def main():
    data = read_data('input.txt')
    output = 0

    for line in data:
        output += process_line(line)

    print(output)


def read_data(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


def process_line(line):
    line_parts = line.split(':')
    line = line_parts[1]

    line_parts = line.split('|')
    winning_numbers = [int(num) for num in line_parts[0].split()]
    numbers = [int(num) for num in line_parts[1].split()]

    exp = 0
    curr_point = 0

    for num in numbers:
        if num in winning_numbers:
            curr_point = 2**exp
            exp += 1
    return curr_point


main()
