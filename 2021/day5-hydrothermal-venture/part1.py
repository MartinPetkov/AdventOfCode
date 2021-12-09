# Run as:
# python3 part1.py [input|sample]

import sys

from collections import defaultdict
from pprint import pprint


def solve(data):
  lines = [l.strip() for l in data.splitlines() if l.strip()]

  # A set of points, don't assume grid size.
  grid = defaultdict(int)
  overlaps = 0
  for line in lines:
    start, end = line.split('->')
    start, end = [tuple(int(coord) for coord in point.strip().split(',')) for point in line.split('->')]

    # As per instructions, only consider horizontal and vertical lines.
    points = []
    if start[0] == end[0]:
      x = start[0]
      end1 = min(start[1], end[1])
      end2 = max(start[1], end[1])
      points = [(x,y) for y in range(end1, end2+1)]
    elif start[1] == end[1]:
      y = start[1]
      end1 = min(start[0], end[0])
      end2 = max(start[0], end[0])
      points = [(x,y) for x in range(end1, end2+1)]

    for point in points:
      grid[point] += 1
      if grid[point] == 2:
        overlaps += 1

  return overlaps


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
