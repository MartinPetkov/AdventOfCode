# Run as:
# python3 part1.py [input|sample]

import sys

SCORE = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
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

  scores = []
  for line in lines:
    corrupted = False

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
        corrupted = True
        break

      expected_closer = OPENERS[stack[-1]]
      if delim != expected_closer:
        corrupted = True
        break

      # Valid closer. Remove from the stack.
      stack.pop()

    # Unfinished line. Time to score it.
    if not corrupted and len(stack) > 0:
      score = 0
      while stack:
        opener = stack.pop()
        closer = OPENERS[opener]
        print(closer, end='')
        score *= 5
        score += SCORE[closer]
      print(f' - {score}')
      scores.append(score)

  # Get the middle score.
  scores.sort()
  return scores[len(scores)//2]


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
