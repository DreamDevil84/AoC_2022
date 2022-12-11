class Monkey:
    def __init__(self, items: [int], operator: str, parameter: str, test: int, true_target: int, false_target: int):
        self.items: [int] = items
        self.operator: str = operator
        self.parameter: str = parameter
        self.test: int = test
        self.true_target: int = true_target
        self.false_target: int = false_target
        self.times_inspected: int = 0

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self):
        string = "Items: " + str(self.items) + "\n"
        string += "Old = old " + str(self.operator) + " " + str(self.parameter) + "\n"
        string += "Divided by " + str(self.test) + "\n"
        string += "  If true: " + str(self.true_target) + "\n"
        string += "  If false: " + str(self.false_target) + "\n"
        return string


class MonkeyKeepAway:
    def __init__(self, monkeys: [Monkey]):
        self.monkeys: [Monkey] = monkeys

    def game_round_with_division(self):
        def inspect_and_throw_with_division(monkey: Monkey):
            def inspect(worry, operator, parameter):
                if parameter == 'old':
                    par = worry
                else:
                    par = int(parameter)
                if operator == '+':
                    return worry + par
                elif operator == '-':
                    return worry - par
                elif operator == '*':
                    return worry * par
                elif operator == '/':
                    return worry / par

            def test(worry, val):
                if worry % val == 0:
                    return True
                else:
                    return False

            for i in range(0, len(monkey.items)):
                item = monkey.items.pop(0)
                item = inspect(item, monkey.operator, monkey.parameter)
                monkey.times_inspected += 1
                item = int(item / 3)
                if test(item, monkey.test):
                    self.monkeys[monkey.true_target].add_item(item)
                else:
                    self.monkeys[monkey.false_target].add_item(item)

        for monkey_item in self.monkeys:
            inspect_and_throw_with_division(monkey_item)

    def two_most_active_monkeys(self):
        inspected_arr = []
        for monkey in self.monkeys:
            inspected_arr.append(monkey.times_inspected)
        inspected_arr.sort(reverse=True)
        return inspected_arr[0] * inspected_arr[1]

    def game_round_with_factorising(self):
        # Use modulo to prevent numbers becoming too large
        mod = 1
        for monkey_test in self.monkeys:
            mod *= monkey_test.test

        def inspect_and_throw_with_factorising(monkey: Monkey):
            def inspect(worry, operator, parameter):
                if parameter == 'old':
                    par = worry
                else:
                    par = int(parameter)
                if operator == '+':
                    return worry + par
                elif operator == '-':
                    return worry - par
                elif operator == '*':
                    return worry * par

            def test(worry, val):
                if worry % val == 0:
                    return True
                else:
                    return False

            for i in range(0, len(monkey.items)):
                item = monkey.items.pop(0)
                item = inspect(item, monkey.operator, monkey.parameter) % mod
                monkey.times_inspected += 1
                if test(item, monkey.test):
                    self.monkeys[monkey.true_target].add_item(item)
                else:
                    self.monkeys[monkey.false_target].add_item(item)

        for monkey_item in self.monkeys:
            inspect_and_throw_with_factorising(monkey_item)

    # For development
    def show_monkey_inventory(self):
        string = ""
        for i in range(0, len(self.monkeys)):
            string += "Monkey " + str(i) + ": "
            for j in range(0, len(self.monkeys[i].items)):
                string += str(self.monkeys[i].items[j])
                if not j == len(self.monkeys[i].items) - 1:
                    string += ", "
            string += "\n"

        print(string)

    def show_times_inspected(self):
        string = ""
        for i in range(0, len(self.monkeys)):
            string += "Monkey " + str(i) + " inspected items " + str(self.monkeys[i].times_inspected) + " times."
            string += "\n"

        print(string)

    def __str__(self):
        string = ""
        for monkey in self.monkeys:
            string += str(monkey)
            string += "\n"
        return string


def parse(raw):
    monkeys = []
    monkey_index = 0
    monkey_stuff = []
    for line in raw:
        if 'Starting' in line:
            items = line[18:].split(', ')
            items_int = []
            for x in items:
                items_int.append(int(x))
            monkey_stuff.append(items_int)
        elif 'Operation' in line:
            operator = line[23:24]
            parameter = line[25:]
            monkey_stuff.append(operator)
            monkey_stuff.append(parameter)
        elif 'Test' in line:
            divisible = int(line[-2:])
            monkey_stuff.append(divisible)
        elif 'If true' in line:
            true_target = int(line[-1:])
            monkey_stuff.append(true_target)
        elif 'If false' in line:
            false_target = int(line[-1:])
            monkey_stuff.append(false_target)
        if line == "":
            monkeys.append(Monkey(monkey_stuff[0],
                                  monkey_stuff[1],
                                  monkey_stuff[2],
                                  monkey_stuff[3],
                                  monkey_stuff[4],
                                  monkey_stuff[5]
                                  ))
            monkey_index += 1
            monkey_stuff = []

    monkeys.append(Monkey(monkey_stuff[0],
                          monkey_stuff[1],
                          monkey_stuff[2],
                          monkey_stuff[3],
                          monkey_stuff[4],
                          monkey_stuff[5]
                          ))
    return monkeys


def part_1(raw_input):
    monkeys = parse(raw_input)
    monkey_game = MonkeyKeepAway(monkeys)
    for i in range(0, 20):
        monkey_game.game_round_with_division()
    return monkey_game.two_most_active_monkeys()


def part_2(raw_input):
    monkeys = parse(raw_input)
    monkey_game = MonkeyKeepAway(monkeys)
    for i in range(0, 10000):
        monkey_game.game_round_with_factorising()
    return monkey_game.two_most_active_monkeys()
