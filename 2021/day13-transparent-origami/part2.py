# Run as:
# python3 part1.py [input|sample]

import sys


class Fold:
  def __init__(self, fold_instruction):
    coord = fold_instruction.split()[-1]
    direction, line = coord.split('=')
    self.direction = direction
    self.line = int(line)

  def __repr__(self):
    return f'fold along {self.direction}={self.position}'

def draw(points):
  # Find the edges of both coordinate dimensions.
  endx = max([x for (x,y) in points])
  endy = max([y for (x,y) in points])
  for y in range(endy+1):
    for x in range(endx+1):
      symbol = '█' if (x,y) in points else '.'
      print(symbol, end='')
    print()

def solve(data):
  lines = [line.strip() for line in data.splitlines() if line.strip()]

  points = {tuple(map(int, line.split(','))) for line in lines if ',' in line}
  folds = [Fold(line) for line in lines if 'fold ' in line]

  # Now do the folds.
  for fold in folds:
    if fold.direction == 'x':
      # Fold left at the x coordinates.
      snapshot = set(points)
      for point in snapshot:
        x, y = point
        # Only consider those to the right of the fold line.
        if x <= fold.line:
          continue

        # Calculate new coordinates using the offset from the fold line.
        new_point = (fold.line - (x - fold.line), y)
        points.remove(point)
        points.add(new_point)

    elif fold.direction == 'y':
      # Fold up at the y coordinates.
      snapshot = set(points)
      for point in snapshot:
        x, y = point
        # Only consider those to the right of the fold line.
        if y <= fold.line:
          continue

        # Calculate new coordinates using the offset from the fold line.
        new_point = (x, fold.line - (y - fold.line))
        points.remove(point)
        points.add(new_point)

  draw(points)
  return len(points)


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
