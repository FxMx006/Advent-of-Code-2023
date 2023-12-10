def ways_to_win(time, distance):
    ways = 0
    for i in range(time):
        if (time - i) * i > distance:
            ways += 1
    return ways


with open('Input.txt', 'r') as f:
    lines = f.readlines()

time = int(''.join(lines[0].split()[1:]))
distance = int(''.join(lines[1].split()[1:]))

total_ways = ways_to_win(time, distance)

print(total_ways)
