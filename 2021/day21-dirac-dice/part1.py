# Run as:
# python3 part1.py [input|sample]

import sys


RING_SIZE = 10
DICE = list(range(1,101))
DICE_POS = 0


def move(pos, advance):
  return (((pos-1) + advance) % RING_SIZE) + 1

def roll():
  global DICE_POS
  num_rolls = 3
  dice_sum = 0
  for i in range(num_rolls):
    dice_sum += DICE[DICE_POS]
    DICE_POS = (DICE_POS+1) % len(DICE)
  return dice_sum, num_rolls

def solve(data):
  lines = data.splitlines()
  p1 = int(lines[0][-1])
  p2 = int(lines[1][-1])

  p1_score = 0
  p2_score = 0
  total_rolls = 0
  while True:
    # Move p1
    distance, rolls = roll()
    total_rolls += rolls
    p1 = move(p1, distance)
    p1_score += p1
    if p1_score >= 1000:
      break

    # Move p2
    distance, rolls = roll()
    total_rolls += rolls
    p2 = move(p2, distance)
    p2_score += p2
    if p2_score >= 1000:
      break

  print(f'Rolled {total_rolls} number of times, score: P1={p1_score} P2={p2_score}')
  return total_rolls * min(p1_score, p2_score)

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
