from time import time
from functools import reduce


def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def part_one(inputs: list) -> int:
    '''207'''
    min_start = int(inputs[0])
    print(min_start)
    schedules = list(
        map(int, filter(lambda x: x != "x", inputs[1].split(","))))
    print(schedules)
    tables = {
        table: 0 for table in schedules
    }
    print(tables)
    for table in tables:
        value = tables[table]
        while value < min_start:
            value += table
            tables[table] = value

    print(tables)
    next_departure = min(tables, key=lambda table: tables[table])
    print(next_departure)

    return next_departure * (tables[next_departure] - min_start)


def part_two_brute_force(inputs: list) -> int:
    '''never ends...'''
    debut = time()
    freq = 2 ** 24
    schedules = {i: int(k)
                 for i, k in enumerate(inputs[1].split(",")) if k != "x"}
    print(schedules)
    departure = 0
    while True:
        if all((departure + index) % value == 0
               for index, value in schedules.items()):
            break
        departure += 1
        # if departure == 1068782:
        # print("failed")
        if departure % freq == 0:
            print(departure, time() - debut)

    return departure


def bezout_solver(a, b):
    '''résout a * u + b * v = q
    trouve le plus petit q > 0'''
    r, u, v, rp, up, vp = a, 1, 0, b, 0, 1
    while rp != 0:
        q = r // rp
        r, u, v, rp, up, vp = rp, up, vp, r - q*rp, u - q*up, v - q*vp
    return r, u, v


def inverse_modulo(n1, n2):
    '''inverse de n1 modulo n2'''
    r, _, v = bezout_solver(n1, n2)
    assert (v * n2) % n1 == r
    return v * n2


def part_two(schedules):
    '''
    530015546283687
    '''
    n = reduce(int.__mul__, schedules.values())
    schedules_mod = [(value, n // value)
                     for value in schedules.values()]
    inv_schedules = [inverse_modulo(n_chap, n)
                     for n, n_chap in schedules_mod]
    s = sum(index * inv
            for index, inv in zip(
                schedules.keys(),
                inv_schedules
            ))
    # get smallest positive solution
    if s < 0:
        while s < 0:
            s += n
    if s > n:
        while s > n:
            s -= n

    # magic trix, il faut soustraire la somme des offsets...
    # pourquoi ?
    return s - sum(schedules.keys())


def test_sols():
    for path in [
            "e1.txt",
            "e2.txt",
            "e3.txt",
            "e4.txt",
            "e5.txt",
            "e6.txt",
    ]:
        inputs = read_file(path)
        schedules = {i: int(k)
                     for i, k in enumerate(inputs[1].split(",")) if k != "x"}
        sol = int(inputs[0])
        rep = part_two(schedules)
        keys = list(schedules.keys())
        print(sol, rep, rep - sol, keys, sum(keys))


def main():
    inputs: list = read_file("./input.txt")
    schedules = {i: int(k)
                 for i, k in enumerate(inputs[1].split(",")) if k != "x"}
    return print(part_two(schedules))
    # '''
    # test_sols()


if __name__ == "__main__":
    main()
