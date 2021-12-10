def parse_input():
    with open("../../input/day_10_incomp.txt", "r") as file:
        return [x.strip() for x in file if x != ""]

def get_couple(line, chars):
    for i, element in enumerate(line):
        counter = 0
        if chars.index(element) % 2 != 0:
            for j in range(i, -1, -1):
                if line[j] == element:
                    counter += 1
                elif chars.index(line[j]) == chars.index(element) - 1 and counter != 0:
                    counter -= 1
                if chars.index(line[j]) == chars.index(element) - 1 and counter == 0:
                    return j, i

chars = list('()[]{}<>')
points = {')': 1, ']': 2, '}': 3, '>': 4}
solutions = []
incomplete_lines = parse_input()
for line in incomplete_lines:
    solution = 0
    while True:
        result = get_couple(line, chars)
        if result != None:
            start = result[0]
            end = result[1]
            line = line[:start] + line[start+1:end] + line[end+1:]
        else:
            break
    closing_chars = "".join([chars[chars.index(x) + 1] for x in line[::-1]])
    for letter in closing_chars:
        solution *= 5
        solution += points[letter]
    solutions.append(solution)

solutions.sort()
print(solutions[len(solutions)//2])