from collections import defaultdict

def parse_input():
    with open("../../input/day_14.txt", "r") as file:
        data = [x for x in file.read().split("\n\n")]
        polymer_template = defaultdict(int)
        for i in range(len(data[0]) - 1):
            polymer_template[data[0][i] + data[0][i + 1]] += 1
        return polymer_template, dict([x.split(" -> ") for x in data[1].split("\n")])

polymer_template, insertion_rules = parse_input()
for _ in range(40):
    temp_polymer = defaultdict(int)
    for pair in polymer_template.keys():
        if pair in insertion_rules.keys():
            new_pair_1 = pair[0] + insertion_rules[pair]
            new_pair_2 = insertion_rules[pair] + pair[1]
            temp_polymer[new_pair_1] += polymer_template[pair]
            temp_polymer[new_pair_2] += polymer_template[pair]
    polymer_template = temp_polymer

solution = []
for letter in set(insertion_rules.values()):
    first_count = 0; second_count = 0
    for pair in polymer_template.keys():
        if letter == pair[0]:
            first_count += polymer_template[pair]
        if letter == pair[1]:
            second_count += polymer_template[pair]
    solution.append(max(first_count, second_count))

solution.sort()
print(solution[-1] - solution[0])