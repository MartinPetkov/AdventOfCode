# Run as:
# python3 part1.py [input|sample]

import sys
import math
from collections import defaultdict


def solve(data):
  # Try to do this in one pass.
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  heightmap = defaultdict(int)
  lowpoints = defaultdict(lambda: True)
  last_coord = (0,0)
  for x in range(len(lines)):
    line = lines[x]
    for y in range(len(line)):
      height = int(line[y])
      heightmap[(x,y)] = height
      last_coord = (x,y)

      # Look to the left.
      left_coord = (x,y-1)
      left = heightmap.get(left_coord, None)
      if left is not None:
        # Update the left point and us in relation to it.
        lowpoints[left_coord] &= left < height
        lowpoints[(x,y)] &= left > height

      # Look above.
      above_coord = (x-1,y)
      above = heightmap.get(above_coord, None)
      if above is not None:
        # Update the left point and us in relation to it.
        lowpoints[above_coord] &= above < height
        lowpoints[(x,y)] &= above > height

  # Extract all the lowpoints and find basins from them.
  lowpoints = [k for k,v in lowpoints.items() if v]
  basins = []
  for lowpoint in lowpoints:
    # Expand outwards from this point.
    seen = set()
    queue = [lowpoint]
    basinsize = 0
    while queue:
      (x, y) = queue.pop(0)
      if (x,y) in seen:
        continue

      for around in [(x,y-1), (x-1,y), (x,y+1), (x+1,y)]:
        if around not in heightmap:
          continue
        # From here, we know the point exists.
        # If it's a 9, stop exploring.
        if heightmap[around] == 9:
          continue
        # Otherwise, it's a normal point, add it to be explored.
        queue.append(around)

      # Finished processing this point.
      seen.add((x,y))
      basinsize += 1

    # Record this basin.
    basins.append(basinsize)

  return math.prod(sorted(basins)[-3:])


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
