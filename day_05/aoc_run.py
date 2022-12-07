def parse_containers(raw):
    data = []
    for char in raw[-1]:
        if char in "123456789":
            data.append("")

    for line in reversed(raw):
        char_index = 1
        array_index = 0
        while char_index < len(line):
            if line[char_index] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                data[array_index] += line[char_index]
            array_index += 1
            char_index += 4

    return data


def parse_instructions(raw):
    data = []
    for line in raw:
        instruction_string = line.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        data.append([int(instruction_string[0]), int(instruction_string[1]) - 1, int(instruction_string[2]) - 1])
    return data


def part_1(raw_input):
    index_of_separator = 0
    for x in range(0, len(raw_input)):
        if raw_input[x] == "":
            index_of_separator = x
            break
    containers = parse_containers(raw_input[:index_of_separator])
    instructions = parse_instructions(raw_input[index_of_separator + 1:])

    for instruction in instructions:
        amount = instruction[0]
        from_index = instruction[1]
        to_index = instruction[2]
        for num in range(0, amount):
            containers[to_index] += containers[from_index][-1:]
            containers[from_index] = containers[from_index][:-1]

    answer = ""

    for line in containers:
        answer += line[-1]

    return answer


def part_2(raw_input):
    index_of_separator = 0
    for x in range(0, len(raw_input)):
        if raw_input[x] == "":
            index_of_separator = x
            break
    containers = parse_containers(raw_input[:index_of_separator])
    instructions = parse_instructions(raw_input[index_of_separator + 1:])

    for instruction in instructions:
        amount = instruction[0]
        from_index = instruction[1]
        to_index = instruction[2]
        containers[to_index] += containers[from_index][-amount:]
        containers[from_index] = containers[from_index][:-amount]

    answer = ""

    for line in containers:
        answer += line[-1]

    return answer
