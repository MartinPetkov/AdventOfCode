# Run as:
# python3 solve.py input

import sys

def window_sum(lines):
  return sum([int(l.strip()) for l in lines])

def solve(data):
  lines = [l.strip() for l in data.splitlines() if l.strip()]

  # Now use a window.
  window = 3
  prev = window_sum(lines[0:window])

  num_larger = 0
  for i in range(1, len(lines)-window+1):
    cur = window_sum(lines[i:i+window])
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
