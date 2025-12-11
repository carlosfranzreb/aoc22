class Pile:
    def __init__(self, crates):
        """A pile comprises a list of crates, where the top one is at position 0
        and the bottom one in last position."""
        self.crates = crates

    def get(self):
        """Pop the top crate (i.e. at first position)."""
        return self.crates.pop(0)

    def get_new(self, n):
        """Pop the top n crate (i.e. at first position)."""
        out, self.crates = self.crates[:n], self.crates[n:]
        return out

    def add(self, crate):
        """Add a crate to the top of the pile (i.e. first position)."""
        self.crates.insert(0, crate)

    def add_new(self, crates):
        """Add multiple crates to the top of the pile. The new crates
        as ordered in the same way as the existing ones: with the top one
        in first position."""
        self.crates = crates + self.crates


def init_piles(drawing):
    """Given the drawing of the nine piles, initialize them and return them in a
    list, ordered as they should."""
    piles = [[] for _ in range(9)]
    indices = list(range(1, 9 * 4, 4))
    for line in drawing[:-1]:
        for pile, idx in enumerate(indices):
            if line[idx] != " ":
                piles[pile].append(line[idx])
    return [Pile(crates) for crates in piles]


def process_action(action):
    """Given the string action, return the three relevant numbers: how many crates
    to move, from which pile and to which pile."""
    numbers = [""]
    writing = False
    for char in action:
        if char.isdigit():
            writing = True
            numbers[-1] += char
        elif writing is True:
            writing = False
            numbers.append("")
    return [int(n) for n in numbers[:-1]]


def q1(actions, piles):
    for action in actions:
        amount, from_pile, to_pile = process_action(action)
        for _ in range(amount):
            crate = piles[from_pile - 1].get()
            piles[to_pile - 1].add(crate)
    out = ""
    for pile in piles:
        out += pile.get()
    print(out)


def q2(actions, piles):
    for action in actions:
        amount, from_pile, to_pile = process_action(action)
        crates = piles[from_pile - 1].get_new(amount)
        piles[to_pile - 1].add_new(crates)
    out = ""
    for pile in piles:
        out += pile.get()
    print(out)


if __name__ == "__main__":
    f = open("day5.txt")
    drawing, actions = list(), list()
    draw = True
    for line in f:
        if draw is True:
            if line == "\n":
                draw = False
            else:
                drawing.append(line)
        else:
            actions.append(line)
    piles = init_piles(drawing)
    q2(actions, piles)
