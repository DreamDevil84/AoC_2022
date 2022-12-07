import time
import sys
import day_01.aoc_run
import day_02.aoc_run
import day_03.aoc_run
import day_04.aoc_run
import day_05.aoc_run
import day_06.aoc_run
import day_07.aoc_run
import day_08.aoc_run
import day_09.aoc_run
import day_10.aoc_run
import day_11.aoc_run
import day_12.aoc_run
import day_13.aoc_run
import day_14.aoc_run
import day_15.aoc_run
import day_16.aoc_run
import day_17.aoc_run
import day_18.aoc_run
import day_19.aoc_run
import day_20.aoc_run
import day_21.aoc_run
import day_22.aoc_run
import day_23.aoc_run
import day_24.aoc_run
import day_25.aoc_run


def run(day, data_file, puzzle_part):
    day_string = ""
    if 0 < int(day) < 10:
        day_string += "0" + day
    elif 9 < int(day) < 26:
        day_string += day

    func_adr = 'day_' + day_string +\
               '.aoc_run.part_' + str(puzzle_part) +\
               '(get_data("' + day_string + '", data_file))'

    def get_data(date, data_type):
        datafile = open('day_' + date + '/' + data_type + '.txt')
        data = []

        for line in datafile:
            entry = line.replace('\n', "")
            data.append(entry)

        datafile.close()
        return data

    return eval(func_adr)


# sample is for the general data provided as part of the puzzle, development only
# input is for the personal data provided
# DATA = 'sample'
DATA = 'input'

print("Please enter a number between 1 and 25")
day_input = input()

if 0 < int(day_input) < 26:
    for part in range(1, 3):
        time_start = time.time()
        print("\n" + str(run(day_input, DATA, part)))
        end_time = (time.time() - time_start) * 1000
        print("{:.2f}".format(end_time) + " ms")
        # print(end_time)
else:
    print("Must be a number between 1 and 25")

# For running specific parts, development only
# print("\n" + str(run(day_input, DATA, 1)))
# print("\n" + str(run(day_input, DATA, 2)))
