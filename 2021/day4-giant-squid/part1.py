# Run as:
# python3 part1.py [input|sample]

import sys


class Board:
  class Spot:
    def __init__(self, val, marked=False):
      self.val = val
      self.marked = marked

    def __repr__(self):
      return str(self.val)

  def __init__(self, rows):
    self.rows = []
    for r in rows:
      row = []
      for num in r:
        row.append(self.Spot(num))
      self.rows.append(row)

  # Mark a spot and return whether the board is won.
  def mark_num(self, num):
    solved = False
    for row in self.rows:
      for col_num, spot in enumerate(row):
        if spot.val == num:
          spot.marked = True
          # Check the row and column
          solved = solved or all(s.marked for s in row) or all(r[col_num].marked for r in self.rows)
    return solved

  def sum_unmarked(self):
    return sum([int(spot.val) for row in self.rows for spot in row if not spot.marked])


def solve(data):
  lines = [l.strip() for l in data.splitlines()]
  numbers = [n.strip() for n in lines[0].split(',')]

  # Parse the boards.
  boards = []
  board_lines = []
  for line in lines[2:]:
    if not line.strip():
      boards.append(Board(board_lines))
      board_lines = []
      continue
    board_lines.append([n.strip() for n in line.split()])
  boards.append(Board(board_lines))

  # Play the game.
  for num in numbers:
    for board in boards:
      if board.mark_num(num):
        print('Solved board:')
        print(board.rows)
        return int(num) * board.sum_unmarked()

  return 0


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
