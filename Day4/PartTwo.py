def read_data(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


def main():
    data = read_data('input.txt')
    output = 0
    global copies_count
    copies_count = [0] * (len(data) + 1)

    for line in data:
        output += process_line(line)

    print(sum(copies_count))


def process_line(line):
    line_parts = line.split(':')
    card_id = int(line_parts[0].split()[-1])
    line = line_parts[1]

    copies_count[card_id] += 1

    line_parts = line.split('|')
    winning_numbers = [int(num) for num in line_parts[0].split()]
    numbers = [int(num) for num in line_parts[1].split()]

    exp = 0
    curr_point = 0

    for num in numbers:
        if num in winning_numbers:
            curr_point = 2 ** exp
            exp += 1

    if curr_point > 0:
        for idx in range(card_id + 1, card_id + exp + 1):
            copies_count[idx] += 1 * copies_count[card_id]

    return curr_point


main()
