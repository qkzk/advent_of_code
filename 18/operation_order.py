from collections import deque


def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def parse_line(line):
    return deque(list(line.replace(" ", "")))


def evaluate(tokens, add_preced=False):
    accumulator = 0
    multiplier = 1
    op = int.__add__
    while tokens:
        tok = tokens.popleft()
        if tok.isdigit():
            val = int(tok) * multiplier
            accumulator = op(accumulator, val)
        elif tok == "+":
            op = int.__add__
        elif tok == "*":
            if add_preced:
                multiplier = accumulator
                accumulator = 0
            else:
                op = int.__mul__
        elif tok == "(":
            val = evaluate(tokens, add_preced=add_preced) * multiplier
            accumulator = op(accumulator, val)
        elif tok == ")":
            break
    return accumulator


def part_one(inputs: list) -> int:
    vals = [evaluate(parse_line(line)) for line in inputs if line]
    print(vals)
    return sum(vals)


def part_two(inputs: list) -> int:
    vals = [evaluate(parse_line(line), add_preced=True)
            for line in inputs if line]
    print(vals)
    return sum(vals)


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
