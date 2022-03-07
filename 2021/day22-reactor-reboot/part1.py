# Run as:
# python3 part1.py [input|sample]

import sys


def coord_range(coords):
  bounds = coords.split('=')[-1]
  c_min, c_max = sorted([int(c) for c in bounds.split('..')])
  if c_min < -50 or c_max > 50:
    return range(0)

  return range(c_min, c_max+1)

def solve(data):
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  reactor = {}
  for reboot_step in lines:
    power, cuboid = reboot_step.split(' ', 1)
    x_range, y_range, z_range = [coord_range(c) for c in cuboid.split(',')]
    for x in x_range:
      for y in y_range:
        for z in z_range:
          reactor[(x,y,z)] = power

  return len([p for p in reactor.values() if p == 'on'])

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
