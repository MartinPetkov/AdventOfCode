# Run as:
# python3 part1.py [input|sample]

import sys


class Cuboid:
  def __init__(self, power, x_start, x_end, y_start, y_end, z_start, z_end):
    self.power = power
    self.x_start = x_start
    self.x_end = x_end
    self.y_start = y_start
    self.y_end = y_end
    self.z_start = z_start
    self.z_end = z_end

  def on(self):
    return self.power == 'on'

def coord_range(coords):
  bounds = coords.split('=')[-1]
  return sorted([int(c) for c in bounds.split('..')])

def cuboid_from_reboot_step(reboot_step):
  power, ranges = reboot_step.split(' ', 1)
  x_range, y_range, z_range = ranges.split(',')
  x_range = coord_range(x_range)
  y_range = coord_range(y_range)
  z_range = coord_range(z_range)
  return Cuboid(power, x_range[0], x_range[1], y_range[0], y_range[1], z_range[0], z_range[1])


# Returns the cuboid at the intersection
# This is kind of intuitive across the dimensions:
# - the x range start is the maximum of the two x range starts
# - the x range end is the minimum of the two x range ends
# - same for the y ranges
# - same for the z ranges
# If the second cuboid is added we subtract the intersection. That way,
# we end up with volume(cuboid1) + volume(cuboid2) - intersection
# which is exactly what we want to avoid double-counting the intersection.
def intersection(cuboid1, cuboid2):
    inter_cuboid = Cuboid(
      power='off' if cuboid2.on() else 'on',
      # x range
      x_start=max(cuboid1.x_start, cuboid2.x_start),
      x_end=min(cuboid1.x_end, cuboid2.x_end),
      # y range
      y_start=max(cuboid1.y_start, cuboid2.y_start),
      y_end=min(cuboid1.y_end, cuboid2.y_end),
      # z range
      z_start=max(cuboid1.z_start, cuboid2.z_start),
      z_end=min(cuboid1.z_end, cuboid2.z_end),
    )

    # If the start is ever after the end on any dimension, then there is
    # no intersection.
    if (inter_cuboid.x_start > inter_cuboid.x_end
        or inter_cuboid.y_start > inter_cuboid.y_end
        or inter_cuboid.z_start > inter_cuboid.z_end):
      return None

    return inter_cuboid


def solve(data):
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  # List of reactor core cuboids
  reactor = []

  # Parse all reboot steps and track intersecting cuboids
  for reboot_step in lines:
    cuboid = cuboid_from_reboot_step(reboot_step)

    # If it's on, mark it for adding
    to_add = [cuboid] if cuboid.on() else []

    # Find all the cuboids it intersects with in the core so far
    for core in reactor:
      inter_cuboid = intersection(cuboid, core)
      if inter_cuboid is not None:
        to_add.append(inter_cuboid)
    reactor += to_add

  # Now count how many cores are on by adding or subtracting the volumes of the
  # cuboids
  on = 0
  for core in reactor:
    # Standard volume calculation
    volume = (core.x_end - core.x_start + 1) * (core.y_end - core.y_start + 1) * (core.z_end - core.z_start + 1)
    # Add or subtract depending on the power setting
    if core.on():
      on += volume
    else:
      on -= volume

  return on

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
