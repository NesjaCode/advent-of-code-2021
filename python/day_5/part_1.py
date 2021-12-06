def parse_input():
    with open("../../input/day_5.txt", "r") as file:
        input_data = list(map(lambda x: x.strip(), file.readlines()))
        input_data = [x.split(" -> ") for x in input_data if
                      x.split(" -> ")[0].split(",")[0] == x.split(" -> ")[1].split(",")[0] or
                      x.split(" -> ")[0].split(",")[1] == x.split(" -> ")[1].split(",")[1]]
        input_data = list(map(lambda x: [[int(x[0].split(",")[0]), int(x[0].split(",")[1])],
                                         [int(x[1].split(",")[0]), int(x[1].split(",")[1])]], input_data))
        return input_data

def increment_result(point, result):
    if point in result:
        result[point] += 1
    else:
        result[point] = 1
    return result

lines = parse_input()
result = dict()
for line in lines:
    if line[0][0] == line[1][0]:
        for i in range(abs(line[1][1] - line[0][1]) + 1):
            point = (line[0][0], min(line[1][1], line[0][1]) + i)
            result = increment_result(point, result)
    elif line[0][1] == line[1][1]:
        for i in range(abs(line[1][0] - line[0][0]) + 1):
            point = (min(line[0][0], line[1][0]) + i, line[0][1])
            result = increment_result(point, result)

print(sum([1 for x in result.values() if x > 1]))