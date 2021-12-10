# Run as:
# python3 part1.py [input|sample]

import sys


CYCLE = 6
BABY_LANTERNFISH_CYCLE = CYCLE + 2
DAYS = 256

def solve(data):
  fish = [int(f) for f in data.strip().split(',')]
  #return solve2(fish, DAYS)

  # Track population for fish per day in cycle.
  # Include 0 and the starting day of a baby lanternfish cycle.
  # Initial set should have no fish on days 7-8, since none are babies.
  # Add +1 because range is exclusive.
  upper_bound = BABY_LANTERNFISH_CYCLE + 1
  population = [fish.count(i) for i in range(upper_bound)]

  # For each day, increase the population on a particular day of the cycle
  # by the number of fish that many days back in the cycle.
  # This creates a rolling sum for each day of a cycle.
  for day in range(DAYS):
    population[(day + CYCLE + 1) % upper_bound] += population[day % upper_bound]

  print(population)
  return sum(population)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
