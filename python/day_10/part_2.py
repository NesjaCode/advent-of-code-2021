def parse_input():
    with open("../../input/day_10.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

chars = list('()[]{}<>')
points = {')': 1, ']': 2, '}': 3, '>': 4}
solutions = []
for line in parse_input():
    corrupt = False
    correct_completion = ""
    for letter in line:
        if chars.index(letter) % 2 == 0:
            correct_completion = chars[chars.index(letter) + 1] + correct_completion
        else:
            if letter == correct_completion[0]:
                correct_completion = correct_completion[1:]
            else:
                corrupt = True
                break
    if not corrupt:
        result = 0
        for letter in correct_completion:
            result *= 5
            result += points[letter]
        solutions.append(result)

solutions.sort()
print(solutions[len(solutions)//2])