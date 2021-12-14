def parse_input():
    with open("../../input/day_1.txt", "r") as file:
        return list(map(lambda x: int(x.strip()), file.readlines()))

input_data = parse_input()
result = 0
for i in range(1, len(input_data)):
    if input_data[i] - input_data[i - 1] > 0:
        result += 1

print(result)