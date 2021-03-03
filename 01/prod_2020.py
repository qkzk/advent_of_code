def read_inputs():
    with open("./input.txt") as inputs:
        return inputs.readlines()


def parse_inputs(inputs):
    return list(map(int, inputs))


def find_two_sum_2020(numbers: list) -> int:
    for val_1 in numbers:
        for val_2 in numbers:
            if val_1 + val_2 == 2020:
                return val_1 * val_2
    return -1


def find_three_sum_2020(numbers: list) -> int:
    for index_1, val_1 in enumerate(numbers):
        for index_2, val_2 in enumerate(numbers[index_1:]):
            for val_3 in numbers[index_2:]:
                if val_1 + val_2 + val_3 == 2020:
                    return val_1 * val_2 * val_3
    return -1


def main():
    inputs: list = read_inputs()
    numbers: list = parse_inputs(inputs)
    print(find_two_sum_2020(numbers))
    print(find_three_sum_2020(numbers))


if __name__ == "__main__":
    main()
