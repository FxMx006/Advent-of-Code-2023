

def input_parser(input_data):
    lines = []
    for line in input_data.splitlines():
        lines.append(tuple(map(int, line.split())))
    return lines


def part1(input_data, invert=False):
    diff_multiplier = 1 if invert else -1
    prediction_value_index = 0 if invert else -1
    prediction_sum = 0
    for line in input_data:
        last_sequence = line
        prediction_values = [line[prediction_value_index]]
        while True:
            diff_sequence = []
            for i in range(len(last_sequence) - 1):
                diff_sequence.append((last_sequence[i] - last_sequence[i + 1]) * diff_multiplier)
            if all(i == 0 for i in diff_sequence):
                break
            last_sequence = diff_sequence
            prediction_values.append(diff_sequence[prediction_value_index])
        prediction_sum += sum(prediction_values)
    return prediction_sum


with open('Input.txt', 'r') as file:
    input_data = file.read()


parsed_data = input_parser(input_data)
print(part1(parsed_data))
