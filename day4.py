def get_range(string):
    start, end = string.split("-")
    return list(range(int(start), int(end) + 1))


if __name__ == "__main__":
    # Q1: In how many assignment pairs does one range fully contain the other?
    out = 0
    f = open("day4.txt")
    for line in f:  # a-b,c-d
        first, second = line.strip().split(",")
        a, b = [int(s) for s in first.split("-")]
        c, d = [int(s) for s in second.split("-")]
        if a >= c and b <= d:  # first is subset of second
            out += 1
        elif c >= a and d <= b:  # second is subset of first
            out += 1
    print(out)
    f.close()

    # Q2: How many assignment pairs overlap?
    out = 0
    f = open("day4.txt")
    for line in f:  # a-b,c-d
        first, second = line.strip().split(",")
        a, b = [int(s) for s in first.split("-")]
        c, d = [int(s) for s in second.split("-")]
        if a >= c and b <= d:  # first is subset of second
            out += 1
        elif c >= a and d <= b:  # second is subset of first
            out += 1
        elif a <= c and b >= c:  # overlap where first is further left
            out += 1
        elif c <= a and d >= a:  # overlap where second is further left
            out += 1
        else:
            print(line)
    print(out)
    f.close()
