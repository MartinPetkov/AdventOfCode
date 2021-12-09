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
  num_boards = len(boards)
  boards_won = set()
  for num in numbers:
    for i, board in enumerate(boards):
      # Skip boards that have already won.
      if i in boards_won:
        continue

      if board.mark_num(num):
        # Board won.
        # If it's the last to win, return the result.
        if len(boards_won) == num_boards - 1:
          return int(num) * board.sum_unmarked()
        # Else, remove it from the race.
        boards_won.add(i)

  return 0


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
