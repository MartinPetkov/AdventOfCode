# Run as:
# python3 part1.py [input|sample]

import sys


# Pixel symbols
L = '#'
D = '.'


def boundaries(coords):
  x_min, x_max, y_min, y_max = 0, 0, 0, 0
  for c in coords:
    x, y = c
    x_min = x if x < x_min else x_min
    x_max = x if x > x_max else x_max
    y_min = y if y < y_min else y_min
    y_max = y if y > y_max else y_max
  return x_min, x_max, y_min, y_max

def print_image(coords):
  x_min, x_max, y_min, y_max = boundaries(coords)
  for x in range(x_min, x_max+1):
    line = ''
    for y in range(y_min, y_max+1):
      line += coords[(x,y)]
    print(line)
  print()

def calculate_pixel(point, coords, algo, default):
  index = ''.join([
    '0' if coords.get(p, default) == D else '1'
    for p in [
      # Top row
      (point[0]-1, point[1]-1),
      (point[0]-1, point[1]),
      (point[0]-1, point[1]+1),
      # Middle row
      (point[0], point[1]-1),
      (point[0], point[1]),
      (point[0], point[1]+1),
      # Bottom row
      (point[0]+1, point[1]-1),
      (point[0]+1, point[1]),
      (point[0]+1, point[1]+1),
    ]
  ])
  index = int(index, 2)
  return algo[index]

def solve(data):
  algo, image = data.split('\n\n', 1)

  # Convert the image to a coordinate map.
  coords = {}
  lines = image.splitlines()
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      coords[(x,y)] = lines[x][y]
  print_image(coords)

  # Default starts at dark
  default = D

  # Expand the image repeatedly
  x_min, x_max, y_min, y_max = boundaries(coords)
  for rounds in range(2):
    # Expand outward by 1. Everything else outside of that area is the default value.
    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1

    # Calculate all the new pixels.
    new_coords = {}
    for x in range(x_min, x_max+1):
      for y in range(y_min, y_max+1):
        new_coords[(x,y)] = calculate_pixel((x,y), coords, algo, default)
    coords = new_coords

    # Print the image.
    print_image(coords)

    # Update the default.
    default = algo[0] if default == D else algo[-1]

  return len([True for pixel in coords.values() if pixel == L])

def main():
  with open(sys.argv[1]) as f:
    data = f.read().strip()
  print(solve(data))

if __name__ == '__main__':
  main()
