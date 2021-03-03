from pprint import pprint

def read_file(filename):
    with open(filename) as inputs:
        return inputs.read().strip().splitlines()

def process_line(line):
    line = (line
        .replace("bags", "bag")
        .replace(",", "")
        .replace(".", "")
        .replace("contain", "")
        .replace("no", "")
        .replace("other", ""))
    separation = line.split("bag")
    container = separation[0].strip()
    insides = [" ".join(words.strip().split(" ")[1:]) for words in separation[1:-1]]
    return container, insides

def dfs(graph, source):
    nexts = [source]
    visited = []
    while nexts:
        current = nexts.pop()
        if current not in  visited:
            visited.append(current)
            for neighbor in graph.get(current, []):
                nexts.append(neighbor)
    return visited

def part_one(inputs: list) -> int:
    '''
    You have a shiny gold bag. If you wanted to carry it in at least one other
    bag, how many different bag colors would be valid for the outermost bag?
    (In other words: how many colors can, eventually, contain at least one
     shiny gold bag?)
    '''
    graph = {}
    for line in inputs:
        container, elements = process_line(line)
        for element in elements:
            if element not in graph:
                graph[element] = []
            graph[element].append(container)
    # pprint(graph)
    possibles = dfs(graph, "shiny gold")
    possibles.remove("shiny gold")
    return len(possibles)


def process_line_two(line):
    line = (line
        .replace("bags", "bag")
        .replace(",", "")
        .replace(".", "")
        .replace("contain", "")
        .replace("no", "")
        .replace("other", "")
        .strip())
    separation = line.split("bag")
    container = separation[0].strip()
    phrases = [" ".join(words.strip().split(" ")) for words in separation[1:-1]]
    insides = [(" ".join(words.split(" ")[1:]),
                int(words.split(" ")[0].strip()))
               for words in phrases
               if words != ""]
    return container, insides


def total_bags(graph, source):
    if graph[source] == []:
        return 1
    return 1 + sum(elem[1] * total_bags(graph, elem[0])
                   for elem in graph[source])

def part_two(inputs: list) -> int:
    '''How many individual bags are required inside your single shiny gold bag?'''
    graph = {}
    for line in inputs:
        container, elements = process_line_two(line)
        # print(container, elements)
        graph[container] = elements
    # pprint(graph)
    return total_bags(graph, "shiny gold") - 1

def main():
    # inputs: list = read_file("./example.txt")
    # inputs: list = read_file("./example2.txt")
    inputs: list = read_file("./input.txt")
    # print(part_one(inputs))
    print(part_two(inputs))


if __name__ == "__main__":
    main()
