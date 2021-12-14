def parse_input():
    with open("../../input/day_2.txt", "r") as file:
        return list(map(lambda x: x.strip().split(" "), file.readlines()))

puzzle_input = parse_input()
pos = 0
depth = 0
for command in puzzle_input:
    if command[0] == "forward":
        pos += int(command[1])
    elif command[0] == "down":
        depth += int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])

print(pos*depth)