def parse_input():
    with open("../../input/day_10.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def check_if_valid(line, chars):
    counters = [0 for j in range(4)]
    for i in line:
        element_index = chars.index(i)
        if element_index % 2 == 0:
            counters[element_index//2] += 1
        else:
            counters[element_index//2] -= 1
    if sum(counters) != 0:
        return False
    return True

def check_corrupted(line, chars):
    for i, element in enumerate(line):
        counter = 0
        if chars.index(element) % 2 != 0:
            for j in range(i, -1, -1):
                if line[j] == element:
                    counter += 1
                elif chars.index(line[j]) == chars.index(element) - 1 and counter != 0:
                    counter -= 1
                if chars.index(line[j]) == chars.index(element) - 1 and counter == 0:
                    if not check_if_valid(line[j+1:i], chars):
                        return element
                    break
                if j == 0:
                    return element

chars = list('()[]{}<>')
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
solution = 0
for line in parse_input():
    result = check_corrupted(line, chars)
    if result != None:
        solution += points[result]
    else:
        with open("../../input/day_10_incomp.txt", "a") as file:
            file.write(line + "\n")

print(solution)