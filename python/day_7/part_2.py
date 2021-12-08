def parse_input():
    with open("../../input/day_7.txt", "r") as file:
        return [int(i) for i in file.readlines()[0].split(",")]

def calculate_fuel(target_pos):
    fuel = 0
    for position in horizontal_pos:
        move = abs(position - target_pos)
        fuel += int((move / 2) * (1 + move))
    return fuel

horizontal_pos = parse_input()
target_pos = sum(horizontal_pos) // len(horizontal_pos)

print(min(calculate_fuel(target_pos), calculate_fuel(target_pos + 1)))