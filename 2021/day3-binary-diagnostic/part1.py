# Run as:
# python3 part1.py [input|sample]

import sys

def solve(data):
  lines = [l.strip() for l in data.splitlines() if l.strip()]
  bits = {}
  for line in lines:
    for i, bit in enumerate(line):
      if i not in bits:
        bits[i] = {}
      if bit not in bits[i]:
        bits[i][bit] = 0
      bits[i][bit] += 1

  gamma = ''
  epsilon = ''
  for position in range(len(bits)):
    stats = bits[position]
    most_frequent_bit = max(stats, key=lambda b: stats[b])
    gamma += most_frequent_bit
    least_frequent_bit = min(stats, key=lambda b: stats[b])
    epsilon += least_frequent_bit

  gamma = int(gamma, 2)
  epsilon = int(epsilon, 2)

  return gamma * epsilon


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
