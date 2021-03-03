from itertools import chain

def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

def neighbors(cell):
    x, y, z = cell
    yield x - 1, y - 1, z - 1
    yield x - 1, y - 1, z
    yield x - 1, y - 1, z + 1
    yield x - 1, y, z - 1
    yield x - 1, y, z
    yield x - 1, y, z + 1
    yield x - 1, y + 1, z - 1
    yield x - 1, y + 1, z
    yield x - 1, y + 1, z + 1

    yield x, y - 1, z - 1
    yield x, y - 1, z
    yield x, y - 1, z + 1
    yield x, y, z - 1
    yield x, y, z + 1
    yield x, y + 1, z - 1
    yield x, y + 1, z
    yield x, y + 1, z + 1

    yield x + 1, y - 1, z - 1
    yield x + 1, y - 1, z
    yield x + 1, y - 1, z + 1
    yield x + 1, y, z - 1
    yield x + 1, y, z
    yield x + 1, y, z + 1
    yield x + 1, y + 1, z - 1
    yield x + 1, y + 1, z
    yield x + 1, y + 1, z + 1

def read_inputs_part_one(inputs):
    return {(x, y, 0)
            for y, line in enumerate(inputs)
            for x, cell in enumerate(line)
            if cell == "#"}

def next_state(state: set) -> set:
    newtate = set()
    recalc = state | set(chain(*map(neighbors, state)))
    for cell in recalc:
        count = sum((neigh in state) for neigh in neighbors(cell))
        if count == 3 or (count == 2 and cell in state):
            newtate.add(cell)
    return newtate

def part_one(inputs: list) -> int:
    state = read_inputs_part_one(inputs)
    for _ in range(6):
        state = next_state(state)
    return len(state)

def part_two(inputs: list) -> int:
    state = read_inputs_part_two(inputs)
    for _ in range(6):
        state = next_state_4d(state)
    return len(state)

def read_inputs_part_two(inputs):
    return {(x, y, 0, 0)
            for y, line in enumerate(inputs)
            for x, cell in enumerate(line)
            if cell == "#"}

def base_3(integer: int) -> str:
    if integer == 0:
        return '0000'
    nums = []
    while integer:
        integer, tern = divmod(integer, 3)
        nums.append(str(tern))
    terns = ''.join(reversed(nums))
    return f'{terns:0>4s}'

def translate_int_neighbors(integer: int) -> tuple:
    terns = base_3(integer)
    return tuple(int(tern) - 1 for tern in terns)

def neighbors_4d(cell):
    for integer in range(81):
        if integer != 40:
            offsets = translate_int_neighbors(integer)
            yield tuple(coord + offset
                        for coord, offset in zip(cell, offsets))


def next_state_4d(state: set) -> set:
    newtate = set()
    recalc = state | set(chain(*map(neighbors_4d, state)))
    for cell in recalc:
        count = sum((neigh in state) for neigh in neighbors_4d(cell))
        if count == 3 or (count == 2 and cell in state):
            newtate.add(cell)
    return newtate

def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
