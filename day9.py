HEAD_MOVES = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}
TAIL_MOVES = {
    "R": (-1, 0),
    "L": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
    "RU": (1, 1),
    "RD": (1, -1),
    "LU": (-1, 1),
    "LD": (-1, -1),
}


class Knot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.visited = [(x, y)]

    def __repr__(self):
        return self.name

    def move(self, x_delta, y_delta):
        self.x += x_delta
        self.y += y_delta
        if (self.x, self.y) not in self.visited:
            self.visited.append((self.x, self.y))
        return self.x, self.y


def dist(head, tail):
    """Compute the distance between two knots, where diagonal moves are allowed."""
    x_dist = abs(head.x - tail.x)
    y_dist = abs(head.y - tail.y)
    diag_moves = 0
    while x_dist != 0 and y_dist != 0:
        diag_moves += 1
        x_dist -= 1
        y_dist -= 1
    return x_dist + y_dist + diag_moves


def move_tail(head_c, tail_c):
    """Return the move that tail has to make to get closer to head
    for the given axis coordinates."""
    if head_c == tail_c:
        return 0
    elif head_c > tail_c:
        return 1
    else:
        return -1


def make_moves(fname, n_knots):
    """Reads the fname, performs the moves stated there for the head knot, and
    performs the necessary moves for the tail knot, so the distance between them
    is always at most one."""
    knots = [Knot(str(i), 0, 0) for i in range(n_knots)]
    f = open(fname)
    for line in f:
        direction, steps = line.strip().split(" ")
        for _ in range(int(steps)):
            knots[0].move(*HEAD_MOVES[direction])
            for i in range(1, n_knots):
                head = knots[i - 1]
                tail = knots[i]
                if dist(head, tail) > 1:
                    tail_x = move_tail(head.x, tail.x)
                    tail_y = move_tail(head.y, tail.y)
                    tail.move(tail_x, tail_y)
    return knots


if __name__ == "__main__":
    for n_knots in [2, 10]:
        knots = make_moves("day9.txt", n_knots)
        print(len(knots[-1].visited))
