def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()




def part_one(inputs: list) -> int:
    '''somme des longueurs des sets des lettres de chaque groupe'''
    letters = set()
    counts = []
    for line in inputs:
        if not line.strip():
            count = len(letters)
            counts.append(count)
            letters = set()
        else:
            letters = letters.union(set(line))

    count = len(letters)
    counts.append(count)
    return sum(counts)


def part_two(inputs: list) -> int:
    letters = set()
    counts = []
    new = True
    for line in inputs:
        if not line.strip():
            count = len(letters)
            counts.append(count)
            letters = set()
            new = True
        else:
            if new:
                new = False
                letters = set(line)
            else:
                letters.intersection_update(set(line))

    count = len(letters)
    counts.append(count)
    return sum(counts)



def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
