from collections import deque
from itertools import product

def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

def readlines(inputs):
    return list(map(int, inputs))

def valid_sums(values):
    return {a + b for a, b in product(values, repeat=2)}

def part_one(inputs: list) -> int:
    '''find the first number in the list (after the preamble) which is not the
    sum of two of the 25 numbers before it. What is the first number that does
    not have this property?'''
    integers = readlines(inputs)
    queue = deque(integers[:25])
    for value in integers[25:]:
        vs = valid_sums(queue)
        if value not in vs:
            return value
        queue.popleft()
        queue.append(value)
    return -1


def part_two(inputs: list) -> int:
    # goal = 127
    goal = 138879426
    integers = readlines(inputs)

    for i, x in enumerate(integers[:-1]):
        for j, y in enumerate(integers[i + 1:]):
            s = sum(integers[i:j+1])
            if s == goal:
                return min(integers[i:j+1]) + max(integers[i:j+1])
            elif s > goal:
                break
    return -1



def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
