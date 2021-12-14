def parse_input():
    with open("../../input/day_6.txt", "r") as file:
        return [int(x) for x in file.readlines()[0].split(',')]

def calculate_population(lanters, max_days):
    fish_dict = dict()
    for i in range(9):
        fish_dict[i] = lanters.count(i)
    for i in range(max_days):
        number_of_zeroes = fish_dict[0]
        for x in range(8):
            fish_dict[x] = fish_dict[x + 1]
        fish_dict[8] = number_of_zeroes
        fish_dict[6] += number_of_zeroes
    return fish_dict

print(sum(calculate_population(parse_input(), 256).values()))