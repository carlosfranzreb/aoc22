her_options = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
my_options = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}
options = list(her_options.values())
her_keys = list(her_options.keys())
round_points = {"X": 0, "Y": 3, "Z": 6}
hand_points = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}
hand_point_values = list(hand_points.values())

game_rules = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3],
]

points = 0
with open("day2.txt") as f:
    for line in f:
        her, me = line.strip().split(" ")
        round = round_points[me]
        hand = hand_point_values[game_rules[her_keys.index(her)].index(round)]
        points += round + hand

print(points)
