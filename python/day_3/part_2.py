def parse_input():
    with open("../../input/day_3.txt", "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def calculate_rating(input_binary, most_common=True):
    for i in range(len(puzzle_input[0])):
        if len(input_binary) == 1:
            break

        counting = 0
        for j in range(len(input_binary)):
            if input_binary[j][i] == "1":
                counting += 1
            else:
                counting -= 1

        if counting >= 0:
            common = "1"
        else:
            common = "0"

        if most_common:
            input_binary = list(filter(lambda x: x[i] == common, input_binary))
        else:
            input_binary = list(filter(lambda x: x[i] != common, input_binary))

    return "".join(input_binary)

puzzle_input = parse_input()
print(int(calculate_rating(puzzle_input), 2) * int(calculate_rating(puzzle_input, False), 2))