class CommDevice:
    def __init__(self, data):
        self.register = 1
        self.cycle = []

        for line in data:
            if line[0] == 'noop':
                self.noop()
            else:
                self.add_value(line[1])

    def add_value(self, val):
        self.cycle.append(self.register)
        self.cycle.append(self.register)
        self.register += val

    def noop(self):
        self.cycle.append(self.register)


def parse(raw):
    data = []
    for line in raw:
        temp = line.split(' ')
        if temp[0] == 'noop':
            data.append(['noop'])
        else:
            data.append(['addx', int(temp[1])])

    return data


def part_1(raw_input):
    data = parse(raw_input)
    device = CommDevice(data)
    signal_strength = 0
    for i in range(0, 6):
        current_cycle = (i * 40) + 20
        print(current_cycle * device.cycle[current_cycle - 1])
        signal_strength += current_cycle * device.cycle[current_cycle - 1]

    return signal_strength


def part_2(raw_input):
    data = parse(raw_input)
    device = CommDevice(data)

    image = ""
    for i in range(0, len(device.cycle)):
        sprite_pos = device.cycle[i]
        pixel_pos = i % 40
        if pixel_pos in range(sprite_pos - 1, sprite_pos + 2):
            image += '#'
        else:
            image += '.'

        if pixel_pos == 39:
            image += '\n'

    return image
