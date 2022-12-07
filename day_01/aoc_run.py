def part_1(raw_input):
    calorie = 0
    elves_calories = []
    for x in raw_input:
        if x != '':
            calorie += int(x)
        else:
            elves_calories.append(calorie)
            calorie = 0

    elves_calories.append(calorie)

    # search list for highest
    highest = 0
    for n in elves_calories:
        if n > highest:
            highest = n

    return highest

def part_2(raw_input):
    # same as above, but we sort the array
    calorie = 0
    elves_calories = []
    for x in raw_input:
        if x != '':
            calorie += int(x)
        else:
            elves_calories.append(calorie)
            calorie = 0

    elves_calories.append(calorie)

    # search list for highest
    calorie_sum = 0
    elves_calories.sort(reverse=True)

    for n in range(0, 3):
        calorie_sum += elves_calories[n]

    return calorie_sum
