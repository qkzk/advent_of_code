def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

def parse_line(line):
    elems = line.split(" ")
    elems[1] = int(elems[1])
    return elems

def process_instructions(instructions):
    accumulator = 0
    visited = []
    next_line = 0
    while next_line not in visited:
        visited.append(next_line)
        instruction, value = instructions[next_line]
        if instruction == "nop":
            next_line +=1
        elif instruction == "acc":
            accumulator += value
            next_line += 1
        else:
            next_line += value
    return accumulator

def process_instructions_terminate(instructions):
    accumulator = 0
    visited = []
    next_line = 0
    while next_line < len(instructions):
        visited.append(next_line)
        instruction, value = instructions[next_line]
        # print(instruction, value)
        if instruction == "nop":
            next_line +=1
        elif instruction == "acc":
            accumulator += value
            next_line += 1
        else:
            next_line += value
        if next_line in visited:
            return False, 0
    return True, accumulator

def part_one(inputs: list) -> int:
    '''Run your copy of the boot code. Immediately before any instruction is
    executed a second time, what value is in the accumulator?'''
    instructions = [parse_line(line) for line in inputs]
    return process_instructions(instructions)


def part_two(inputs: list) -> int:
    instructions = [parse_line(line) for line in inputs]
    for line_nb in range(len(instructions)):
        instruction, value = instructions[line_nb]
        if instruction == "acc":
            continue
        if instruction == "nop":
            instructions[line_nb] = ("jmp", value)
        else:
            instructions[line_nb] = ("nop", value)

        finished, final = process_instructions_terminate(instructions)
        if finished:
            return final
        instructions[line_nb] = (instruction, value)
    return None



def main():
    # inputs: list = read_file("./example.txt")
    # inputs: list = read_file("./example_corrected.txt")
    inputs: list = read_file("./input.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
