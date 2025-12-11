def instructions(fname):
    with open(fname) as f:
        for line in f:
            if "noop" in line:
                yield None
            else:
                yield None
                yield int(line.strip().split(" ")[1])


def q1(fname):
    cycles = [20, 60, 100, 140, 180, 220]
    strengths = dict()
    val = 1
    for i, instruction in enumerate(instructions(fname)):
        if i + 1 in cycles:
            strengths[i + 1] = val
        if instruction is not None:
            val += instruction
    print(sum([k * v for k, v in strengths.items()]))


def q2(fname):
    col_start = [1, 41, 81, 121, 161, 201]
    screen = ["." for _ in range(240)]
    sprite_center = 1
    for i, instruction in enumerate(instructions(fname)):
        # draw pixel
        horizontal_pos = i % 40
        if horizontal_pos in range(sprite_center - 1, sprite_center + 2):
            screen[i] = "#"
        # update sprite center
        if instruction is not None:
            sprite_center += instruction
    for i in range(0, len(screen), 40):
        print("".join(screen[i : i + 40]))


if __name__ == "__main__":
    fname = "day10.txt"
    q1(fname)
    q2(fname)

# command to run this script and time it
# time python3 day10.py
