def task1(input_f: str) -> int:
    lines = [list(line.strip()) for line in open(input_f)]
    n_removed = remove_accessible_rolls(lines)[1]
    return n_removed


def remove_accessible_rolls(lines: list[list[str]]) -> tuple[list[list[str]], int]:
    n_accessible = 0
    new_lines = list()
    for row_idx in range(len(lines)):
        new_lines.append(list())
        for col_idx in range(len(lines[0])):
            if lines[row_idx][col_idx] == ".":
                new_lines[-1].append(".")
                continue

            surrounding = 8
            for adj_row_idx, adj_col_idx in [
                (row_idx - 1, col_idx - 1),
                (row_idx - 1, col_idx),
                (row_idx - 1, col_idx + 1),
                (row_idx, col_idx - 1),
                (row_idx, col_idx + 1),
                (row_idx + 1, col_idx - 1),
                (row_idx + 1, col_idx),
                (row_idx + 1, col_idx + 1),
            ]:
                if adj_row_idx < 0 or adj_row_idx >= len(lines):
                    surrounding -= 1
                elif adj_col_idx < 0 or adj_col_idx >= len(lines[0]):
                    surrounding -= 1
                elif lines[adj_row_idx][adj_col_idx] == ".":
                    surrounding -= 1

            if surrounding < 4:
                new_lines[-1].append(".")
                n_accessible += 1
            else:
                new_lines[-1].append("@")

    return new_lines, n_accessible


def task2(input_f: str) -> int:
    lines = [list(line.strip()) for line in open(input_f)]
    n_removed_total = 0
    n_removed = 1
    while n_removed > 0:
        lines, n_removed = remove_accessible_rolls(lines)
        n_removed_total += n_removed

    return n_removed_total


if __name__ == "__main__":
    input_f = "input.txt"
    print("task 1: ", task1(input_f))
    print("task 2: ", task2(input_f))
