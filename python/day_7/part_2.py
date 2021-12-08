def parse_input():
    with open("../../input/day_7.txt", "r") as file:
        return [int(i) for i in file.readlines()[0].split(",")]

def calculate_fuel(i, horizontal_pos):
    fuel = []
    for position in horizontal_pos:
        move = abs(position - i)
        fuel.append(int((move/2)*(1 + move)))
    return sum(fuel)

horizontal_pos = parse_input()
max_pos = max(horizontal_pos)
result = []
for i in range(max_pos):
    result.append(calculate_fuel(i, horizontal_pos))

print(min(result))