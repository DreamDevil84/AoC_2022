import sys


class Node:
    def __init__(self, elevation: int, is_start: bool, is_end: bool, x: int, y: int, starting_weight: int):
        self.elevation: int = elevation
        self.x: int = x
        self.y: int = y
        self.start = is_start
        self.end = is_end
        self.neighbor_nodes: [Node] = []
        self.weight = starting_weight

    def shortest_path(self):
        def recurse(node: Node):
            for neighbor in node.neighbor_nodes:
                if neighbor.elevation <= node.elevation + 1:
                    if neighbor.weight > node.weight + 1:
                        neighbor.weight = node.weight + 1
                        recurse(neighbor)

        recurse(self)

    def reversed_path(self):
        def recurse(node: Node):
            for neighbor in node.neighbor_nodes:
                if neighbor.elevation >= node.elevation - 1:
                    if neighbor.weight > node.weight + 1:
                        neighbor.weight = node.weight + 1
                        recurse(neighbor)
        recurse(self)

    def __str__(self):
        return str(self.elevation)


def parse(raw):
    node_map = []
    # Create Nodes
    max_steps = len(raw) * len(raw[0])
    for row in range(0, len(raw)):
        node_line = []
        for col in range(0, len(raw[row])):
            if raw[row][col] == 'S':
                node_line.append(Node(0, True, False, col, row, 0))
            elif raw[row][col] == 'E':
                node_line.append(Node(25, False, True, col, row, max_steps))
            else:
                elevation = ord(raw[row][col]) - 97
                node_line.append(Node(elevation, False, False, col, row, max_steps))
        node_map.append(node_line)
    # Bind nodes
    for row in range(0, len(node_map)):
        for col in range(0, len(node_map[row])):
            if 0 < col:
                node_map[row][col].neighbor_nodes.append(node_map[row][col - 1])
            if col < len(node_map[row]) - 1:
                node_map[row][col].neighbor_nodes.append(node_map[row][col + 1])
            if 0 < row:
                node_map[row][col].neighbor_nodes.append(node_map[row - 1][col])
            if row < len(node_map) - 1:
                node_map[row][col].neighbor_nodes.append(node_map[row + 1][col])
    return node_map


# Djikstra time
def part_1(raw_input):
    nodes = parse(raw_input)

    for line in nodes:
        for node in line:
            if node.start:
                node.shortest_path()

    for line in nodes:
        for node in line:
            if node.end:
                return node.weight
    return 0


def part_2(raw_input):
    # Do the same, but in reverse
    nodes = parse(raw_input)

    min_steps = len(nodes) * len(nodes[0])

    for line in nodes:
        for item in line:
            if item.start:
                item.weight = len(nodes) * len(nodes[0])
            if item.end:
                item.weight = 0

    # Increase recursion limit above 999, careful this might cause stack overflow with too high a dataset
    sys.setrecursionlimit(len(nodes) * len(nodes[0]))

    for line in nodes:
        for node in line:
            if node.end:
                node.reversed_path()

    for line in nodes:
        for item in line:
            if item.elevation == 0 and item.weight < min_steps:
                min_steps = item.weight

    return min_steps
