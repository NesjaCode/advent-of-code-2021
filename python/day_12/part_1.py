def parse_input():
    with open("../../input/day_12.txt", "r") as file:
        return [x.strip().split("-") for x in file.readlines()]

caves = parse_input()
paths = [['start']]
stop = False
i = 0
while not stop:
    stop = True
    for i in range(len(paths)):
        current_node = paths[i][-1]
        if current_node != 'end':
            for cave in caves:
                for j in range(2):
                    if cave[j] == current_node:
                        if (cave[j-1].islower() and cave[j-1] not in paths[i]) or cave[j-1].isupper():
                            stop = False
                            if paths[i][-1] != current_node:
                                paths.append(paths[i][:-1])
                                paths[-1].append(cave[j-1])
                            else:
                                paths[i].append(cave[j-1])

result = 0
for path in paths:
    if path[-1] == 'end':
        result += 1

print(result)