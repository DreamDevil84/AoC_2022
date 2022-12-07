# The joys of recursion

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return self.name + ", " + str(self.size)


class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children: [Directory] = []
        self.size = 0
        self.files: [File] = []

    def new_directory(self, name):
        directory = Directory(name)
        directory.parent = self
        self.children.append(directory)

    def increase_size(self, size):
        self.size += size
        if self.parent:
            self.parent.increase_size(size)

    def new_file(self, name, size):
        self.files.append(File(name, size))
        self.increase_size(int(size))

    def get_sum_of_directories(self, limit):
        dir_sum = 0
        if self.size <= limit:
            dir_sum += self.size
        for child in self.children:
            dir_sum += child.get_sum_of_directories(limit)
        return dir_sum

    def get_list_of_directories(self):
        dir_list = [self.size]
        for child in self.children:
            child_list = child.get_list_of_directories()
            for item in child_list:
                dir_list.append(item)
        return dir_list

    def __str__(self):
        return "Dir: " + str(self.name) + ", " + str(self.size)


def generate_directories(data):
    # Constants
    CHANGE_DIRECTORY = "$ cd "
    SHOW_LIST = "$ ls"
    ROOT_DIRECTORY = "/"
    GO_BACK = ".."
    CREATE_DIRECTORY = "dir "

    root = Directory("/")
    current_dir = root
    index = 0

    # Create directories
    while index < len(data):
        if CHANGE_DIRECTORY in data[index]:
            arg = data[index][5:]
            if arg == ROOT_DIRECTORY:
                current_dir = root
            elif arg == GO_BACK:
                # Does nothing if already at root
                if current_dir.parent:
                    current_dir = current_dir.parent
            else:
                for child in current_dir.children:
                    if child.name == arg:
                        current_dir = child
                        break
        elif SHOW_LIST in data[index]:
            # placeholder
            pass
        elif CREATE_DIRECTORY in data[index]:
            name = data[index][4:]
            new_child = Directory(name)
            new_child.parent = current_dir
            current_dir.children.append(new_child)
        else:
            # create file
            new_file = str(data[index]).split(" ")
            current_dir.new_file(new_file[1], new_file[0])
            pass
        index += 1

    # Calculate directory sizes

    return root


def part_1(raw_input):
    directories = generate_directories(raw_input)
    limit = 100_000
    return directories.get_sum_of_directories(limit)


def part_2(raw_input):
    directories = generate_directories(raw_input)
    total_space = 70_000_000
    update_size = 30_000_000
    space_needed = update_size - (total_space - directories.size)

    directory_list = directories.get_list_of_directories()
    directory_list.sort()

    for size in directory_list:
        if size >= space_needed:
            return size
