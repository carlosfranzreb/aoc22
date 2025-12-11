N_ROCKS = 2022


class Wind:
    def __init__(self, winds):
        self.winds = winds
        self.idx = 0

    def get(self):
        out = self.winds[self.idx]
        self.idx += 1
        if self.idx == len(self.winds):
            self.idx = 0
        return 1 if out == ">" else -1


class RockShape:
    def __init__(self, lines):
        self.shape = list()
        for line in lines:
            self.shape.append(list())
            for char in line:
                n = 1 if char == "#" else 0
                self.shape[-1].append(n)
        self.height = len(lines)
        self.width = len(lines[0])


class Rock:
    def __init__(self, id, rock_shape):
        """x,y define the upper left corner of the shape, no matter
        if it's free or solid (0 or 1)."""
        self.id = id
        self.rock_shape = rock_shape
        self.x = 2
        self.y = 0
        self.stopped = False

    def __repr__(self):
        return str(self.id)

    def shift(self, direction, floor):
        new_x = self.x + direction
        if new_x < 0 or new_x + self.rock_shape.width > len(floor[0]):
            return  # new_x outside chamber limits
        elif (
            self.y + self.rock_shape.height - 1 >= 0
        ):  # already in the realm of the floor
            if not self.is_valid(self.y, new_x, floor):
                return
        self.x = new_x

    def drop(self, floor):
        new_y = self.y + 1
        bottom = new_y + self.rock_shape.height - 1
        if bottom == len(floor):
            self.stopped = True
            return  # rock already on the floor
        elif bottom >= 0:  # already in the realm of the floor
            if not self.is_valid(new_y, self.x, floor):
                self.stopped = True
                return
        self.y = new_y

    def is_valid(self, y, x, floor):
        """Whether the move is valid or not."""
        for i in range(self.rock_shape.height):
            for j in range(self.rock_shape.width):
                rock_square = self.rock_shape.shape[i][j]
                floor_square = floor[y + i][x + j]
                if rock_square == 1 and floor_square == 1:
                    return False
        return True


class Chamber:
    def __init__(self, wind, rock_shapes):
        self.width = 7
        self.height = rock_shapes[0].height
        self.wind = wind
        self.rock_shapes = rock_shapes
        self.next_shape = 1
        self.rock = Rock(0, rock_shapes[0])
        self.rock.y = 0  # only the first rock is an exception
        self.n_rocks = 1
        self.floor = [
            [0 for _ in range(self.width)]
            for _ in range(self.rock.rock_shape.height + 3)
        ]

    def add_rock(self):
        """Add a new rock and the necessary space to the floor to encompass it."""
        self.height = max(self.height, len(self.floor) - self.rock.y)
        self.update_floor()
        shape = self.rock_shapes[self.next_shape]
        self.rock = Rock(self.n_rocks, shape)
        self.next_shape += 1
        if self.next_shape == len(self.rock_shapes):
            self.next_shape = 0
        self.n_rocks += 1
        new_height = self.height + self.rock.rock_shape.height + 3
        if new_height > len(self.floor):
            new_floor = [
                [0 for _ in range(self.width)]
                for _ in range(new_height - len(self.floor))
            ]
            self.floor = new_floor + self.floor
        elif new_height < len(self.floor):
            self.floor = self.floor[len(self.floor) - new_height :]
        return self.rock

    def update_floor(self):
        """Add current rock to the floor."""
        rock_range = range(self.rock.y, self.rock.y + self.rock.rock_shape.height)
        for y in range(len(self.floor)):
            if y in rock_range:
                for x in range(self.rock.rock_shape.width):
                    square = self.rock.rock_shape.shape[y - self.rock.y][x]
                    self.floor[y][self.rock.x + x] = square

    def shift(self):
        self.rock.shift(self.wind.get(), self.floor)

    def drop(self):
        self.rock.drop(self.floor)


def parse_input(fname):
    lines = [l.strip() for l in open(fname)]
    wind = Wind(lines[0])
    rock_shapes = list()
    shape = list()
    for line in lines[2:]:
        if line == "":
            rock_shapes.append(RockShape(shape))
            shape = list()
        else:
            shape.append(line)
    rock_shapes.append(RockShape(shape))
    return wind, rock_shapes


def q1(wind, rock_shapes):
    chamber = Chamber(wind, rock_shapes)
    rock = chamber.rock
    while chamber.n_rocks <= N_ROCKS:
        if not rock.stopped:
            chamber.shift()
            chamber.drop()
        else:
            rock = chamber.add_rock()
    return len(chamber.floor)


if __name__ == "__main__":
    fname = "day17.txt"
    wind, rock_shapes = parse_input(fname)
    print(q1(wind, rock_shapes))
