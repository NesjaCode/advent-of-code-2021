def parse_input():
    with open("../../input/day_12.txt", "r") as file:
        return [x.strip().split("-") for x in file.readlines()]

def chech_valid_lower(path, cave):
    counter = 0
    doubles = False
    seen = set()
    for i in path:
        if i.islower() and i != 'start':
            if i == cave:
                counter += 1
            if i in seen:
                doubles = True
            seen.add(i)
    if counter == 0 or (counter == 1 and not doubles):
        return True
    return False

caves = parse_input()
paths = [['start']]
stop = False
i = 0
while not stop:
    stop = True
    for i in range(len(paths)):
        current_node = paths[i][-1]
        current_path = paths[i][::]
        if current_node != 'end':
            for cave in caves:
                for j in range(2):
                    if cave[j] == current_node and cave[j - 1] != 'start':
                        if (cave[j - 1].islower() and chech_valid_lower(current_path, cave[j - 1])) or cave[j - 1].isupper():
                            stop = False
                            if paths[i][-1] != current_node:
                                paths.append(paths[i][:-1])
                                paths[-1].append(cave[j - 1])
                            else:
                                paths[i].append(cave[j - 1])

result = 0
for path in paths:
    if path[-1] == 'end':
        result += 1

print(result)