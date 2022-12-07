class Directory:
    """Stores the file sizes and subdirectories found in a directory. It also keeps track
    of whether we have iterated through the directory or not. If we have iterated through
    the directory, we can calculate the size of the directory."""

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent = parent_dir
        self.file_sizes = []
        self.subdirs = []
        self.size = None  # sum of the file sizes and the dir sizes

    def __repr__(self):
        return self.name

    def add_file_size(self, file_size):
        self.file_sizes.append(file_size)

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def get_size(self):
        if self.size is not None:
            return self.size
        else:
            self.size = sum(self.file_sizes)
            for subdir in self.subdirs:
                self.size += subdir.get_size()
            return self.size


class Crawler:
    """Stores the tree of dirs that have been visited. When a dir is visited, it creates
    a new Directory object and adds it to the tree. It also keeps track of the current
    directory so that we can add files and subdirs to the correct directory."""

    def __init__(self, root_name):
        self.root = Directory(root_name, None)
        self.current_dir = self.root
        self.all_dirs = [self.root]

    def add_file(self, file_size):
        self.current_dir.add_file_size(file_size)

    def add_subdir(self, dir_name):
        new_dir = Directory(dir_name, self.current_dir)
        self.current_dir.add_subdir(new_dir)
        self.all_dirs.append(new_dir)

    def visit_dir(self, dir_name):
        for folder in self.current_dir.subdirs:
            if folder.name == dir_name:
                self.current_dir = folder
                return
        raise Exception("Directory not found")

    def leave_dir(self):
        self.current_dir = self.current_dir.parent


def parse_line(line):
    """Parses an input line and outputs a tuple containing whether it is a command
    (identified by the $ symbol at the beginning), or a file or dir. Files stated
    with their size and their name. Dirs are just ther name, preceded by "dir"."""
    content = line.strip().split(" ")
    is_command = content[0] == "$"
    if is_command:
        if content[1] == "ls":
            return (True, "ls", None)
        elif content[1] == "cd":
            return (True, "cd", content[2])
    else:
        if content[0] == "dir":
            return (False, "dir", content[1])
        else:
            return (False, "file", int(content[0]))


def parse_file(filename):
    """Parses a file and returns the resulting crawler object, which contains all the
    information about the directory tree."""
    f = open(filename)
    _, _, root_dir = parse_line(f.readline())
    crawler = Crawler(root_dir)
    for line in f:
        is_command, command, arg = parse_line(line)
        if is_command:
            if command == "cd":
                if arg == "..":  # go up a directory
                    crawler.leave_dir()
                else:  # enter directory
                    crawler.visit_dir(arg)
        else:  # line is not a command
            if command == "file":
                crawler.add_file(arg)
            elif command == "dir":
                crawler.add_subdir(arg)
    f.close()
    return crawler


def q1(crawler):
    """Print the sum of all directories that have a total size of at most 100,000.
    Children and parents can be both included in this sum. The crawler must be complete,
    meaning that it must have iterated through the whole input file."""
    total = 0
    for folder in crawler.all_dirs:
        print(folder, folder.get_size())
        if folder.get_size() <= 100000:
            total += folder.get_size()
    print(total)


def q2(crawler):
    """Find the smallest directory that, if deleted, would free up enough space on the
    filesystem to run the update. The total disk space is 70,000,000. We need unused
    space of at least 30,000,000."""
    space_used = crawler.root.get_size()
    print("Space used:", space_used)
    print("Space to be freed:", space_used - 40000000)
    min_dir = None
    for folder in crawler.all_dirs:
        if space_used - folder.get_size() <= 40000000:
            if min_dir is None:
                min_dir = folder
            elif folder.get_size() < min_dir.get_size():
                min_dir = folder
    print(min_dir.name, min_dir.get_size())


if __name__ == "__main__":
    crawler = parse_file("day7.txt")
    q2(crawler)
