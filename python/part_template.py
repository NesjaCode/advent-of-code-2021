def parse_input():
    with open("input.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))