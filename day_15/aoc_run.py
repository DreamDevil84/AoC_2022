class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "X: " + str(self.x) + ', Y: ' + str(self.y)


class Sensor:
    def __init__(self, sensor_coord: [int], beacon_coord: [int]):
        self.coord = Coordinate(sensor_coord[0], sensor_coord[1])
        self.target = Coordinate(beacon_coord[0], beacon_coord[1])
        self.manhattan_distance = abs(self.coord.x - self.target.x) + abs(self.coord.y - self.target.y)

    def is_in_range(self, x: int, y: int):
        return abs(x - self.coord.x) + abs(y - self.coord.y) <= self.manhattan_distance

    def __str__(self):
        return "Self: " + str(self.coord.x) + ", " + str(self.coord.y) +\
               "\nTarget: " + str(self.target.x) + ", " + str(self.target.y) + \
               "\nManhattan Distance: " + str(self.manhattan_distance)


class SensorMap:
    def __init__(self, sensors: [Sensor]):
        self.sensors: [Sensor] = sensors

    def find_empty_space(self, start_value: int, end_value: int):
        def get_steps(cur: Coordinate, sens: Sensor) -> int:
            distance_from_center = Coordinate(cur.x - sens.coord.x, cur.y - sens.coord.y)
            return int((sens.manhattan_distance - (distance_from_center.x + distance_from_center.y)) / 2) + 1

        for sensor in self.sensors:
            # Empty cell will always be along one upper-right edge

            top_point = sensor.coord.y - sensor.manhattan_distance - 1
            right_point = sensor.coord.x + sensor.manhattan_distance + 1
            cursor = Coordinate(sensor.coord.x, top_point)

            # Adjust cursor so it is within range
            if cursor.x < start_value:
                cursor.y += abs(cursor.x)
                cursor.x = 0
            if cursor.y < start_value:
                cursor.x += abs(cursor.y)
                cursor.y = 0

            # Check current position against all sensor ranges
            # Find largest step
            checking_cursor = True
            if cursor.x > end_value or cursor.y > end_value:
                checking_cursor = False
            while checking_cursor:
                max_steps = 0
                is_empty = True
                for other_sensor in self.sensors:
                    if other_sensor.is_in_range(cursor.x, cursor.y):
                        is_empty = False
                        step = get_steps(cursor, other_sensor)
                        if step > max_steps:
                            max_steps = step
                # If none of the other sensors hit the cursor, empty cell found
                if is_empty:
                    return cursor
                # Goto new cursor point
                cursor.x += max_steps
                cursor.y += max_steps
                # Repeat until x in cursor point > right_point
                if cursor.x > right_point or cursor.x > end_value or cursor.y > end_value:
                    checking_cursor = False

            # Go to next sensor


def parse(raw):
    data: [Sensor] = []
    for line in raw:
        arr = line.split(': ')
        for i in range(2):
            arr[i] = arr[i][arr[i].find('x')+2:]
            arr[i] = arr[i].replace(' y=', '')
            arr[i] = arr[i].split(',')
            for j in range(2):
                arr[i][j] = int(arr[i][j])
        data.append(Sensor(arr[0], arr[1]))

    return data


def range_of_occupied_coords_on_row(sensors, row_to_check):
    # Create array of ranges
    x_ranges = []
    for sensor in sensors:
        # Check if sensor range reaches row to check
        if abs(sensor.coord.y - row_to_check) <= sensor.manhattan_distance:
            distance = sensor.manhattan_distance - abs(sensor.coord.y - row_to_check)
            x_ranges.append([sensor.coord.x - distance, sensor.coord.x + distance])

    comparing = True
    while comparing:
        comparing = False
        for i in range(len(x_ranges)):
            current_range = x_ranges[i]
            for j in range(0, len(x_ranges)):
                if x_ranges[j][0] < current_range[0] < x_ranges[j][1] or\
                        x_ranges[j][0] < current_range[1] < x_ranges[j][1]:
                    comparing = True
                if x_ranges[j][0] <= current_range[0] <= x_ranges[j][1]:
                    current_range[0] = x_ranges[j][0]
                if x_ranges[j][0] <= current_range[1] <= x_ranges[j][1]:
                    current_range[1] = x_ranges[j][1]
            x_ranges[i] = current_range

    true_ranges = [x_ranges[0]]
    for x_range in x_ranges:
        if not x_range == x_ranges[0]:
            true_ranges.append(x_range)

    return true_ranges


# Don't make a 2D array, it's a trap
def part_1(raw_input):
    row_to_check = 2_000_000
    sensors: [Sensor] = parse(raw_input)

    true_ranges = range_of_occupied_coords_on_row(sensors, row_to_check)

    answer = 0
    for x in true_ranges:
        answer += abs(x[0]) + abs(x[1])

    return answer


def part_2(raw_input):
    sensor_map = SensorMap(parse(raw_input))
    min_distance = 0
    max_distance = 4_000_000

    coord = sensor_map.find_empty_space(min_distance, max_distance)

    def get_tuning(x_val: int, y_val: int):
        return (x_val * 4_000_000) + y_val

    return get_tuning(coord.x, coord.y)
