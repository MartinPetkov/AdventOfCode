# Run as:
# python3 part1.py [input|sample]

import sys

from collections import defaultdict


def solve(data):
  crabs = sorted([int(c.strip()) for c in data.split(',')])

  # Count how many crabs are in each position.
  num_positions = max(crabs) + 1
  positions = [0] * num_positions
  for crab in crabs:
    positions[crab] += 1
  print(positions)

  # Track the total distance travelled for all crabs to reach each position.
  distances = [0] * num_positions

  # Calculate all the distances for crabs moving from the left.
  crab_squad = 0
  distance = 0
  for i, crabs_at_position in enumerate(positions):
    # Advance the whole squad by one.
    distance += crab_squad
    distances[i] += distance

    # Pick up the crabs in the current position and add them to the squad.
    crab_squad += crabs_at_position

  # Calculate all the distances for crabs moving from the right.
  crab_squad = 0
  distance = 0
  for i, crabs_at_position in reversed(list(enumerate(positions))):
    # Advance the whole squad by one.
    distance += crab_squad
    distances[i] += distance

    # Pick up the crabs in the current position and add them to the squad.
    crab_squad += crabs_at_position

  # Now we have that for each position in distances, that's the distance
  # travelled by all crabs from the left and the right to get there.

  return min(distances)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
