def visible_one_side(ints, reverse):
    """Given a list of integers, return a boolean array of the same size stating
    whether the value at that index is larger than all the values to its left. The
    first one doesn't count."""
    if reverse:
        ints = ints[::-1]
    max_height = -1
    visible = [False for _ in ints]
    for i, height in enumerate(ints):
        if height > max_height:
            visible[i] = True
            max_height = height
    if reverse:
        visible = visible[::-1]
    return visible


def visible_both_sides(ints):
    """Given a list of integers, return a boolean array of the same size stating
    whether the value at that index is larger than either all the values to its left or
    right. The first and last ones don't count."""
    left = visible_one_side(ints, False)
    right = visible_one_side(ints, True)
    for i in range(len(left)):
        left[i] = left[i] or right[i]
    return left


def scores_one_side(ints, reverse):
    """Given a list of integers, return an array of the same size stating the score
    of each value. The score equals the number of trees to the left that are smaller
    than the current value, stopping at the first one that is larger or of equal
    size."""
    if reverse:
        ints = ints[::-1]
    scores = [0 for _ in ints]
    for i, height in enumerate(ints):
        for j in range(i - 1, -1, -1):
            if ints[j] < height:
                scores[i] += 1
            else:
                scores[i] += 1
                break
    if reverse:
        scores = scores[::-1]
    return scores


def scores_both_sides(ints):
    """Given a list of integers, return an array of the same size stating the score
    of each value. The score equals the number of trees to the left and right that are
    smaller than the current value, stopping at the first one that is larger or of
    equal size. Both values are multiplied together."""
    left = scores_one_side(ints, False)
    right = scores_one_side(ints, True)
    for i in range(len(left)):
        left[i] *= right[i]
    return left


def q2(fname):
    f = open(fname)
    columns = list()
    scores = list()
    for i, row in enumerate(f):
        ints = [int(char) for char in row.strip()]
        scores.append(scores_both_sides(ints))
        for j in range(len(ints)):
            if len(columns) <= j:
                columns.append(list())
            columns[j].append(ints[j])
    max_score = 0
    for j in range(len(columns)):
        score_ver = scores_both_sides(columns[j])
        for i in range(len(score_ver)):
            scores[i][j] *= score_ver[i]
            if scores[i][j] > max_score:
                max_score = scores[i][j]
    print(max_score)
    f.close()


def q1(fname):
    f = open(fname)
    columns = list()
    visible = list()
    for i, row in enumerate(f):
        ints = [int(char) for char in row.strip()]
        visible.append(visible_both_sides(ints))
        for j in range(len(ints)):
            if len(columns) <= j:
                columns.append(list())
            columns[j].append(ints[j])
    n_visible = 0
    for j in range(len(columns)):
        visible_ver = visible_both_sides(columns[j])
        for i in range(len(visible_ver)):
            visible[i][j] = visible[i][j] or visible_ver[i]
            n_visible += visible[i][j]
    print(n_visible)
    f.close()


if __name__ == "__main__":
    fname = "day8.txt"
    q1(fname)
    q2(fname)
