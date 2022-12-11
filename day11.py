from math import gcd
from functools import reduce


class Bag:
    """A bag of a monkey's items. get() retrieves the item at the beginning
    of the list and add() appends the new item to the end of the list."""

    def __init__(self, items):
        self.items = items

    def get(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return None

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


class Monkey:
    """A monkey starts with a bag of items. At each step, it takes an item from the
    bag and inspects it with its operation. Afterwards, the value of the item is
    divided by 3, before the monkey's test is performed. The result of this test
    determines to which monkey the item is passed."""

    def __init__(self, id, items, operation, test_value, false_monkey, true_monkey):
        self.id = id
        self.bag = Bag(items)
        self.operation = operation
        self.test_value = test_value
        self.false_monkey = false_monkey
        self.true_monkey = true_monkey
        self.n_inspections = 0

    def __repr__(self):
        return self.id

    def step(self):
        while len(self.bag) > 0:
            item = self.bag.get()
            new_value = self.operation(item) // 3
            if new_value % self.test_value == 0:
                self.true_monkey.bag.add(new_value)
            else:
                self.false_monkey.bag.add(new_value)
            self.n_inspections += 1

    def step_q2(self, divisor):
        while len(self.bag) > 0:
            item = self.bag.get()
            new_value = self.operation(item) % divisor
            if new_value % self.test_value == 0:
                self.true_monkey.bag.add(new_value)
            else:
                self.false_monkey.bag.add(new_value)
            self.n_inspections += 1


def parse_operation(string):
    """Given a string where an operation is performed, return a lambda function
    that performs the operation. Operations have the form new = old op value,
    where op is one of + or *."""
    op_str = string[21]
    value = string[23:]
    if value == "old":
        if op_str == "+":
            return lambda x: x + x
        elif op_str == "*":
            return lambda x: x * x
    else:
        value = int(value)
        if op_str == "+":
            return lambda x: x + value
        elif op_str == "*":
            return lambda x: x * value


def init_monkey(lines):
    """Given the six lines that describe a monkey, return a Monkey object."""
    items_str = lines[1][16:]
    return Monkey(
        id=int(lines[0][7:-1]),
        items=[int(item) for item in items_str.split(", ")],
        operation=parse_operation(lines[2]),
        test_value=int(lines[3][19:]),
        false_monkey=int(lines[5][26:]),
        true_monkey=int(lines[4][25:]),
    )


def q1(fname, rounds=20, top=2):
    """Run a step of each monkey for the given number of rounds. Return the
    product of the number of inspections performed by the top monkeys."""
    f = open(fname)
    monkeys = list()
    lines = [line.strip() for line in f]
    for i in range(0, len(lines), 7):
        monkeys.append(init_monkey(lines[i : i + 6]))
    for monkey in monkeys:
        monkey.false_monkey = monkeys[monkey.false_monkey]
        monkey.true_monkey = monkeys[monkey.true_monkey]
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.step()
    monkeys.sort(key=lambda x: x.n_inspections, reverse=True)
    result = 1
    for i in range(top):
        result *= monkeys[i].n_inspections
    f.close()
    return result


def q2(fname, rounds=10000, top=2):
    """Run a step of each monkey for the given number of rounds. Return the
    product of the number of inspections performed by the top monkeys."""
    f = open(fname)
    monkeys = list()
    lines = [line.strip() for line in f]
    for i in range(0, len(lines), 7):
        monkeys.append(init_monkey(lines[i : i + 6]))
    for monkey in monkeys:
        monkey.false_monkey = monkeys[monkey.false_monkey]
        monkey.true_monkey = monkeys[monkey.true_monkey]
    sum_tests = [m.test_value for m in monkeys]
    # compute the minimum common multiple of all test values
    mcm = reduce(lambda x, y: x * y // gcd(x, y), sum_tests)
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.step_q2(mcm)
    monkeys.sort(key=lambda x: x.n_inspections, reverse=True)
    result = 1
    for i in range(top):
        result *= monkeys[i].n_inspections
    f.close()
    return result


if __name__ == "__main__":
    print(q2("day11.txt"))
    # this does not work bc it has to be divisuble by all test
    # I need to multiply all test values and use that to keep
    # the item values in check
