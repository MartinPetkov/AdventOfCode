# Run as:
# python3 part1.py [input|sample]

import sys

SCORE = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

OPENERS = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

CLOSERS = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<',
}

def solve(data):
  # Try to do this in one pass.
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  score = 0
  for line in lines:
    # Place opening characters on the stack as we see them.
    # Remove them as we see the matching closing characters.
    stack = []
    for delim in line:
      if delim in OPENERS:
        # It's an opener. Add to the stack.
        stack.append(delim)
        continue

      # It's a closer. Ensure the stack has its counterpart.
      if len(stack) <= 0:
        score += SCORE[delim]
        break

      expected_closer = OPENERS[stack[-1]]
      if delim != expected_closer:
        score += SCORE[delim]
        break

      # Valid closer. Remove from the stack.
      stack.pop()

  return score


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
