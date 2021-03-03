def read_inputs():
    with open("./input.txt") as inputs:
        return inputs.readlines()


def example(inputs: list) -> list:
    return '''
..##.......
# ...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
# .##...#...
#...##....#
.#..#...#.#'''.strip().splitlines(keepends=False)


def part_one_count_trees(map_trees, slope=3, skip_odd=False):
    # map_trees = map_trees[1:]
    length = len(map_trees[0]) - 1  # line ends with "\n" :(
    offset = 0
    counter = 0
    for nb_line, line in enumerate(map_trees):
        if not skip_odd or nb_line % 2 == 0:
            line = line.strip()
            if line[offset] == "#":
                counter += 1
            # print(line[:offset] + ("X" if line[offset]
                # == "#" else "O") + line[1 + offset:],
                # end = "  ")
            offset = (offset + slope) % length
            # print("checked")
        # else:
            # print(line, end="  ")
            # print("not")

    return counter


def part_two_many_slopes(map_trees):
    prod = 1
    for (slope, skip_odd) in [(1, False), (3, False), (5, False), (7, False),
                              (1, True)]:
        nb = part_one_count_trees(map_trees, slope=slope, skip_odd=skip_odd)
        print(nb)
        prod *= nb
    return prod


def main():
    inputs: list = read_inputs()
    # inputs: list = example(inputs)
    # print(part_one_count_trees(inputs))
    print(part_two_many_slopes(inputs))


if __name__ == "__main__":
    main()
