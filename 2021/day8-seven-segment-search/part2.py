# Run as:
# python3 part1.py [input|sample]

import sys


def solve(data):
  # Displays can be represented as sets of segments.
  # Part 1 is pretty simple, just count unique numbers of digits.

  numsum = 0
  for line in data.splitlines():
    line = line.strip()
    keys, output = line.split('|')
    keys = [''.join(sorted(k.strip())) for k in keys.split()]
    output = [''.join(sorted(o.strip())) for o in output.split()]

    # Find the trivial keys we know by unique length.
    key_1 = next(k for k in keys if len(k) == 2)
    key_7 = next(k for k in keys if len(k) == 3)
    key_4 = next(k for k in keys if len(k) == 4)
    key_8 = next(k for k in keys if len(k) == 7)

    # Now that we know those particular keys, we can figure out the rest by
    # looking visually at the segments and deducing some rules:
    # len == 5 and includes key_1 -> 3
    # len == 5 and includes (key_4-key_7) -> 5
    # len == 5 else -> 2
    # len == 6 and includes key_4 and includes key_7 -> 9
    # len == 6 and does NOT include key_1 -> 6
    # len == 6 else -> 0
    for key in keys:
      if len(key) == 5:
        if set(key_1).issubset(set(key)):
          key_3 = key
        elif (set(key_4)-set(key_7)).issubset(set(key)):
          key_5 = key
        else:
          key_2 = key
      elif len(key) == 6:
        if (set(key_4)|set(key_7)).issubset(set(key)):
          key_9 = key
        elif not set(key_1).issubset(set(key)):
          key_6 = key
        else:
          key_0 = key

    # Save the encoding and decode the output
    encoding = {
      key_0: '0',
      key_1: '1',
      key_2: '2',
      key_3: '3',
      key_4: '4',
      key_5: '5',
      key_6: '6',
      key_7: '7',
      key_8: '8',
      key_9: '9',
    }
    output = int(''.join([encoding[o] for o in output]))
    numsum += output

  return numsum


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
