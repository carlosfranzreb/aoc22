def task1(input_f: str) -> int:
    invalid_ids = list()
    ranges_str = open(input_f).read().split(",")
    for range_str in ranges_str:
        start, end = range_str.split("-")
        n_chars_start, n_chars_end = len(start), len(end)
        start_offset = n_chars_start % 2 != 0

        for n_chars in range(n_chars_start + start_offset, n_chars_end + 1, 2):

            # define the start of the range
            if n_chars > n_chars_start:  # all possible invalid are larger than start
                start_valid = "1" + "0" * (n_chars - 1)
            else:
                start_valid = start

            # gather invalid IDs
            mid_idx = n_chars // 2
            half = start_valid[:mid_idx]
            while int(half * 2) <= int(end):
                if int(half * 2) >= int(start):
                    invalid_ids.append(int(half * 2))

                half = str(int(half) + 1)

    return sum(invalid_ids)


def task2(input_f: str) -> int:
    invalid_ids = set()
    ranges_str = open(input_f).read().split(",")
    for range_str in ranges_str:
        start, end = range_str.split("-")
        n_chars_start, n_chars_end = len(start), len(end)

        for n_chars in range(n_chars_start, n_chars_end + 1):
            for n_repetitions in range(2, n_chars + 1):

                # the number of repetitions must fit in n_chars
                if n_chars % n_repetitions != 0:
                    continue

                # define the start of the range
                if (
                    n_chars > n_chars_start
                ):  # all possible invalid are larger than start
                    start_valid = "1" + "0" * (n_chars - 1)
                else:
                    start_valid = start

                # gather invalid IDs
                split_idx = n_chars // n_repetitions
                sub = start_valid[:split_idx]
                while int(sub * n_repetitions) <= int(end):
                    if int(sub * n_repetitions) >= int(start):
                        invalid_ids.add(int(sub * n_repetitions))

                    sub = str(int(sub) + 1)

    return sum(invalid_ids)


if __name__ == "__main__":
    input_f = "input.txt"
    print("task 1: ", task1(input_f))
    print("task 2: ", task2(input_f))
