def parse_input():
    with open("../../input/day_8.txt", "r") as file:
        return [[y[0].split(" "), y[1].split(" ")] for y in [x.strip().split(" | ") for x in file.readlines()]]

def backtracking(tests, reference, alphabet, cross_reference=" "*7, current_letter=0):
    if current_letter == 7:
        correct = True
        for test in tests:
            mapped_test = set()
            for letter in test:
                mapped_test.add(cross_reference[alphabet.index(letter)])
            if mapped_test not in reference:
                correct = False
        if correct:
            return cross_reference
        else:
            return None

    for segment in alphabet:
        if segment not in cross_reference:
            cross_reference = cross_reference[:current_letter] + segment + cross_reference[current_letter+1:]
            result = backtracking(tests, reference, alphabet, cross_reference, current_letter + 1)
            if result != None:
                return result

input_data = parse_input()
reference = [set('abcefg'), set('cf'), set('acdeg'), set('acdfg'), set('bcdf'), set('abdfg'), set('abdefg'), set("acf"), set('abcdefg'), set('abcdfg')]
alphabet = list('abcdefg')
solution = []
for line in input_data:
    key = backtracking(line[0], reference, alphabet)
    result = ''
    for i in line[1]:
        mapped_input = ''
        for letter in i:
            mapped_input += key[alphabet.index(letter)]
        result += str(reference.index(set(mapped_input)))
    solution.append(int(result))

print(sum(solution))