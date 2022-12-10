class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_left(self):
        self.x += -1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y += -1

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)


class Rope:
    def __init__(self, length):
        self.knots = []
        self.trail = {"0,0"}
        for i in range(0, length):
            self.knots.append(Knot())

    # direction: the direction that the previous knot moved
    def follow_knot(self, previous_movement: str, index: int, previous_knot: Knot):
        up_left = 'UL'
        up = 'U'
        up_right = 'UR'
        left = 'L'
        right = 'R'
        down_left = 'DL'
        down = 'D'
        down_right = 'DR'

        own_movement = ''

        start_x = self.knots[index].x
        start_y = self.knots[index].y

        def previous_knot_moved_left():
            if self.knots[index].x > previous_knot.x + 1:
                return True
            else:
                return False

        def previous_knot_moved_right():
            if self.knots[index].x < previous_knot.x - 1:
                return True
            else:
                return False

        def previous_knot_moved_up():
            if self.knots[index].y < previous_knot.y - 1:
                return True
            else:
                return False

        def previous_knot_moved_down():
            if self.knots[index].y > previous_knot.y + 1:
                return True
            else:
                return False

        # Diagonal movement has 4 cases, no change, move vertically, move horizontally, move both
        if previous_movement == up_left:
            # Order of operations is important here, always check for both first
            # Single case, move both
            if previous_knot_moved_left() and previous_knot_moved_up():
                self.knots[index].move_left()
                self.knots[index].move_up()

            # Two cases, move left
            elif previous_knot_moved_left():
                self.knots[index].move_left()
                self.knots[index].y = previous_knot.y

            # Two cases, move up
            elif previous_knot_moved_up():
                self.knots[index].move_up()
                self.knots[index].x = previous_knot.x

        elif previous_movement == up_right:
            if previous_knot_moved_right() and previous_knot_moved_up():
                self.knots[index].move_right()
                self.knots[index].move_up()

            elif previous_knot_moved_right():
                self.knots[index].move_right()
                self.knots[index].y = previous_knot.y

            elif previous_knot_moved_up():
                self.knots[index].move_up()
                self.knots[index].x = previous_knot.x

        elif previous_movement == down_left:
            if previous_knot_moved_left() and previous_knot_moved_down():
                self.knots[index].move_left()
                self.knots[index].move_down()

            elif previous_knot_moved_left():
                self.knots[index].move_left()
                self.knots[index].y = previous_knot.y

            elif previous_knot_moved_down():
                self.knots[index].move_down()
                self.knots[index].x = previous_knot.x

        elif previous_movement == down_right:
            if previous_knot_moved_right() and previous_knot_moved_down():
                self.knots[index].move_right()
                self.knots[index].move_down()

            elif previous_knot_moved_right():
                self.knots[index].move_right()
                self.knots[index].y = previous_knot.y

            elif previous_knot_moved_down():
                self.knots[index].move_down()
                self.knots[index].x = previous_knot.x

        elif previous_movement == left:
            if previous_knot_moved_left():
                self.knots[index].move_left()
                self.knots[index].y = previous_knot.y

        elif previous_movement == right:

            if previous_knot_moved_right():
                self.knots[index].move_right()
                self.knots[index].y = previous_knot.y

        elif previous_movement == up:
            if previous_knot_moved_up():
                self.knots[index].move_up()
                self.knots[index].x = previous_knot.x

        elif previous_movement == down:
            if previous_knot_moved_down():
                self.knots[index].move_down()
                self.knots[index].x = previous_knot.x

        # Calculate own movement

        if self.knots[index].y < start_y:
            own_movement += 'D'
        elif self.knots[index].y > start_y:
            own_movement += 'U'

        if self.knots[index].x < start_x:
            own_movement += 'L'
        elif self.knots[index].x > start_x:
            own_movement += 'R'

        if not own_movement == '' and index < len(self.knots) - 1:
            self.follow_knot(own_movement, index + 1, self.knots[index])

    def move_left(self):
        self.knots[0].move_left()
        self.follow_knot('L', 1, self.knots[0])

    def move_right(self):
        self.knots[0].move_right()
        self.follow_knot('R', 1, self.knots[0])

    def move_up(self):
        self.knots[0].move_up()
        self.follow_knot('U', 1, self.knots[0])

    def move_down(self):
        self.knots[0].move_down()
        self.follow_knot('D', 1, self.knots[0])

    def update_trail(self):
        self.trail.add(str(self.knots[-1].x) + ',' + str(self.knots[-1].y))

    def trail_amount(self):
        return len(self.trail)

    def visualize(self):
        x_max = 0
        y_max = 0
        for coord in self.knots:
            if coord.x > x_max:
                x_max = coord.x
            if coord.y > y_max:
                y_max = coord.y

        rope_map = []
        for line in range(0, y_max + 1):
            row = []
            for col in range(0, x_max + 1):
                row.append('.')
            rope_map.append(row)

        for i in range(0, len(self.knots)):
            knot = self.knots[i]
            if i == 0:
                rope_map[knot.y][knot.x] = 'H'
            else:
                if rope_map[knot.y][knot.x] == '.':
                    rope_map[knot.y][knot.x] = str(i)

        string = ''
        rope_map.reverse()
        for row in rope_map:
            for char in row:
                string += char
            string += "\n"
        print(string)

    def visualize_trail(self):
        x_max = 0
        y_max = 0
        for coord in self.trail:
            values = coord.split(',')
            if int(values[0]) > x_max:
                x_max = int(values[0])
            if int(values[1]) > y_max:
                y_max = int(values[1])

        trail_map = []
        for y in range(0, y_max + 1):
            line = []
            for x in range(0, x_max + 1):
                line.append(0)
            trail_map.append(line)

        for coord in self.trail:
            values = coord.split(',')
            x = int(values[0])
            y = int(values[1])
            trail_map[y][x] = 1

        string = ""
        for i in range(0, len(trail_map)):
            for mark in trail_map[-i - 1]:
                if mark == 0:
                    string += '.'
                else:
                    string += '#'
            string += '\n'
        print(string)


def parse_input(data):
    instructions = []
    for line in data:
        split_string = line.split(" ")
        instructions.append([split_string[0], int(split_string[1])])
    return instructions


def part_1(raw_input):
    instructions_list = parse_input(raw_input)

    rope = Rope(2)

    for instruction in instructions_list:
        command = instruction[0]
        amount = instruction[1]

        for step in range(0, amount):
            if command == 'R':
                rope.move_right()
            elif command == 'L':
                rope.move_left()
            elif command == 'U':
                rope.move_up()
            elif command == 'D':
                rope.move_down()
            rope.update_trail()

    return rope.trail_amount()


def part_2(raw_input):
    instructions_list = parse_input(raw_input)
    rope = Rope(10)

    for instruction in instructions_list:
        command = instruction[0]
        amount = instruction[1]

        for step in range(0, amount):
            if command == 'R':
                rope.move_right()
            elif command == 'L':
                rope.move_left()
            elif command == 'U':
                rope.move_up()
            elif command == 'D':
                rope.move_down()
            rope.update_trail()
    return rope.trail_amount()
