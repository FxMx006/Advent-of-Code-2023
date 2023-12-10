def ways_to_win(time, distance):
    ways = 0
    for i in range(time):
        if (time - i) * i > distance:
            ways += 1
    return ways


with open('Input.txt', 'r') as f:
    lines = f.readlines()

times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))

total_ways = 1
for t, d in zip(times, distances):
    total_ways *= ways_to_win(t, d)

print(total_ways)
