# Run as:
# python3 part1.py [input|sample]

import sys


CYCLE = 6
BABY_LANTERNFISH_CYCLE = CYCLE + 2
DAYS = 80

def generation(fishes):
  the_next_generation = []
  for fish in fishes:
    # Time to reproduce.
    if fish == 0:
      the_next_generation.append(CYCLE)
      the_next_generation.append(BABY_LANTERNFISH_CYCLE)
    else:
      the_next_generation.append(fish-1)
  return the_next_generation

def solve(data):
  fish = [int(f.strip()) for f in data.strip().split(',')]
  for i in range(DAYS):
    fish = generation(fish)

  return len(fish)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
