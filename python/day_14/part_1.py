def parse_input():
    with open("../../input/day_14.txt", "r") as file:
        data = [x for x in file.read().split("\n\n")]
        return list(data[0]), dict([x.split(" -> ") for x in data[1].split("\n")])

polymer_temp, insertion_rules = parse_input()
for _ in range(10):
    new_polymer = []
    for j in range(len(polymer_temp) - 1):
        new_polymer.append(polymer_temp[j])
        pair = polymer_temp[j] + polymer_temp[j + 1]
        if pair in insertion_rules.keys():
            new_polymer.append(insertion_rules[pair])
    new_polymer.append(polymer_temp[-1])
    polymer_temp = new_polymer[::]

common_elem = [polymer_temp.count(j) for j in set(polymer_temp)]
common_elem.sort()
print(common_elem[-1] - common_elem[0])