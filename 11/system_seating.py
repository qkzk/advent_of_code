def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def neighbors(x, y):
    return ((x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1))


def make_array(inputs: list) -> list:
    return [list(line) for line in inputs]


def create_array(width, height):
    return [[0] * width for _ in range(height)]


def get_occupied_neighbors(seats, line, col, width, height):
    nb_occupied = 0
    for x, y in neighbors(line, col):
        if x >= 0 and x < height and y >= 0 and y < width:
            neib = seats[x][y]
            if neib == "#":
                nb_occupied += 1
    return nb_occupied


def next_step(seats, line, col, width, height) -> tuple:
    status = seats[line][col]
    if status == ".":
        return ".", False
    nb_occupied = get_occupied_neighbors(seats, line, col, width, height)
    if status == "L" and nb_occupied == 0:
        return "#", True
    if status == "#" and nb_occupied >= 4:
        return "L", True
    return status, False


def present_seats(seats):
    for line in seats:
        print("".join(line))
    print()


def part_one(inputs: list) -> int:
    '''2275'''
    seats = make_array(inputs)
    height, width = len(seats), len(seats[0])
    while True:
        next_array = create_array(width, height)
        not_stop = False
        for line in range(height):
            for col in range(width):
                next_status, changed = next_step(
                    seats, line, col, width, height)
                not_stop = not_stop or changed
                next_array[line][col] = next_status
        seats = next_array
        present_seats(seats)
        if not not_stop:
            break
    return sum(sum(1 for seat in line if seat == "#") for line in seats)


def directions():
    return (
        (-1, -1),
        (-1, -0),
        (-1, +1),
        (-0, -1),
        (-0, +1),
        (+1, -1),
        (+1, -0),
        (+1, +1),
    )


def get_occupied_direction(seats, line, col, width, height):
    nb_occupied = 0
    for dy, dx in directions():
        y, x = line, col
        while True:
            x += dx
            y += dy
            if 0 <= y < height and 0 <= x < width:
                neib = seats[y][x]
                if neib == "#":
                    nb_occupied += 1
                    break
                if neib == "L":
                    break
            else:
                break
    return nb_occupied


def next_step_directions(seats, line, col, width, height) -> tuple:
    status = seats[line][col]
    if status == ".":
        return ".", False
    nb_occupied = get_occupied_direction(seats, line, col, width, height)
    if status == "L" and nb_occupied == 0:
        return "#", True
    if status == "#" and nb_occupied >= 5:
        return "L", True
    return status, False


def part_two(inputs: list) -> int:
    '''2121'''
    seats = make_array(inputs)
    height, width = len(seats), len(seats[0])
    while True:
        next_array = create_array(width, height)
        not_stop = False
        for line in range(height):
            for col in range(width):
                next_status, changed = next_step_directions(
                    seats, line, col, width, height)
                not_stop = not_stop or changed
                next_array[line][col] = next_status
        seats = next_array
        present_seats(seats)
        if not not_stop:
            break
    return sum(sum(1 for seat in line if seat == "#") for line in seats)


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
