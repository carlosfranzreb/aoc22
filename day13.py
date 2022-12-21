def check_ints(left, right):
    """Return whether the elements are in the right order, and whether
    the next element needs to be checked."""
    ordered = left <= right
    check_next = left == right
    return ordered, check_next


def check_lists(left, right):
    """Return whether the elements are in the right order, and whether
    the next element needs to be checked."""
    check_next = True
    for i in range(len(left)):
        if i >= len(right):
            return False, False
        ordered, check_next = right_order(left[i], right[i])
        if not ordered:
            return False, False
        elif not check_next:
            return True, False
    if len(left) == len(right):
        return True, check_next
    elif len(left) < len(right):
        return True, False


def right_order(left, right):
    """Return whether the elements are in the right order, and whether
    the next element needs to be checked."""
    if isinstance(left, int):
        if isinstance(right, int):
            return check_ints(left, right)
        elif isinstance(right, list):
            return check_lists([left], right)
    elif isinstance(left, list):
        if isinstance(right, int):
            return check_lists(left, [right])
        elif isinstance(right, list):
            return check_lists(left, right)


def q1(fname)
    result = 0
    lines = open(fname).readlines()
    for i in range(0, len(lines), 3):
        left, right = eval(lines[i].strip()), eval(lines[i + 1].strip())
        ordered, _ = check_lists(left, right)
        if ordered:
            result += (i / 3) + 1
    print(result)


def q2(fname):
    result = 0
    lines = open(fname).readlines()
    for i in range(0, len(lines), 3):


if __name__ == "__main__":
    fname = "day13.txt"
    q1(fname)