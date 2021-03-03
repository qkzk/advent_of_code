from collections import Counter


def read_inputs():
    with open("./input.txt") as inputs:
        return inputs.readlines()


def parse_inputs(inputs: list) -> list:
    passwords = []
    for line in inputs:
        splits = line.strip().split(" ")
        values = splits[0].split("-")
        values = [int(value) for value in values]
        letter = splits[1][0]
        password = splits[2]
        password_entry = {
            "mini": values[0],
            "maxi": values[1],
            "letter": letter,
            "password": password,
        }
        passwords.append(password_entry)
    return passwords


def check_valid_inputs(passwords: list) -> list:
    valids = []
    for pw in passwords:
        count = Counter(pw["password"])
        if pw["mini"] <= count[pw["letter"]] <= pw["maxi"]:
            valids.append(pw)
    return valids


def check_valid_second_round(passwords: list) -> list:
    return [pw["password"]
            for pw in passwords
            if ((pw["password"][pw["mini"] - 1] == pw["letter"]) ^
                (pw["password"][pw["maxi"] - 1] == pw["letter"]))]


def main():
    inputs: list = read_inputs()
    passwords: list = parse_inputs(inputs)
    print(len(check_valid_inputs(passwords)))
    print(len(check_valid_second_round(passwords)))


if __name__ == "__main__":
    main()
