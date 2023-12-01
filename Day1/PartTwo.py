def main():
    lines = read_file('Input.txt')
    result = calculate_sum(lines)
    print(result)


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip().split("\n")


def get_digit(s):
    digit_words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word, digit in digit_words.items():
        if s.endswith(word):
            return digit
    return None


def find_first_last_digit(line):
    first_digit = None
    last_digit = None
    s = ""
    for char in line:
        if char.isdigit():
            last_digit = char
            if first_digit is None:
                first_digit = char
        else:
            s += char
            digit = get_digit(s)
            if digit is not None:
                last_digit = digit
                if first_digit is None:
                    first_digit = digit
    return first_digit, last_digit


def calculate_sum(lines):
    total = 0
    for line in lines:
        first_digit, last_digit = find_first_last_digit(line)
        if first_digit is not None and last_digit is not None:
            total += int(first_digit + last_digit)
    return total


if __name__ == "__main__":
    main()
