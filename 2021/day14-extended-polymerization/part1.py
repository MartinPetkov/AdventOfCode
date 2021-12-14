# Run as:
# python3 part1.py [input|sample]

import sys

STEPS = 10


def solve(data):
  lines = [line.strip() for line in data.splitlines()]

  polymer = lines[0]
  rules = dict([tuple(r.strip() for r in rule.split(' -> ')) for rule in lines[2:]])

  for step in range(STEPS):
    print(polymer)
    next_polymer = ''
    for i in range(len(polymer)):
      element = polymer[i]
      next_polymer += element

      if i < (len(polymer)-1):
        pair = f'{element}{polymer[i+1]}'
        if pair in rules:
          next_polymer += rules[pair]

    polymer = next_polymer

  most_common = max(polymer, key=polymer.count)
  least_common = min(polymer, key=polymer.count)
  return polymer.count(most_common) - polymer.count(least_common)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
