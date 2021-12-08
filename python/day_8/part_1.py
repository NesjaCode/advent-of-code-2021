def parse_input():
    with open("../../input/day_8.txt", "r") as file:
        return [[y[0].split(" "), y[1].split(" ")] for y in [x.strip().split(" | ") for x in file.readlines()]]

result = 0
for segment in parse_input():
    for comb in segment[1]:
        if len(comb) in [2, 3, 4, 7]:
            result += 1

print(result)