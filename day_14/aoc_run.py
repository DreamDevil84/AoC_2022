import sys


class Caves:
    SAND = 'o'
    ROCK = '#'
    ORIGIN = '+'
    AIR = '.'

    def __init__(self, rock_coordinates: [[(int, int)]], sand_origin: (int, int)):
        self.sand_origin: (int, int) = sand_origin
        self.rock_map: {} = self.generate_map(rock_coordinates, sand_origin)

        # Find edges
        self.x_min = sys.maxsize
        self.x_max = -sys.maxsize

        self.y_min = sys.maxsize
        self.y_max = -sys.maxsize

        for key in self.rock_map.keys():
            x = key[0]
            y = key[1]

            if x < self.x_min:
                self.x_min = x
            if x > self.x_max:
                self.x_max = x
            if y < self.y_min:
                self.y_min = y
            if y > self.y_max:
                self.y_max = y

        # Apply offsets
        self.x_min += -1
        self.x_max += 1
        self.y_min += -1
        self.y_max += 1

    def sand_drip(self):
        sand_grains = 0

        # Returns True if sand falls into void (out of bounds)
        def sand_grain(starting_pos):
            sand_moving = True
            falling_into_void = True
            x_pos = starting_pos[0]
            y_pos = starting_pos[1]

            while sand_moving:
                down_left = (x_pos - 1, y_pos + 1)
                down = (x_pos, y_pos + 1)
                down_right = (x_pos + 1, y_pos + 1)

                if down[1] < self.y_max:
                    if down not in self.rock_map.keys():
                        sand_moving = True
                        y_pos += 1
                    else:
                        if down_left not in self.rock_map.keys():
                            sand_moving = True
                            y_pos += 1
                            x_pos += -1
                        elif down_right not in self.rock_map.keys():
                            sand_moving = True
                            y_pos += 1
                            x_pos += 1
                        else:
                            self.rock_map[(x_pos, y_pos)] = self.SAND
                            return not falling_into_void
                else:
                    return falling_into_void

        filling = True
        dropped_into_void = True

        while filling:
            filling = False
            if sand_grain(self.sand_origin) is not dropped_into_void:
                sand_grains += 1
                filling = True
        return sand_grains

    def sand_drip_with_floor(self):
        sand_grains = 0

        floor = self.y_max + 1

        def sand_grain(starting_pos):
            sand_moving = True
            x_pos = starting_pos[0]
            y_pos = starting_pos[1]

            while sand_moving:
                down_left = (x_pos - 1, y_pos + 1)
                down = (x_pos, y_pos + 1)
                down_right = (x_pos + 1, y_pos + 1)

                if down[1] < floor:
                    sand_moving = True
                    if down not in self.rock_map.keys() and down[1] < floor:
                        y_pos += 1
                    elif down_left not in self.rock_map.keys() and down_left[1] < floor:
                        y_pos += 1
                        x_pos += -1
                    elif down_right not in self.rock_map.keys() and down_right[1] < floor:
                        y_pos += 1
                        x_pos += 1
                    else:
                        sand_moving = False
                        self.rock_map[(x_pos, y_pos)] = self.SAND
                else:
                    sand_moving = False
                    self.rock_map[(x_pos, y_pos)] = self.SAND

        filling = True
        while filling:
            filling = False
            if self.rock_map[self.sand_origin] == self.ORIGIN:
                sand_grain(self.sand_origin)
                sand_grains += 1
                filling = True
        return sand_grains

    @staticmethod
    def generate_map(coordinates: [[(int, int)]], sand_origin: (int, int)):
        map_dict = {}

        rock = '#'

        for line in coordinates:
            start_point = line[0]
            for i in range(1, len(line)):
                end_point = line[i]
                # Have to create rocks from left -> right, up -> down

                # Generate vertical
                if start_point[0] == end_point[0]:
                    start = start_point[1]
                    end = end_point[1]
                    if start < end:
                        for j in range(start, end + 1):
                            map_dict[(start_point[0], j)] = rock
                    else:
                        for j in range(end, start + 1):
                            map_dict[(start_point[0], j)] = rock

                # Generate horizontal
                if start_point[1] == end_point[1]:
                    start = start_point[0]
                    end = end_point[0]
                    if start < end:
                        for j in range(start, end + 1):
                            map_dict[(j, start_point[1])] = rock
                    else:
                        for j in range(end, start + 1):
                            map_dict[(j, start_point[1])] = rock

                # Create new start
                start_point = line[i]

        map_dict[sand_origin] = '+'

        return map_dict

    def display(self):
        string = ""
        for key in self.rock_map.keys():
            x = key[0]
            y = key[1]

            if x < self.x_min:
                self.x_min = x
            if x > self.x_max:
                self.x_max = x
            if y < self.y_min:
                self.y_min = y
            if y > self.y_max:
                self.y_max = y

        x_range = self.x_max - self.x_min + 1
        y_range = self.y_max - self.y_min + 1

        arr = [['.'] * x_range for i in range(y_range)]
        for key in self.rock_map.keys():
            x = key[0] - self.x_min
            y = key[1] - self.y_min

            arr[y][x] = self.rock_map[key]

        for line in arr:
            for char in line:
                string += char
            string += '\n'

        return string


def parse(raw):
    data = []

    for line in raw:
        path_str = line.split(' -> ')
        path = []
        for item in path_str:
            coord = item.split(',')
            x = int(coord[0])
            y = int(coord[1])
            path.append((x, y))
        data.append(path)

    return data


def part_1(raw_input):
    sand_origin = (500, 0)
    rock_coordinates = parse(raw_input)
    caves = Caves(rock_coordinates, sand_origin)

    return caves.sand_drip()


def part_2(raw_input):
    sand_origin = (500, 0)
    rock_coordinates = parse(raw_input)
    caves = Caves(rock_coordinates, sand_origin)

    answer = caves.sand_drip_with_floor()
    # print(caves.display())

    return answer
