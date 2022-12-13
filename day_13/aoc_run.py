def parse(raw):
    data = []

    index = 0
    # They joy of eval()
    while index < len(raw):
        pair = [
            eval(raw[index]),
            eval(raw[index + 1])
        ]
        data.append(pair)
        index += 3
    return data


def parse_part2(raw):
    data = []
    for line in raw:
        if not line == "":
            data.append(eval(line))
    return data


def compare(first, second):
    # Order of operations is important
    # Cannot use true/false
    # Has 3 outcomes
    # 0: either
    # 1: right order
    # 2: wrong order
    for i in range(0, len(first)):
        if i < len(second):
            # USE CASE: both values are int
            if type(first[i]) is int and type(second[i]) is int:
                # print('both are ints')
                if first[i] < second[i]:
                    return 1
                elif first[i] > second[i]:
                    return 2
            # USE CASE: both values are a list
            elif type(first[i]) is list and type(second[i]) is list:
                # print('both are lists')
                compared_lists = compare(first[i], second[i])
                if not compared_lists == 0 and compared_lists:
                    return compared_lists
            # USE CASE: one value is int and one is a list
            elif type(first[i]) is int and type(second[i]) is list:
                compared = compare([first[i]], second[i])
                if not compared == 0 and compared:
                    return compared
            elif type(second[i]) is int and type(first[i] is list):
                compared = compare(first[i], [second[i]])
                if not compared == 0 and compared:
                    return compared
            else:
                return 0
        # Right side runs out of items
        else:
            return 2
    # Left side runs out of items
    if len(first) == len(second):
        return 0
    else:
        return 1


def part_1(raw_input):
    pairs = parse(raw_input)

    answer = 0

    for i in range(0, len(pairs)):
        result = compare(pairs[i][0], pairs[i][1])
        if result == 1:
            answer += i + 1
    return answer


def part_2(raw_input):
    data = parse_part2(raw_input)

    divider_1 = [[2]]
    divider_2 = [[6]]

    divider_1_index = 0
    divider_2_index = 0

    data.append(divider_1)
    data.append(divider_2)

    index_list = []
    for i in range(0, len(data)):
        index_list.append(i)

    debug = False

    sorting = True
    while sorting:
        sorting = False
        for i in range(0, len(index_list) - 1):
            first_index = index_list[i]
            second_index = index_list[i + 1]
            result = compare(data[first_index], data[second_index])
            if result == 2:
                sorting = True
                index_list[i] = second_index
                index_list[i + 1] = first_index

    new_data = []

    for index in index_list:
        new_data.append(data[index])

    for i in range(0, len(new_data)):
        if new_data[i] == divider_1:
            divider_1_index = i + 1
        if new_data[i] == divider_2:
            divider_2_index = i + 1

    return divider_1_index * divider_2_index
