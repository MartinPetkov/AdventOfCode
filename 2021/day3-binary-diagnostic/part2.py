# Run as:
# python3 part1.py [input|sample]

import sys
from functools import reduce

# Filter the set of numbers based on the frequency of bits in the given
# position and the mode ('oxygen' or 'co2').
def filter_numbers(numbers, position, mode='oxygen'):
  def collect(collector, elem):
    if elem[position] == '0':
      return (collector[0]+1,collector[1])
    return (collector[0],collector[1]+1)
  num_0s, num_1s = reduce(collect, numbers, (0,0))

  most_frequent = '1'
  least_frequent = '0'
  if num_0s > num_1s:
    most_frequent = '0'
    least_frequent = '1'

  if num_0s == num_1s:
    target = '1' if mode == 'oxygen' else '0'
  elif mode == 'oxygen':
    target = most_frequent
  else:
    target = least_frequent

  return list(filter(lambda n: n[position] == target, numbers))


def solve(data):
  lines = [l.strip() for l in data.splitlines() if l.strip()]
  diagnostics = set(lines)

  # Figure out the oxygen.
  position = 0
  oxygen = filter_numbers(diagnostics, position, 'oxygen')
  while len(oxygen) != 1:
    position += 1
    oxygen = filter_numbers(oxygen, position, 'oxygen')
  oxygenbin = oxygen[0]
  oxygen = int(oxygenbin, 2)
  print(f'Oxygen: {oxygenbin} ({oxygen})')

  # Figure out the co2.
  position = 0
  co2 = filter_numbers(diagnostics, position, 'co2')
  while len(co2) != 1:
    position += 1
    co2 = filter_numbers(co2, position, 'co2')
  co2bin = co2[0]
  co2 = int(co2bin, 2)
  print(f'CO2: {co2bin} ({co2})')

  return oxygen * co2


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
