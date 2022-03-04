# Run as:
# python3 part1.py [input|sample]

import functools
import itertools
import sys


RING_SIZE = 10
DICE = list(range(1,101))
DICE_POS = 0


@functools.cache
def wins(p1, p2, p1_score, p2_score):
  wins_1 = 0
  wins_2 = 0
  for rolls in itertools.product((1, 2, 3), repeat=3):
    # Roll this possibility and advance p1
    rolls = sum(rolls)
    new_p1 = (((p1-1) + rolls) % 10) + 1
    new_p1_score = p1_score + new_p1

    # The game ends as soon as p1 wins, stop recursing
    if new_p1_score >= 21:
      wins_1 += 1
      continue

    # Otherwise, keep playing as p2
    # The cache prevents this from turning our CPU into a grill
    new_wins_2, new_wins_1 = wins(p2, new_p1, p2_score, new_p1_score)

    # Record the wins for both players that particular recursive call
    wins_1 += new_wins_1
    wins_2 += new_wins_2

  return wins_1, wins_2

def solve(data):
  lines = data.splitlines()
  p1 = int(lines[0][-1])
  p2 = int(lines[1][-1])

  # Start playing out game states.
  p1_wins, p2_wins = wins(p1, p2, 0, 0)
  print(f'P1 wins in {p1_wins} universes')
  print(f'P2 wins in {p2_wins} universes')

  return max(p1_wins, p2_wins)

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
