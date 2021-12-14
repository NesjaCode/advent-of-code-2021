def parse_input():
    with open("../../input/day_7.txt", "r") as file:
        return [int(i) for i in file.readlines()[0].split(",")]

horizontal_pos = parse_input()
horizontal_pos.sort()
target_pos = horizontal_pos[(len(horizontal_pos) - 1)//2]
fuel = 0
for position in horizontal_pos:
    fuel += int(abs(position - target_pos))

print(fuel)