def read_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


class CategoryMap:
    def __init__(self, category_name, next_category, map_tuples):
        self.category_name = category_name
        self.next_category = next_category
        self.map_tuples = map_tuples

    def apply(self, value):
        for to_idx, from_idx, length in self.map_tuples:
            if from_idx <= value < from_idx + length:
                return to_idx + (value - from_idx)
        return value


def parse_lines(lines):
    line_iterator = iter(lines)
    seeds = [int(n) for n in next(line_iterator).replace("seeds: ", "").split(" ")]

    category_maps = {}

    while True:
        try:
            line = next(line_iterator)
        except StopIteration:
            break

        if "map" in line:
            from_category, to_category = line.replace(" map:", "").split("-to-")
            map_tuples = []

            while True:
                try:
                    line = next(line_iterator)
                except StopIteration:
                    break

                if line == "":
                    break

                to_idx, from_idx, length = line.split(" ")
                map_tuples.append((int(to_idx), int(from_idx), int(length)))

            category_map = CategoryMap(from_category, to_category, map_tuples)
            category_maps[from_category] = category_map

    return seeds, category_maps


def apply_category_map_to_range(category_map, value_range):
    all_starts = [from_idx for _, from_idx, _ in category_map.map_tuples]
    all_ends = [from_idx + length for _, from_idx, length in category_map.map_tuples]
    all_s_and_t = sorted(set(all_starts + all_ends))

    split_ranges = []
    next_start = value_range[0]
    for v in all_s_and_t:
        if v <= value_range[0] or v >= value_range[1]:
            continue

        split_ranges.append((next_start, v))
        next_start = v
    split_ranges.append((next_start, value_range[1]))

    new_ranges = []
    for s, t in split_ranges:
        new_start = category_map.apply(s)
        new_end = new_start + (t - s)
        new_ranges.append((new_start, new_end))

    return new_ranges


def solve(lines):
    seed_data, category_maps = parse_lines(lines)

    seed_intervals = []
    for i in range(len(seed_data) // 2):
        s = seed_data[2 * i]
        length = seed_data[2 * i + 1]
        seed_intervals.append((s, s + length))

    location_intervals = get_location_from_seed_intervals(seed_intervals, category_maps)
    closest_location = min([i[0] for i in location_intervals])
    return closest_location


def get_location_from_seed_intervals(seed_intervals, category_maps):
    category = "seed"
    intervals = seed_intervals
    while category != "location":
        category_map = category_maps[category]
        all_new_intervals = []
        for interval in intervals:
            new_intervals = apply_category_map_to_range(category_map, interval)
            all_new_intervals.extend(new_intervals)

        intervals = all_new_intervals
        category = category_map.next_category

    return intervals


def main():
    lines = read_input()
    solution = solve(lines)
    print("solution =", solution)


if __name__ == "__main__":
    main()
