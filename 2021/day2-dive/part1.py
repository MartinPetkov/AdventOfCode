# Run as:
# python3 part1.py [input|sample]

import sys

def solve(data):
  distance = 0
  depth = 0
  lines = [l.strip() for l in data.splitlines() if l.strip()]
  for line in lines:
    direction, amount = line.split()
    amount = int(amount)
    if direction == 'forward':
      distance += amount
    elif direction == 'down':
      depth += amount
    elif direction == 'up':
      depth -= amount

    if depth < 0:
      depth = 0

  return distance * depth


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
