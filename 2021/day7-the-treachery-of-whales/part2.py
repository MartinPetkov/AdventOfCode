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

  # Track the total distance travelled for all crabs to reach each position.
  distances = [0] * num_positions

  # Calculate all the distances for crabs moving from the left.
  for i, crab_squad in enumerate(positions):
    # Since crab squads use up more fuel with each move, calculate the
    # distance travelled individually per squad.
    fuel_usage = 1
    distance_travelled = 0
    for p in range(i+1, num_positions):
      distance_travelled += crab_squad * fuel_usage
      distances[p] += distance_travelled
      fuel_usage += 1

  # Calculate all the distances for crabs moving from the right.
  for i, crab_squad in reversed(list(enumerate(positions))):
    # Since crab squads use up more fuel with each move, calculate the
    # distance travelled individually per squad.
    fuel_usage = 1
    distance_travelled = 0
    for p in range(i-1, -1, -1):
      distance_travelled += crab_squad * fuel_usage
      distances[p] += distance_travelled
      fuel_usage += 1

  # Now we have that for each position in distances, that's the distance
  # travelled by all crabs from the left and the right to get there.

  return min(distances)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
