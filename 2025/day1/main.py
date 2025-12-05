def ceil(n: float) -> int:
    """Ceil the float, assuming it is not negative."""
    n_int = int(n)
    if n - n_int == 0:
        return n_int
    else:
        return n_int + 1


def update_position(old_pos: int, rotation: int) -> tuple[int, int]:

    # calculate times zero is passed
    rotation_sign = -1 if rotation < 0 else 1
    div = abs(rotation) // 100
    mod = abs(rotation) % 100
    add = old_pos + mod * rotation_sign
    n_zeros = div + int(add > 99) + int(add < 0)

    # update position
    position = old_pos + rotation
    if position > 99:
        position %= 100
    elif position < 0:
        position += ceil(position / -100) * 100

    return position, n_zeros


def task1(input_f: str) -> int:
    position = 50
    n_zeros = 0

    for line in open(input_f):
        rotation_str = line.strip()
        if rotation_str.startswith("R"):
            rotation = int(rotation_str[1:])
        elif rotation_str.startswith("L"):
            rotation = int(rotation_str.replace("L", "-"))

        position = update_position(position, rotation)[0]
        n_zeros += position == 0

    return n_zeros


def task2(input_f: str) -> int:
    position = 50
    n_zeros = 0

    for line in open(input_f):
        rotation_str = line.strip()
        if rotation_str.startswith("R"):
            rotation = int(rotation_str[1:])
        elif rotation_str.startswith("L"):
            rotation = int(rotation_str.replace("L", "-"))

        position, new_zeros = update_position(position, rotation)
        n_zeros += new_zeros

    return n_zeros


if __name__ == "__main__":
    input_f = "input.txt"
    print("task 1: ", task1(input_f))
    print("task 2: ", task2(input_f))
