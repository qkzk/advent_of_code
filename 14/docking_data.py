def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def read_mask(line):
    return line[7:]


def read_mem(line):
    memory = int(line.strip().split("[")[1].split("]")[0])
    print("memory", memory)
    value = int(line.split("=")[1].strip())
    print("value", value)
    return memory, value


def apply_mask(mask, value):
    bits_val = f'{value:0>36b}'
    bits_rep = "".join((b_val if b_mask == 'X' else b_mask)
                       for b_mask, b_val in zip(mask, bits_val))
    print(bits_val)
    print(mask)
    print(bits_rep, value)
    return int(bits_rep, 2)


def part_one(inputs: list) -> int:
    memory = {}
    mask = None
    for line in inputs:
        if line.startswith("mask = "):
            mask = read_mask(line)
        else:
            address, value = read_mem(line)
            memory[address] = apply_mask(mask, value)
    # print(memory)
    return sum(memory.values())


def write_memory(memory, mask, address, value):
    adresses = ['']
    mem_bits = f'{address:0>36b}'
    for b_mem, b_mask in zip(mem_bits, mask):
        if b_mask == '0':
            adresses = [add + b_mem for add in adresses]
        elif b_mask == '1':
            adresses = [add + '1' for add in adresses]
        else:
            new_adresses = []
            for i in range(len(adresses)):
                new_adresses.append(adresses[i] + '0')
                new_adresses.append(adresses[i] + '1')
            adresses = new_adresses

    adresses = [int(add, 2) for add in adresses]
    for address in adresses:
        memory[address] = value


def part_two(inputs: list) -> int:
    memory = {}
    mask = None
    for line in inputs:
        if line.startswith("mask = "):
            mask = read_mask(line)
        else:
            address, value = read_mem(line)
            write_memory(memory, mask, address, value)
    print(memory)
    return sum(memory.values())


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # inputs: list = read_file("./example2.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
