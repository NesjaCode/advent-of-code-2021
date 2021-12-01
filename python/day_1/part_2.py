def parse_input():
    with open("../../input/day_1.txt", "r") as file:
        return list(map(lambda x: int(x.strip()), file.readlines()))

input_data = parse_input()
result = 0
for i in range(0, len(input_data) - 3):
    A = input_data[i] + input_data[i + 1] + input_data[i + 2]
    B = input_data[i + 1] + input_data[i + 2] + input_data[i + 3]
    if B - A > 0:
        result += 1

print(result)