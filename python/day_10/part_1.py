def parse_input():
    with open("../../input/day_10.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

chars = list('()[]{}<>')
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
solution = 0
for line in parse_input():
    correct_completion = ""
    for letter in line:
        if chars.index(letter) % 2 == 0:
            correct_completion = chars[chars.index(letter) + 1] + correct_completion
        else:
            if letter == correct_completion[0]:
                correct_completion = correct_completion[1:]
            else:
                solution += points[letter]
                break

print(solution)