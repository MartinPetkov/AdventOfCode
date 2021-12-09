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

    # Determine the points range, diagonal or not.
    startx, starty = start
    endx, endy = end

    stepx = 0
    if startx < endx:
      stepx = 1
    elif startx > endx:
      stepx = -1

    stepy = 0
    if starty < endy:
      stepy = 1
    elif starty > endy:
      stepy = -1

    # Generate points by "stepping" forward across the dimentions of the range.
    points = []
    x = startx
    y = starty
    while True:
      point = (x,y)
      grid[point] += 1
      if grid[point] == 2:
        overlaps += 1

      # If we've reached the end of either range, stop generating points.
      # Be inclusive of the final point in the range.
      x += stepx
      y += stepy
      if stepx != 0 and x == endx + stepx:
        break
      if stepy != 0 and y == endy + stepy:
        break

  return overlaps


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
