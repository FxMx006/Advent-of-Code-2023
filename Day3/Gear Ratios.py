def main():
    lines = read_file("Input.txt")
    ans = 0
    for i, line in enumerate(lines):
        ans += process_line(i, line, lines)
    print(ans)


def read_file(file_name):
    with open(file_name) as fin:
        data = fin.read()
        lines = data.strip().split("\n")
    return lines


def is_valid_index(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def is_symbol(i, j, lines):
    if not is_valid_index(i, j, len(lines), len(lines[0])):
        return False
    return lines[i][j] != "." and not lines[i][j].isdigit()


def process_line(i, line, lines):
    ans = 0
    j = 0
    while j < len(line):
        start = j
        num = ""
        while j < len(line) and line[j].isdigit():
            num += line[j]
            j += 1
        if num == "":
            j += 1
            continue

        num = int(num)

        if is_symbol(i, start-1, lines) or is_symbol(i, j, lines):
            ans += num
            continue
        for k in range(start-1, j+1):
            if is_symbol(i-1, k, lines) or is_symbol(i+1, k, lines):
                ans += num
                break
    return ans


if __name__ == "__main__":
    main()
