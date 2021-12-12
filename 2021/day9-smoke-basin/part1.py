# Run as:
# python3 part1.py [input|sample]

import sys
from collections import defaultdict


def solve(data):
  # Try to do this in one pass.
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  heightmap = defaultdict(int)
  lowpoints = defaultdict(lambda: True)
  risksum = 0
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

        # On the last row, this will be the last time a point is seen.
        # If it's still a lowpoint, record it.
        if x == len(lines)-1 and lowpoints[left_coord]:
          risksum += 1 + left

      # Look above.
      above_coord = (x-1,y)
      above = heightmap.get(above_coord, None)
      if above is not None:
        # Update the left point and us in relation to it.
        lowpoints[above_coord] &= above < height
        lowpoints[(x,y)] &= above > height

        # In our single pass, this is the last time this point is seen, so
        # if it's still a lowpoint, record it.
        if lowpoints[above_coord]:
          risksum += 1 + above

  # Finally, check the last point.
  if lowpoints[last_coord]:
    risksum += 1 + heightmap[last_coord]

  return risksum


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
