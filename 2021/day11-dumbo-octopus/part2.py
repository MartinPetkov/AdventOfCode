# Run as:
# python3 part1.py [input|sample]

import sys

STEPS = 1000

def solve(data):
  # Try to do this in one pass.
  lines = [line.strip() for line in data.splitlines() if line.strip()]
  octopi = {
    (x,y): int(energy_level)
    for x,row in enumerate(lines)
    for y,energy_level in enumerate(list(row))
  }

  for step in range(STEPS):
    # Count flashes per step.
    num_flashes = 0

    # First increase all energy levels by 1.
    flashes = set()
    for position in octopi:
      octopi[position] += 1
      # If its energy is too high, flash it.
      if octopi[position] > 9:
        flashes.add(position)

    # Now flash any that are above 9.
    while flashes:
      position = flashes.pop()
      num_flashes += 1

      # Set its energy back down to 0.
      octopi[position] = 0

      # Flash surrounding octopi if their energy is > 0
      # Diagonals are considered adjacent.
      x, y = position
      adjacent = [
        (x-1,y), (x+1,y),      # Horizontal
        (x,y-1), (x,y+1),      # Vertical
        (x-1,y-1), (x-1,y+1),  # Left diagonals
        (x+1,y-1), (x+1,y+1),  # Right diagonals
      ]
      for adj in adjacent:
        # Out of bounds.
        if adj not in octopi:
          continue

        # Ignore already-flashed octopi. Energy should never be 0 without a
        # flash, since the first round increases all energy by 1.
        if octopi[adj] == 0:
          continue

        octopi[adj] += 1
        # If its energy is too high, flash it.
        if octopi[adj] > 9:
          flashes.add(adj)

    if num_flashes == len(octopi):
      return step + 1

  return None


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
