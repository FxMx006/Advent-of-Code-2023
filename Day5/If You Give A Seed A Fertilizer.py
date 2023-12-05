def main():
    lines = read_input()
    solution = solve(lines)
    print("solution =", solution)


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


def solve(lines):
    seeds, category_maps = parse_lines(lines)

    seed_to_location = {}
    for seed in seeds:
        category = "seed"
        value = seed
        while category != "location":
            category_map = category_maps[category]
            value = category_map.apply(value)
            category = category_map.next_category
        seed_to_location[seed] = value

    closest_location = min(seed_to_location.values())
    return closest_location


if __name__ == "__main__":
    main()
