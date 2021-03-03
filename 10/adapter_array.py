def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def make_ints_sort(inputs):
    return sorted(map(int, inputs))


def part_one(inputs: list) -> int:
    '''2590'''
    integers = make_ints_sort(inputs)
    distrib = {1: 0,
               2: 0,
               3: 0}
    for i, x in enumerate(integers[:-1]):
        y = integers[i + 1]
        distrib[y - x] += 1

    return (distrib[1] + 1) * (distrib[3] + 1)


def part_two(inputs: list) -> int:
    '''
    226775649501184
    plusieurs arrangements... 
    différence de moins de 3 et pas 2-2

    1, 2, 3 => (1, 3), (1, 2, 3)
    1, 2, 4 => (1, 2), (1, 2, 4)
    1, 3, 5 => (1, 3, 5)

    Ce que je sais :
    si y'a 3 d'écart, ils sont indispensables et font 1 arrangement
    1, 2, 3, 4 => 4 arrangements (1 2 3 4) (1 3 4) (1 2 4) (1 4)
    '''
    integers = make_ints_sort(inputs)
    integers.append(integers[-1] + 3)
    counter = {0: 1}
    for integer in integers:
        counter[integer] = (counter.get(integer - 3, 0) +
                            counter.get(integer - 2, 0) +
                            counter.get(integer - 1, 0))
    return counter[integers[-1]]


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
