class Marker:
    def __init__(self, length):
        self.chars = list()
        self.skip = 0
        self.length = length

    def move(self, char):
        """Remove the first char of the list and add the given one in last
        position. If the given char is already in the list, set the skip
        attribute to the index of the char in the list. The next `index` chars
        will be moved automatically, again checking for duplicates. Return true
        if after the move, all four chars are different."""
        if char in self.chars:
            new_skip = self.last_index(char)
            if new_skip > self.skip:
                self.skip = new_skip
        if len(self.chars) == self.length:
            self.chars.pop(0)
        self.chars.append(char)
        if self.skip > 0:
            self.skip -= 1
        return len(self.chars) == self.length and self.skip == 0

    def last_index(self, char):
        """Return the last index of the given char in the list."""
        for i in range(len(self.chars) - 1, -1, -1):
            if self.chars[i] == char:
                return i + 2  # +2 because skip is decremented after each move


if __name__ == "__main__":
    with open("day6.txt") as f:
        chars = f.read()
    marker = Marker(14)
    skip = 0
    for i, char in enumerate(chars):
        done = marker.move(char)
        if done is True:
            print(i, char, marker.chars)
            break
