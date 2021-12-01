# Run as:
# python3 solve.py input

import sys

def solve(data):
  lines = data.splitlines()
  prev = int(lines[0].strip())
  num_larger = 0
  for line in lines[1:]:
    line = line.strip()
    if not line:
      continue

    cur = int(line)
    if cur > prev:
      num_larger += 1
    prev = cur

  return num_larger

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()

  print(solve(data))


if __name__ == '__main__':
  main()
