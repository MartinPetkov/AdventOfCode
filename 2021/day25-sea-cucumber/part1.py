# Run as:
# python3 part1.py [input|sample]

import sys


def print_grid(grid):
  print('\n'.join([''.join(row) for row in grid]))


def make_swaps(grid, swaps):
  for ((x1,y1), (x2,y2)) in swaps:
    grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]


def solve(data):
  grid = [list(line.strip()) for line in data.splitlines() if line.strip()]
  height = len(grid)
  width = len(grid[0])

  cucumbers_moved = True
  move = 0
  #print('Initial state:')
  #print_grid(grid)
  while cucumbers_moved:
    cucumbers_moved = False

    # Move east
    swaps = []
    for x, row in enumerate(grid):
      for y in range(len(row)):
        cucumber = grid[x][y]
        if cucumber != '>':
          continue

        next_right = (y+1) % width
        right_spot = grid[x][next_right]
        if right_spot == '.':
          cucumbers_moved = True
          swaps.append(((x,y), (x,next_right)))
    make_swaps(grid, swaps)

    # Move south
    swaps = []
    for x, row in enumerate(grid):
      for y in range(len(row)):
        cucumber = grid[x][y]
        if cucumber != 'v':
          continue

        next_down = (x+1) % height
        down_spot = grid[next_down][y]
        if down_spot == '.':
          cucumbers_moved = True
          swaps.append(((x,y), (next_down,y)))
    make_swaps(grid, swaps)

    move += 1
    #print(f'\nAfter {move} step{"s" if move > 1 else ""}:')
    #print_grid(grid)

  return move


def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
