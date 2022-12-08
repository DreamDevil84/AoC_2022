class Tree:
    def __init__(self, size):
        self.size = size
        self.visible = False
        self.view_score = 0

    def __str__(self):
        return "Size: " + str(self.size) + ", Visible: " + str(self.visible)


def make_tree_array(data):
    trees = []
    for line in data:
        row = []
        for char in line:
            row.append(Tree(int(char)))
        trees.append(row)
    return trees


def part_1(raw_input):
    trees = make_tree_array(raw_input)

    for row in range(0, len(trees)):
        for col in range(0, len(trees[row])):
            if row == 0 or row == len(trees) - 1 or col == 0 or col == len(trees[row]) - 1:
                trees[row][col].visible = True

    # Check left to right
    for row in range(1, len(trees) - 1):
        tallest = trees[row][0].size
        for col in range(1, len(trees[row]) - 1):
            if trees[row][col].size > tallest:
                trees[row][col].visible = True
                tallest = trees[row][col].size
            if tallest == 9:
                break

    # Check right to left
    for row in range(1, len(trees) - 1):
        tallest = trees[row][-1].size
        for col in range(2, len(trees[row])):
            if trees[row][-col].size > tallest:
                trees[row][-col].visible = True
                tallest = trees[row][-col].size
            if tallest == 9:
                break

    # Check top to bottom
    for col in range(1, len(trees[0]) - 1):
        tallest = trees[0][col].size
        for row in range(1, len(trees) - 1):
            if trees[row][col].size > tallest:
                trees[row][col].visible = True
                tallest = trees[row][col].size
            if tallest == 9:
                break

    # Check bottom to top
    for col in range(1, len(trees[0]) - 1):
        tallest = trees[-1][col].size
        for row in range(2, len(trees)):
            if trees[-row][col].size > tallest:
                trees[-row][col].visible = True
                tallest = trees[-row][col].size
            if tallest == 9:
                break

    visible_counter = 0
    for row in trees:
        for tree in row:
            if tree.visible:
                visible_counter += 1

    return visible_counter


def part_2(raw_input):
    trees = make_tree_array(raw_input)
    # Awful nested loops
    for row in range(0, len(trees)):
        for col in range(0, len(trees[row])):
            left_visibility = 0
            right_visibility = 0
            top_visibility = 0
            bottom_visibility = 0

            # Check left
            for index in range(1, col + 1):
                left_visibility += 1
                if trees[row][col - index].size >= trees[row][col].size:
                    break
            # Check right
            for index in range(col + 1, len(trees[row])):
                right_visibility += 1
                if trees[row][index].size >= trees[row][col].size:
                    break
            # Check top
            for index in range(1, row + 1):
                top_visibility += 1
                if trees[row - index][col].size >= trees[row][col].size:
                    break
            # Check bottom
            for index in range(row + 1, len(trees)):
                bottom_visibility += 1
                if trees[index][col].size >= trees[row][col].size:
                    break

            trees[row][col].view_score = left_visibility * right_visibility * top_visibility * bottom_visibility

    # Find highest score
    highest_score = 0
    for line in trees:
        for tree in line:
            if tree.view_score > highest_score:
                highest_score = tree.view_score
    return highest_score
