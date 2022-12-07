# CheatSheet: A - Z: 65 - 90
#                    27 - 52
#             a - z: 97 - 122
#                    1 - 26
# ord(char): convert char to integer
# chr(int): convert integer to char

def convert_priority(char):
    char_int = ord(char)
    if 64 < char_int < 91:
        char_int += -38
    elif 96 < char_int < 123:
        char_int += - 96
    return char_int


def part_1(raw_input):
    duplicates = []
    for line in raw_input:
        # First split each line in half
        middle_index = int(len(line)/2)
        first_half = line[:middle_index]
        second_half = line[middle_index:]

        duplicate_in_line = []
        # Compare each char in first half with second half to find duplicates
        for char_first in first_half:
            for char_second in second_half:
                if char_first == char_second:
                    duplicate_in_line.append(char_first)

        duplicates.append(duplicate_in_line[0])

    priority_score = 0
    # Convert characters in duplicates into their priority number
    for char in duplicates:
        priority_score += convert_priority(char)

    return priority_score


def part_2(raw_input):
    # More parsing

    priority_score = 0

    index = 0
    while index < len(raw_input):
        letters_set = set()
        # Separate groups
        group = [
            raw_input[index],
            raw_input[index + 1],
            raw_input[index + 2]
        ]

        # Find common chars between 1st and 2nd line
        for char_0 in group[0]:
            for char_1 in group[1]:
                if char_0 == char_1:
                    letters_set.add(char_0)

        # Find common char in 3rd line
        common_char = ''
        for char_2 in group[2]:
            if char_2 in letters_set:
                common_char = char_2

        priority_score += convert_priority(common_char)
        index += 3
    return priority_score
