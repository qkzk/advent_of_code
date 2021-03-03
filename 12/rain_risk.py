def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


directions = {"E": ("S", "N"),  # droite, gauche
              "S": ("W", "E"),
              "W": ("N", "S"),
              "N": ("E", "W")}


def turn(orientation, direction):
    index = 0 if direction == "R" else 1
    return directions[orientation][index]


def part_one(inputs: list) -> int:
    orientation = "E"
    x = y = 0
    for line in inputs:
        instruction, amount = line[0], int(line[1:])
        if instruction in "LR":
            nb_quart_turn = amount // 90
            for _ in range(nb_quart_turn):
                orientation = turn(orientation, instruction)
        elif instruction == "F":
            if orientation == "E":
                x += amount
            elif orientation == "W":
                x -= amount
            elif orientation == "N":
                y += amount
            else:
                y -= amount
        elif instruction == "N":
            y += amount
        elif instruction == "S":
            y -= amount
        elif instruction == "E":
            x += amount
        else:
            x -= amount
        print(line, x, y, orientation)
    return abs(x) + abs(y)


def part_two(inputs: list) -> int:
    '''178986'''
    waypoint = [10, 1]
    x = y = 0
    for line in inputs:
        instruction, amount = line[0], int(line[1:])
        if instruction == "F":
            for _ in range(amount):
                x += waypoint[0]
                y += waypoint[1]
        elif instruction == "N":
            waypoint[1] += amount
        elif instruction == "S":
            waypoint[1] -= amount
        elif instruction == "E":
            waypoint[0] += amount
        elif instruction == "W":
            waypoint[0] -= amount
        elif instruction in "LR":
            waypoint = rotate_waypoint(x, y, waypoint, instruction, amount)
        print(line, x, y, waypoint)
    return abs(x) + abs(y)


def rotate_waypoint(x, y, waypoint, orientation, amount):
    nb_quart_turn = amount // 90
    for _ in range(nb_quart_turn):
        if orientation == "L":
            waypoint = [-waypoint[1], waypoint[0]]
        if orientation == "R":
            waypoint = [waypoint[1], -waypoint[0]]
    return waypoint


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
