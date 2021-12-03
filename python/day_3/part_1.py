def parse_input():
    with open("../../input/day_3.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

puzzle_input = parse_input()
counting = [0]*len(puzzle_input[0])
for code in puzzle_input:
    for i, element in enumerate(code):
        if element == "1":
            counting[i] += 1
        else:
            counting[i] -= 1

gamma_input = ["1" if x > 0 else "0" for x in counting]
epsilon_rate = ["0" if x > 0 else "1" for x in counting]
print(int("".join(gamma_input), 2) * int("".join(epsilon_rate), 2))