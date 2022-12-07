def parse(raw):
    data = []
    for line in raw:
        elves = line.split(',')
        elf_ranges = []
        for elf in elves:
            temp = elf.split('-')
            elf_ranges.append([int(temp[0]), int(temp[1])])
        data.append(elf_ranges)
    return data


def part_1(raw_input):
    data = parse(raw_input)

    # Find ranges that completely envelop others
    envelop_counter = 0
    for line in data:
        first_elf_start = line[0][0]
        first_elf_end = line[0][1]
        second_elf_start = line[1][0]
        second_elf_end = line[1][1]

        # First elf is enveloped by second elf
        if first_elf_start >= second_elf_start and first_elf_end <= second_elf_end:
            envelop_counter += 1
        # Second elf enveloped by first
        elif first_elf_start <= second_elf_start and first_elf_end >= second_elf_end:
            envelop_counter += 1
    return envelop_counter


def part_2(raw_input):
    data = parse(raw_input)

    envelop_counter = 0
    for line in data:
        first_elf_start = line[0][0]
        first_elf_end = line[0][1]
        second_elf_start = line[1][0]
        second_elf_end = line[1][1]

        # Add new cases
        # First elf is enveloped by second elf
        if first_elf_start >= second_elf_start and first_elf_end <= second_elf_end:
            envelop_counter += 1
        # Second elf enveloped by first
        elif first_elf_start <= second_elf_start and first_elf_end >= second_elf_end:
            envelop_counter += 1
        # Check if edges are within the range of the other elf
        elif first_elf_start <= second_elf_start <= first_elf_end:
            envelop_counter += 1
        elif first_elf_start <= second_elf_end <= first_elf_end:
            envelop_counter += 1

    return envelop_counter
