def main():
    lines = read_file('Input.txt')
    result = calculate_sum(lines)
    print(result)


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def calculate_sum(lines):
    total = 0
    for line in lines:
        line = line.strip()
        first_digit, last_digit = find_first_last_digit(line)
        if first_digit is not None and last_digit is not None:
            total += int(first_digit + last_digit)
    return total


def find_first_last_digit(line):
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            last_digit = char
            if first_digit is None:
                first_digit = char
    return first_digit, last_digit


if __name__ == "__main__":
    main()
