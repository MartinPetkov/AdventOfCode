# Run as:
# python3 part1.py [input|sample]

import sys


def solve(data):
  # Displays can be represented as sets of segments.
  # Part 1 is pretty simple, just count unique numbers of digits.

  num_uniq = 0
  for line in data.splitlines():
    line = line.strip()
    output = line.split('|')[1].strip().split()
    # 1 = 2 segments
    # 4 = 4 segments
    # 7 = 3 segments
    # 8 = 7 segments
    num_uniq += len(list(filter(lambda out: len(out) in [2,4,3,7], output)))

  return num_uniq


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
