import re


def read_inputs():
    with open("./input.txt") as inputs:
        return inputs.readlines()


def read_example():
    with open("./example.txt") as inputs:
        return inputs.readlines()


def read_file(filename):
    with open(filename) as inputs:
        return inputs.readlines()


def byr(field):
    if field == "":
        return False
    if len(field) != 4:
        return False
    try:
        field = int(field)
        return 1920 <= field <= 2002
    except:
        return False


def iyr(field):
    if field == "":
        return False
    if len(field) != 4:
        return False
    try:
        field = int(field)
        return 2010 <= field <= 2020
    except:
        return False


def eyr(field):
    if field == "":
        return False
    if len(field) != 4:
        return False
    try:
        field = int(field)
        return 2020 <= field <= 2030
    except:
        return False


def hgt(field):
    if field == "":
        return False

    if field.endswith("cm"):
        try:
            field = int(field[:-2])
            return 150 <= field <= 193
        except:
            return False
    elif field.endswith("in"):
        try:
            field = int(field[:-2])
            return 59 <= field <= 76
        except:
            return False
    else:
        return False


def hcl(field):
    return len(field) == 7 and re.match("^#([a-f0-9]{6})$", field) is not None


def ecl(field):
    return field in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def pid(field):
    return len(field) == 9 and re.match("^\d{9}$", field) is not None


def nb_valid_fields(string):
    count = 0
    for field in fields:
        if field in string:
            before, after = string.split(field)
            field_data = after.split("\n")[0].split(" ")[0]
            # print("field_type:", field_type)
            valid = validators[field](field_data)
            print(field, "field_data:", field_data, valid)
            if valid:
                count += 1
    return count


def part_one_password_processing(inputs):
    valids = 0
    new_password = True
    count = 0
    print("new password")
    for nb_line, line in enumerate(inputs):

        if not line.strip():  # == "\n":
            if count >= 7:
                valids += 1
            print(count)
            count = 0
            print("new password")
            continue

        print(line)
        count += sum((1 if elem in line else 0 for elem in fields))

    if count >= 7:
        valids += 1
    return valids
    # print(inputs)


def part_two_password_processing(inputs):
    valids = 0
    count = 0
    string = ""
    print("new password")
    for nb_line, line in enumerate(inputs):

        if not line.strip():  # == "\n":
            count = nb_valid_fields(string)
            if count >= 7:
                valids += 1
            print(count)
            count = 0
            string = ""
            print("\nnew password")
            continue

        string += line

    count = nb_valid_fields(string)
    if count >= 7:
        valids += 1
    print("part_two_password_processing returns", valids)
    return valids
    # print(inputs)


def password_validation(password):
    return all(validators[field] for field in validators)


def main():
    inputs: list = read_inputs()
    # inputs: list = read_example()
    # inputs: list = read_file("./valids.txt")
    # print(part_one_password_processing(inputs))
    print(part_two_password_processing(inputs))

    # print(part_two_many_slopes(inputs))


fields = ("byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:")  # , "cid")

validators = {"byr:": byr,
              "iyr:": iyr,
              "eyr:": eyr,
              "hgt:": hgt,
              "hcl:": hcl,
              "ecl:": ecl,
              "pid:": pid}

if __name__ == "__main__":
    main()
