def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

def part_one(inputs: list) -> int:
    return 0


def part_two(inputs: list) -> int:
    return 0



def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    print(part_one(inputs))
    # print(part_two(inputs))


if __name__ == "__main__":
    main()
