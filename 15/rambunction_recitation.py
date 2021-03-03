import time


def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def part_one(inputs: list) -> int:
    begin = list(map(int, inputs[0].split(",")))
    begin.reverse()
    numbers = begin.copy()
    last = numbers[0]
    while len(numbers) < 2020:
        if last in numbers[1:]:
            last = numbers[1:].index(last) + 1
            numbers.insert(0, last)
        else:
            last = 0
            numbers.insert(0, 0)
    return numbers[0]


def part_two(inputs: list) -> int:
    begin = list(map(int, inputs[0].split(",")))
    begin.reverse()
    numbers = begin.copy()
    last = numbers[0]
    while len(numbers) < 30_000_000:
        if last in numbers[1:]:
            last = numbers[1:].index(last) + 1
            numbers.insert(0, last)
        else:
            last = 0
            numbers.insert(0, 0)
        if len(numbers) % 1_000_000 == 0:
            print(len(numbers) // 1_000_000)
            print(time.time())
    return numbers[0]


def better_part_two(inputs) -> int:
    begin = list(map(int, inputs[0].split(",")))
    positions = {value: index + 1 for index, value in enumerate(begin)}
    counter = len(begin)
    courant = 0
    new = False
    while counter < 30_000_000 - 1:
        counter += 1
        if new:
            suivant = 0
        else:
            suivant = counter - positions[courant]

        positions[courant] = counter
        try:
            positions[suivant]
            new = False
        except:
            new = True
        courant = suivant

    return courant


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    # print(part_two(inputs))
    print(better_part_two(inputs))


if __name__ == "__main__":
    main()
