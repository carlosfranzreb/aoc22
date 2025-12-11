class Valve:
    def __init__(self, id, name, flow_rate, leads_to):
        self.id = id
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to = leads_to

    def __repr__(self):
        return self.name


class Path:
    def __init__(self, current_valve=None, opened=[], pressure=0, time_left=30):
        self.current_valve = current_valve
        self.opened = opened
        self.pressure = pressure
        self.time_left = time_left
        self.done = False if time_left > 0 else True

    def __repr__(self):
        return "-".join(self.opened)

    def add_valve(self, valve, open):
        if self.time_left == 0:
            raise ValueError("No time left")
        elif valve.name in self.opened and open:
            raise ValueError("Valve already open")
        self.current_valve = valve
        self.time_left -= 1
        if open:
            self.opened.append(valve.name)
            self.pressure += valve.flow_rate * open
            self.time_left -= 1
        if self.time_left == 0:
            self.done = True


def parse_input(fname):
    """Return list of valves."""
    valves = list()
    for i, line in enumerate(open(fname)):
        first, second = line.strip().split("; ")
        first_words = first.split(" ")
        name = first_words[1]
        flow_rate = int(first_words[-1].split("=")[-1])
        leads_to = list()
        for word in second.split(" "):
            word = word.replace(",", "")
            if word == word.upper():
                leads_to.append(word)
        valves.append(Valve(i, name, flow_rate, leads_to))
    for valve in valves:
        valve.leads_to = [v for v in valves if v.name in valve.leads_to]
    return valves


def step(path, valve):
    """Given a path and a valve, return the two possible paths that may follow
    from adding this valve (open or closed) to the path. If the valve has already
    been opened in this path, return only one path (the one where it is closed)."""
    paths = []
    options = [False] if valve.name in path.opened else [True, False]
    for open in options:
        new_path = Path(None, path.opened, path.pressure, path.time_left)
        new_path.add_valve(valve, open)
        paths.append(new_path)
    return paths


def q1(valves):
    """Work out the steps to release the most pressure in 30 steps."""
    empty_path = Path()
    paths = step(empty_path, valves[0])
    done = []
    while len(paths) > 0:
        path = paths.pop(0)
        if path.done:
            done.append(path)
        else:
            for valve in path.current_valve.leads_to:
                paths += step(path, valve)
    return max([path.pressure for path in done])


if __name__ == "__main__":
    fname = "test.txt"
    valves = parse_input(fname)
    print(q1(valves))
