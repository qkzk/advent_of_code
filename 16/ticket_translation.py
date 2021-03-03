from functools import reduce


def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()


def read_fields(inputs):
    line_nb = 0
    line = inputs[0]
    fields = []
    while line != "":
        numbers = line.split(":")[1]
        fields_values = numbers.split(" or ")
        values_min = [field.split("-")[0] for field in fields_values]
        values_max = [field.split("-")[1] for field in fields_values]
        values_min = list(map(int, values_min))
        values_max = list(map(int, values_max))
        fields.append([(vmin, vmax)
                       for vmin, vmax in zip(values_min, values_max)])
        line_nb += 1
        line = inputs[line_nb]
    return fields


def read_values(inputs):
    line_nb = 0
    while inputs[line_nb] != "nearby tickets:":
        line_nb += 1
    line_nb += 1
    return [
        list(map(int, line.split(","))) for line in inputs[line_nb:]
    ]


def invalid_fields_sum(tickets, fields):
    total = 0
    nb_invalid = 0
    for ticket in tickets:
        for value in ticket:
            if not any(min_val <= value <= max_val
                       for field in fields
                       for (min_val, max_val) in field):
                total += value
                nb_invalid += 1
                print("invalid", value)
    print(nb_invalid, len(tickets))
    return total


def part_one(inputs: list) -> int:
    fields = read_fields(inputs)
    tickets = read_values(inputs)
    print(tickets)
    return invalid_fields_sum(tickets, fields)


def map_fields(inputs):
    line_nb = 0
    line = inputs[0]
    fields = {}
    while line != "":
        field, numbers = line.split(":")
        fields_values = numbers.split(" or ")
        values_min = [field.split("-")[0] for field in fields_values]
        values_max = [field.split("-")[1] for field in fields_values]
        values_min = list(map(int, values_min))
        values_max = list(map(int, values_max))
        fields[field] = [(vmin, vmax)
                         for vmin, vmax in zip(values_min, values_max)]
        line_nb += 1
        line = inputs[line_nb]
    return fields


def filter_valid_tickets(tickets, fields):
    valid_tickets = []
    nb_invalid = 0
    for ticket in tickets:
        invalid = False
        for value in ticket:
            if not any(a <= value <= b or c <= value <= d
                       for ((a, b), (c, d)) in fields.values()):
                invalid = True
                nb_invalid += 1
                break
        if not invalid:
            valid_tickets.append(ticket)
    return valid_tickets


def possibles_corres(tickets_values, fields, sorted_fields):
    possibles = {field: set() for field in sorted_fields}
    for field in sorted_fields:
        ((a, b), (c, d)) = fields[field]
        for i, values in enumerate(tickets_values):
            if all(a <= val <= b or c <= val <= d for val in values):
                possibles[field].add(i)

    track = []
    for field, possib in possibles.items():
        if len(possib) == 1:
            to_remove = list(possib)[0]
            track.append(to_remove)

    while track:
        suivant = track.pop()
        for field, possib in possibles.items():
            if suivant in possib and len(possib) > 1:
                possib.remove(suivant)
                if len(possib) == 1:
                    to_remove = list(possib)[0]
                    track.append(to_remove)

    return possibles


def get_ticket_values(tickets):
    return [[ticket[i] for ticket in tickets] for i in range(len(tickets[0]))]


def read_my_ticket(inputs, correspondances):
    line_nb = 0
    while inputs[line_nb] != "your ticket:":
        line_nb += 1
    line_nb += 1
    values = list(map(int, inputs[line_nb].split(",")))
    return {correspondances[i]: val for i, val in enumerate(values)}


def sort_fields(fields):
    return sorted(fields.keys(),
                  key=lambda field: (
                      fields[field][0][1] - fields[field][0][0] +
                  fields[field][1][1] - fields[field][1][0]))


def part_two(inputs: list) -> int:
    '''3029180675981'''
    fields = map_fields(inputs)
    tickets = read_values(inputs)
    valid_tickets = filter_valid_tickets(tickets, fields)
    tickets_values = get_ticket_values(valid_tickets)
    sorted_fields = sort_fields(fields)
    corres = possibles_corres(tickets_values, fields, sorted_fields)
    corres_inv = {list(ens)[0]: field for field, ens in corres.items()}
    my_ticket = read_my_ticket(inputs, corres_inv)
    return reduce(int.__mul__, (val
                                for field, val in my_ticket.items()
                                if field.startswith("departure")))

    # return 0


def main():
    inputs: list = read_file("./input.txt")
    # inputs: list = read_file("./example.txt")
    # inputs: list = read_file("./example2.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
