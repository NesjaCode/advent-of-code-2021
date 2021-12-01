def parse_input():
    with open("../../input/day_{}.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))