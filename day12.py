from string import ascii_lowercase


def create_map(fname):
    """Given the file with the input data, return the map, the start position and the
    end position. Each letter in the map is replaced by its index in the alphabet. Return
    also a list of lists with the same dimensions as the map, but filled with infinity."""
    # split the alphabet into a list of letters
    letters = list(ascii_lowercase)
    map, paths = list(), list()
    start, end = None, None
    with open(fname) as f:
        for line in f:
            map.append(list())
            paths.append(list())
            for char in line.strip():
                if char == "S":
                    start = [len(map) - 1, len(map[-1])]
                    map[-1].append(letters.index("a"))
                elif char == "E":
                    end = [len(map) - 1, len(map[-1])]
                    map[-1].append(letters.index("z"))
                else:
                    map[-1].append(letters.index(char))
                paths[-1].append(float("inf"))
    return map, paths, start, end


def shortest_paths(map, paths, start, end):
    """Given the map, the paths, the start position and the end position, compute the
    shortest path from the start to the end. Do so with dynamic programming, filling
    the paths list with the shortest path to each position."""
    paths[start[0]][start[1]] = 0
    next_pos = [start]
    seen_pos = list()
    while len(next_pos) > 0:
        pos = next_pos.pop(0)
        seen_pos.append(pos)
        for axis in [0, 1]:
            for direction in [-1, 1]:
                new_pos = pos.copy()
                new_pos[axis] += direction
                if not is_valid(map, pos, new_pos):
                    continue
                paths[new_pos[0]][new_pos[1]] = min(
                    paths[pos[0]][pos[1]] + 1,
                    paths[new_pos[0]][new_pos[1]],
                )  # either same or lower path
                if (
                    new_pos not in next_pos
                    and new_pos != end
                    and new_pos not in seen_pos
                ):
                    next_pos.append(new_pos)
    return paths


def is_valid(map, start, end):
    """Check if the move is valid."""
    if end[0] < 0 or end[0] >= len(map):  # valid horizontal move
        return False
    if end[1] < 0 or end[1] >= len(map[0]):  # valid vertical move
        return False
    if map[end[0]][end[1]] > map[start[0]][start[1]] + 1:  # valid height move
        return False
    return True


def best_start(fname):
    """The best starting point is one with elevation 0 and the shortest path to the end."""
    map, paths, _, end = create_map(fname)
    best = float("inf")
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                these_paths = shortest_paths(map, paths, [i, j], end)
                best = min(best, these_paths[end[0]][end[1]])
    return best


if __name__ == "__main__":
    fname = "day12.txt"
    map, paths, start, end = create_map(fname)
    paths = shortest_paths(map, paths, start, end)
    q1 = paths[end[0]][end[1]]
    print(f"Part 1: {q1}")
    q2 = best_start(fname)
    print(f"Part 2: {q2}")
