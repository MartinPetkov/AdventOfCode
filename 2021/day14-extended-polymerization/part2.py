# Run as:
# python3 part1.py [input|sample]

import sys
from collections import defaultdict

STEPS = 40

def solve(data):
  lines = [line.strip() for line in data.splitlines()]

  rules = dict([tuple(r.strip() for r in rule.split(' -> ')) for rule in lines[2:]])

  # Need a new approach

  # Split into pairs.
  polymer = lines[0]
  pairs = defaultdict(int)
  for i, poly in enumerate(polymer[:-1]):
    pairs[f'{poly}{polymer[i+1]}'] += 1

  # Track the number of each letter.
  counts = defaultdict(int)
  for c in polymer:
    counts[c] = polymer.count(c)

  # Track how many there is of each pair.
  # In each step, for each pair:
  #  * Create two more pairs based on the rule.
  #  * Delete the current pair.
  for step in range(STEPS):
    next_pairs = defaultdict(int)
    for pair, num_pair in pairs.items():
      # If it matches a rule, split it into the same number of two other pairs.
      if pair in rules:
        rule = rules[pair]
        a, b = pair
        next_pairs[f'{a}{rule}'] += num_pair
        next_pairs[f'{rule}{b}'] += num_pair

        # Only update counters when a new letter is added.
        counts[rule] += num_pair

      # Otherwise, just carry it over.
      else:
        next_pairs[pair] = num_pair
    pairs = next_pairs

  return max(counts.values()) - min(counts.values())


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
