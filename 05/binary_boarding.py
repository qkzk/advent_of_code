def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

# part one


mini_row = 0
maxi_row = 127

mini_col = 0
maxi_col = 7


def seat_id(row, col):
    return 8 * row + col


def process_seat(line):
    row_infos = list(line[:7])
    col_infos = list(line[7:].strip())
    print(row_infos, col_infos)

    # rows
    mini = mini_row
    maxi = maxi_row
    for direction in row_infos:
        left = (direction == "F")
        mini, maxi = bst(mini, maxi, left)
    print(mini, maxi)
    assert mini == maxi
    row = mini

    # rows
    mini = mini_col
    maxi = maxi_col
    for direction in col_infos:
        left = (direction == "L")
        mini, maxi = bst(mini, maxi, left)
    print(mini, maxi)
    assert mini == maxi
    col = mini

    return row, col


def bst(mini, maxi, left=True):
    mid = (mini + maxi) // 2
    if left:
        return mini, mid
    return mid + 1, maxi


def find_maxi(list_row_col):
    row_maxi, col_maxi = max(list_row_col,
                             key=lambda elem: seat_id(elem[0], elem[1]))
    return seat_id(row_maxi, col_maxi)


def part_one(inputs):
    list_row_col = [process_seat(line) for line in inputs]
    print(list_row_col)
    return find_maxi(list_row_col)


def convert_seat(inputs):
    return (int(x
                .replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1'), 2)
            for x in inputs)


def better_part_one(inputs):
    seat = max(convert_seat(inputs))
    return seat


# part two
"""
It's a completely full flight, so your seat should be the only missing boarding
pass in your list. However, there's a catch: some of the seats at the very
front and back of the plane don't exist on this aircraft, so they'll be missing
from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and
-1 from yours will be in your list.
"""

"""
ecrire les arrangements possibles de F/B & L/R
faire un set et une différence
"""


def part_two(inputs):
    seats = sorted(convert_seat(inputs))
    for index, seat in enumerate(seats):
        if index == len(seats) - 1:
            break
        next_seat = seats[index + 1]
        if next_seat - seat != 1:
            return seat + 1
    return -1


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    # print(better_part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
