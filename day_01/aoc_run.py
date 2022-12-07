def parse(raw):
    calorie = 0
    elves_calories = []
    for line in raw:
        if line != '':
            calorie += int(line)
        else:
            elves_calories.append(calorie)
            calorie = 0

    elves_calories.append(calorie)
    return elves_calories


def part_1(raw_input):
    elves_calories = parse(raw_input)
    # search list for highest
    highest = 0
    for n in elves_calories:
        if n > highest:
            highest = n

    return highest


def part_2(raw_input):
    # same as above, but we sort the list
    elves_calories = parse(raw_input)
    elves_calories.sort()

    calorie_sum = 0
    # sum last 3 entries in list
    for n in range(-3, 0):
        calorie_sum += elves_calories[n]

    return calorie_sum
