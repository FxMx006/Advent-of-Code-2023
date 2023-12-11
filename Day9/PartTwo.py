from PartTwo import input_parser, part1

def part2(input_data):
    return part1(input_data, invert=True)


with open('Input.txt', 'r') as file:
    input_data = file.read()


parsed_data = input_parser(input_data)
print(part2(parsed_data))
