# Get the data from the test.
from enum import Enum
import aoc
orig_data = aoc.get_input(2).splitlines()
data = []

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    WIN = 1
    LOSS = 2
    TIE = 3

# Process data
for line in orig_data:
    # Parse data.
    opponent = line.split(" ")[0]
    us = line.split(" ")[1]
    if opponent == "A": opponent = Shape.ROCK
    if opponent == "B": opponent = Shape.PAPER
    if opponent == "C": opponent = Shape.SCISSORS
    if us == "X": us = Shape.ROCK
    if us == "Y": us = Shape.PAPER
    if us == "Z": us = Shape.SCISSORS

    # Interpret second column differently for part 2
    forcedresult = Result.TIE
    if us == Shape.ROCK: forcedresult = Result.LOSS
    if us == Shape.SCISSORS: forcedresult = Result.WIN
    actualus = opponent
    if forcedresult == Result.LOSS and opponent == Shape.ROCK: actualus = Shape.SCISSORS
    if forcedresult == Result.WIN and opponent == Shape.ROCK: actualus = Shape.PAPER
    if forcedresult == Result.LOSS and opponent == Shape.PAPER: actualus = Shape.ROCK
    if forcedresult == Result.WIN and opponent == Shape.PAPER: actualus = Shape.SCISSORS
    if forcedresult == Result.LOSS and opponent == Shape.SCISSORS: actualus = Shape.PAPER
    if forcedresult == Result.WIN and opponent == Shape.SCISSORS: actualus = Shape.ROCK
    data.append((opponent, us, actualus))

def score(opponent, us):
    result = Result.TIE
    if us == Shape.ROCK and opponent == Shape.PAPER: result = Result.LOSS
    if us == Shape.ROCK and opponent == Shape.SCISSORS: result = Result.WIN
    if us == Shape.PAPER and opponent == Shape.SCISSORS: result = Result.LOSS
    if us == Shape.PAPER and opponent == Shape.ROCK: result = Result.WIN
    if us == Shape.SCISSORS and opponent == Shape.ROCK: result = Result.LOSS
    if us == Shape.SCISSORS and opponent == Shape.PAPER: result = Result.WIN
    score = 0
    if result == Result.TIE: score += 3
    if result == Result.WIN: score += 6
    if us == Shape.ROCK: score += 1
    if us == Shape.PAPER: score += 2
    if us == Shape.SCISSORS: score += 3
    return score

# Answer 1
print(f"Answer to part 1: {sum([score(x[0], x[1]) for x in data])}")

# Answer 2
print(f"Answer to part 2: {sum([score(x[0], x[2]) for x in data])}")
